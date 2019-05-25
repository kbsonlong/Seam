from django.contrib import admin
import xadmin
# Register your models here.
from .models import Comment

xadmin.site.register(Comment)