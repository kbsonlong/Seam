from django.contrib import admin
import xadmin
from .models import Post,Category,Tags
# Register your models here.

xadmin.site.register(Post)
xadmin.site.register(Category)
xadmin.site.register(Tags)
