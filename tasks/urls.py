from django.conf.urls import patterns, include, url
from tasks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
)
