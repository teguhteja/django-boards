"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
# from django.conf.urls import url

from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # path(r'^$', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path(r'^about/company/$', views.about_company, name='about_company'),
    # path(r'^about/author/$', views.about_author, name='about_author'),
    # path(r'^about/author/vitor/$', views.about_vitor, name='about_vitor'),
    # path(r'^about/author/erica/$', views.about_erica, name='about_erica'),
    # path(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
    # path(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
]
