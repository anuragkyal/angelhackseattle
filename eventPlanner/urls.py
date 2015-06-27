from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from plans import views

router = routers.DefaultRouter()
router.register(r'plans', views.PlanViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventPlanner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
