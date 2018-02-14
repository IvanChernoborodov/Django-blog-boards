# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from posts.views import (
	listofposts,
	create_post,
	detail,
	update_post,
	category,
	)

urlpatterns = [
	url(r'^create/', 
		create_post ,
		name='create_post'),
	url(r'^category/(?P<slug>[-\w]+)/$',
		category,
		name='category'),
	url(r'^(?P<slug>[-\w]+)/edit/$',
		update_post,
		name = 'update_post'),
	url(r'^(?P<slug>[-\w]+)/$',
		detail,
		name = 'detail'),
	url(r'^$',
		listofposts ,
		name='listofposts'),
]


