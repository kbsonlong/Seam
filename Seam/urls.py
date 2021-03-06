"""Seam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import xadmin
from xadmin.plugins import xversion
from rest_framework import routers

from api.views import blog
from blog.views import IndexView


xadmin.autodiscover()
xversion.register_models()
router = routers.DefaultRouter()
router.register(r'posts', blog.PostApiView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('password-reset/',include('password_reset.urls')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('',IndexView.as_view(),name='index'),
    path('userprofile/',include('userprofile.urls',namespace='userprofile')),
    path('comment/',include('comments.urls',namespace='comment')),
    path('inbox/notifications/', include('notifications.urls', namespace='notifications')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)