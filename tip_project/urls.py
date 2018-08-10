"""tip_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # k - notice that both blog.urls and pages.urls configured '' path, while both of them use different view classes, only blog.blogListView load model object. 
    # k - django will search urls from top to bottom, so if blog.urls moved beneath pages.url, it would lead to pages.homepageview; in other words, blog.bloglistview won't load.
    path('',include('blog.urls')),
    path('',include('pages.urls')),
    path('posts',include('posts.urls')),
    
]
