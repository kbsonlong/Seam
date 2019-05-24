from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView
# Create your views here.
from blog.models import Post
from .forms import CommentForm

# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect(post)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': comment_form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    # 处理错误请求
    else:
        return redirect(post)
