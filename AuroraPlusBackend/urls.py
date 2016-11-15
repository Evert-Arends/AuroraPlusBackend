"""AuroraPlusBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from AuroraPlusBack import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<username>\w{1,50})$', views.profile_page, name='user'),
    url(r'^create_user/(?P<name>\w{1,50})/(?P<data>\w{1,50})$', views.insert_page, name='user'),
    url(r'^data/(?P<name>\w{1,50})$', csrf_exempt(views.post_page), name='user'),
    url(r'^post/', views.post),
    url(r'^add_client/', views.add_client),
    url(r'^update_client/', views.save_data),
    url(r'^client_details/(?P<client_key>\w{1,50})/$', views.client_details, name='user'),
    url(r'^client_details/(?P<client_key>\w{1,50})/time/(?P<time_test>\w{1,50})/$', views.client_details, name='user'),
]
