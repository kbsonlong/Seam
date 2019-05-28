from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# ##引入信号
# from django.db.models.signals import post_save
# #信号接收器的装饰器
# from django.dispatch import receiver
# # Create your models here.
#
# class Profile(models.Model):
#     ##与User构成一对一关系
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     phone = models.IntegerField(blank=True,null=True)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/',blank=True,null=True)
#     bio = models.TextField(blank=True,null=True)
#
#     def __str__(self):
#         return 'user {}'.format(self.user.username)
#
#
# # 信号接收函数，每当新建 User 实例时自动调用
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# # 信号接收函数，每当更新 User 实例时自动调用
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class UserProfile(AbstractUser):
    username = models.CharField(verbose_name="用户名",unique=True,max_length=50,null=True)
    email = models.CharField(verbose_name="电子邮箱",max_length=50)
    password = models.CharField(verbose_name="密码",max_length=128)
    phone = models.IntegerField(blank=True,null=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/',blank=True,null=True)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username
