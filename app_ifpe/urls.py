"""app_ifpe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from blog import views
from rest_auth import urls

router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin-site'),
    url(r'^', include(router.urls)),
    # url(r'^', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^rest-auth/', include('rest_auth.urls')),

]
