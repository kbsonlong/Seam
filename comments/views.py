from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from blog.models import Post
from notifications.signals import notify
from django.contrib.auth.models import User
from .models import Comment
from .forms import CommentForm




@login_required(login_url='/userprofile/login/')
# 新增参数 parent_comment_id
def post_comment(request, post_pk, parent_comment_id=None):
    article = get_object_or_404(Post, pk=post_pk)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        print(request.POST,comment_form.is_valid())
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = article
            new_comment.user = request.user

            # 给管理员发送通知
            if not request.user.is_superuser:
                notify.send(
                    request.user,
                    recipient=User.objects.filter(is_superuser=1),
                    verb='回复了你',
                    target=article,
                    action_object=new_comment,
                )

            # 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get(pk=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                # 给其他用户发送通知
                if not parent_comment.user.is_superuser:
                    notify.send(
                        request.user,
                        recipient=parent_comment.user,
                        verb='回复了你',
                        target=article,
                        action_object=new_comment,
                    )
                return HttpResponse('200 OK')
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理 GET 请求
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'form': comment_form,
            'post_pk': post_pk,
            'parent_comment_id': parent_comment_id
        }
        return render(request, 'comment/reply.html', context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")