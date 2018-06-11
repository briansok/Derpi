"""derpi URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authtoken
import api
from sensors import views as sensor_views
from notifications import views as notification_views
from . import views as derpi_views
from . import models as derpi_models

urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('widgets.urls')),
    url(r'^widgets/', include('widgets.urls')),
    url(r'^$', auth_views.login, name='login'),
    url(r'^sensors/', include('sensors.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^controllers/', include('controllers.urls')),
    url(r'^notifications/', notification_views.index),
    url(r'^notifications/(?P<pk>[0-9]+)/$', notification_views.details),
    url(r'^account/', derpi_views.details),

    # API
    url(r'^api/auth', authtoken.obtain_auth_token),
    url(r'^api/categories/$', api.CategoryList.as_view()),
    url(r'^api/categories/(?P<pk>[0-9]+)/$', api.CategoryDetail.as_view()),
    url(r'^api/categories/(?P<pk>[0-9]+)/sensors/$', api.CategorySensors.as_view()),
    url(r'^api/sensors/$', api.SensorList.as_view()),
    url(r'^api/sensors/(?P<pk>[0-9]+)/$', api.SensorDetail.as_view()),
    url(r'^api/controllers/$', api.ControllerList.as_view()),
    url(r'^api/controllers/(?P<pk>[0-9]+)/$', api.ControllerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
