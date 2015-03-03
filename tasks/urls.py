from django.conf.urls import patterns, include, url
from tasks import views

urlpatterns = patterns('',
	url(r'^$',views.HomeView.as_view(), name='home'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
	url(r'^tasks/$', views.IndexView.as_view(), name='index'),
)
