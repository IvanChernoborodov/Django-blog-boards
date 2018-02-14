from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from accounts.views import signup # import views as accounts_views
from accounts import views as accounts_views
from boards.views import (
	# board,
	# board_topics,
	# topic_posts,
	new_topic,
	reply_topic,
	)
from boards import views


urlpatterns = [
	url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),	
	url(r'^boards/$', views.BoardListView.as_view(), name='board'),
    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),

	url(r'^login/$',
		 auth_views.login, 
		 name='login'),
	url(r'^logout/$',
		 auth_views.logout,
		 name='logout'),
	url(r'^admin/', 
			admin.site.urls),
	url(r'^signup/$', 
		signup, 
		name='signup'), # or from accounts import views  as accounts_views and in url add accounts_views.signup , signup is name of out view

	url(r'^', include('posts.urls', namespace='posts')),
	# url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
	
	# url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
	# 	views.PostUpdateView.as_view(), 
	# 	name='edit_post'
	# 	),

	# url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', 
	# 	reply_topic,
	# 	name='reply_topic'
	# 	),

	# url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', 
	# 	views.PostListView.as_view(), 
	# 	name='topic_posts'
	# 	),

	# url(r'^boards/(?P<pk>\d+)/new/$',
	# 	new_topic, 
	# 	name='new_topic'
	# 	),

	# # for GCBV
	# url(r'^boards/(?P<pk>\d+)/$', 
	# 	views.TopicListView.as_view(), 
	# 	name='board_topics'
	# 	),



 #    url(r'^boards/$',
	# 	 views.BoardListView.as_view(), 
	# 	 name='board'),


	


	# url(r'^login/$',
	# 	 auth_views.login, 
	# 	 name='login'),
	# url(r'^logout/$',
	# 	 auth_views.logout,
	# 	 name='logout'),
	# url(r'^admin/', 
	# 		admin.site.urls),
	# url(r'^signup/$', 
	# 	signup, 
	# 	name='signup'), # or from accounts import views  as accounts_views and in url add accounts_views.signup , signup is name of out view
	# url(r'^', include('posts.urls', namespace='posts')),
 #    url(r'^api/v0/', include('api_v0.urls', namespace='api_v0')),
 #    url(r'^api/', include(router.urls)),
 #    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 







	











    