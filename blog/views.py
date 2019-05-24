from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView
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
        queryset = super(IndexView,self).get_queryset()
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

    def get_context_data(self,  **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        order = self.request.GET.get('order')
        search = self.request.GET.get('search')
        if search and search != None:
            context.update({ 'search': search})
        if order and order != 'None':
            context.update({'order': order})
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


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

class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:index',)

class PostUpdateView(UpdateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm

# 删文章
def post_delete(request, pk):
    # 根据 id 获取需要删除的文章
    post = Post.objects.get(id=pk)
    # 调用.delete()方法删除文章
    post.delete()
    # 完成删除后返回文章列表
    return redirect("blog:post_delete")