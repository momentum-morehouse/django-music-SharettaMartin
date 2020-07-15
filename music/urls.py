"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from mytunes import views as mytunes_views
#This last line is helping the files communicate

#First line  urlpatterns given..
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mytunes', mytunes_views.list_albums, name='home'),
    # path('album/add/', mytunes_views.add_albums,name='add_albums')
]

if settings.DEBUG:
    import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),

    #     # For django versions before 2.0:
    #     # url(r'^__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns
