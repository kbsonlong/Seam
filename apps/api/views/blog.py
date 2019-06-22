from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Post
from api.serializers import PostSerializers


class PostApiView(viewsets.ModelViewSet):
    """
    API endpoint that allows Post to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    @method_decorator(login_required)
    def dispatch(self,  *args, **kwargs):
        return super(PostApiView,self).dispatch(*args,**kwargs)