from django.conf.urls import patterns, include, url

from activitylog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^activities/new$', views.create_activity, name='create_activity'),
    url(r'^activities/(?P<activity_id>\d+)/$', views.view_activity, name='view_activity'),
)
