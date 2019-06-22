from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.db.models import Q
import markdown
from markdown.extensions.toc import TocExtension
from .models import Post,Category,Tags
from .forms import PostForm
from comments.forms import CommentForm
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request,'blog/index.html',context)

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 3


    def get_queryset(self):
        order = self.request.GET.get('order')
        searched = self.request.GET.get('search')
        if searched and searched != None:
            search = searched
        else:
            search = None
        if order and order != 'None':
            ordering = '-{}'.format(order)
        else:
            ordering = None
        # 用户搜索逻辑
        if search and order:
            # 用 Q对象 进行联合搜索
            queryset = self.model.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by(ordering)
        elif search:
            queryset = self.model.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
        elif order:
            queryset = self.model.objects.all().order_by(ordering)
        else:
            queryset = self.model.objects.all()

        return queryset

    ##添加上下文
    def get_context_data(self,  **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        order = self.request.GET.get('order')
        search = self.request.GET.get('search')
        if search and search != None:
            context.update({ 'search': search})
        if order and order != 'None':
            context.update({'order': order})
        return context


##分类
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(
            create_time__year=year,
            create_time__month=month
        )


class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tags, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)

##展示文章详情页
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    # 获取文章内容
    def get_object(self, queryset=None):
        post = super(PostDetailView,self).get_object(queryset=None)
        post.increase_views()
        md = markdown.Markdown(extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    ##获取上下文
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        # 获取这篇 post 下的全部评论
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context



## 发布新文章类视图，待完善
class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:index',)

    def get_success_url(self):
        success_url = self.success_url
        print(self.kwargs)
        return success_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm

    def get_queryset(self):
        queryset = self.model.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_success_url(self):
        success_url = reverse_lazy('blog:detail',args=[self.kwargs.get('pk')] )
        return success_url

    def form_valid(self, form):
        print(self.request.FILES)
        # form.instance.avatar = self.request.FILES.name
        print(self.kwargs.get('avatar'))

        form.instance.tags.set = self.kwargs.get('tags')
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:index', )

# 删文章
def post_delete(request, pk):
    # 根据 id 获取需要删除的文章
    post = Post.objects.get(id=pk)
    # 调用.delete()方法删除文章
    post.delete()
    # 完成删除后返回文章列表
    return redirect("blog:post_delete")