from django.contrib import admin
import xadmin
from .models import Post,Tags,Category
# Register your models here.

xadmin.site.register(Post)
xadmin.site.register(Tags)
xadmin.site.register(Category)
