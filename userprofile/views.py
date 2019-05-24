from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm,UserRegisterForm,ProfileForm
from .models import Profile
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            ##.cleaned_data清洗出合法数据
            data = user_login_form.cleaned_data
            user = authenticate(username = data['username'],password = data ['password'])
            if user:
                #将用户数据保存在session中
                login(request,user)
                return redirect("blog:index")
            else:
                return HttpResponse("账号或密码输入错误，请重新输入")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form =UserLoginForm()
        context = {'form':user_login_form}
        return render(request,'userprofile/login.html',context)
    else:
        return HttpResponse("请使用GET或者POST请求")

def user_logout(request):
    logout(request)
    return redirect("blog:index")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.data['password'])
            new_user.save()
            login(request,new_user)
            return redirect("blog:index")
        else:
            return HttpResponse("注册表单输入有误，请重新输入")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form':user_register_form}
        return render(request,'userprofile/register.html',context)
    else:
        return HttpResponse("请使用GET或者POST请求")




@login_required(login_url="/userprofile/login")
def user_delete(request,id):
    user = User.objects.get(pk=id)
    if request.user == user:
        logout(request)
        user.is_active = 0
        user.save()
        return redirect("blog:index")
    elif request.user.is_staff:
        user.delete()
        return HttpResponse("用户{}删除成功".format(user))
    else:
        return HttpResponse("你没有删除操作权限")

@login_required(login_url='/userprofile/login/')
def profile_edit(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user_id=id)

    if request.method =='POST':
        if request.user != user:
            return HttpResponse('你没有权限修改此用户信息')

        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            # 如果 request.FILES 存在文件，则保存
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]
            profile.save()

            return redirect("userprofile:edit",id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    else:
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/profile.html', context)