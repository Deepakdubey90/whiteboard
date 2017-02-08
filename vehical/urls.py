# encoding=utf-8
"""demo URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import VehicalList, VehicalDetail, CreateVehicalView
admin.autodiscover()


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'vehicals', VehicalList.as_view(), base_name="vehical")
router.register(r'vehicals/(?P<pk>[0-9]+)', VehicalDetail.as_view(), base_name="vehical")
api_patterns = router.urls

urlpatterns = i18n_patterns(
        url(r'^admin/', admin.site.urls),
        url(r'^$', TemplateView.as_view(template_name="vehical_list.html")),
        url(r'^create/vehical/$', CreateVehicalView),
        url(r'^update/vehical/(?P<pk>[0-9]+)/$', TemplateView.as_view(template_name="update_vehical.html")),
        url(r'^vehicals/$', VehicalList.as_view()),
        url(r'^vehicals/(?P<pk>[0-9]+)/$', VehicalDetail.as_view()),
        url(r'^i18n/', include('django.conf.urls.i18n')),    
    )
    
    
urlpatterns += [
    url(r'api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#urlpatterns = urlpatterns + i18n_patterns
#urlpatterns += staticfiles_urlpatterns()
