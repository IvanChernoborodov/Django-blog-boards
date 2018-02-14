# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import User
from django.shortcuts import render
from .models import Board
from django.shortcuts import render, redirect, get_object_or_404
from boards.forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from boards.models import Board, Post, Topic
from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.views import listofposts

# GCBV
class BoardListView(ListView):
	model = Board
	context_object_name = 'boards'
	template_name = 'boards.html'


class TopicListView(ListView):
	model = Topic
	context_object_name = 'topics'
	template_name = 'topics.html'
	paginate_by = 10

	# board is the field in models.py
	def get_context_data(self, **kwargs):
		kwargs['board'] = self.board
		return super(TopicListView, self).get_context_data(**kwargs)

	def get_queryset(self):
		self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
		queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
		return queryset


@login_required
def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user = User.objects.first()  # TODO: get the currently logged in user
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
			message=form.cleaned_data.get('message'),
			topic=topic,
			created_by=user
			)
		return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'new_topic.html', {'board': board, 'form': form})


@login_required
def reply_topic(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()
			return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
	else:
		form = PostForm()
	return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

# def topic_posts(request, pk, topic_pk):
# 	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
# 	topic.views += 1
# 	topic.save()
# 	return render(request, 'topic_posts.html', {'topic': topic})

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'topic_posts.html'
	paginate_by = 2

	def get_context_data(self, **kwargs):
		self.topic.views += 1
		self.topic.save()
		kwargs['topic'] = self.topic
		return super(PostListView, self).get_context_data(**kwargs)

	# Here we define query to url
	def get_queryset(self):
		self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
		queryset = self.topic.posts.order_by('created_at')
		return queryset





@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
	model = Post
	fields = ('message', )
	template_name = 'edit_post.html'
	pk_url_kwarg = 'post_pk'
	context_object_name = 'post'

# With the line queryset = super().get_queryset() 
# we are reusing the get_queryset method from 
# the parent class, that is, the UpateView class.
# Then, we are adding an extra filter to the queryset,
# which is filtering the post using the logged in user,
# available inside the request object.

	def get_queryset(self):
		queryset = super(PostUpdateView, self).get_queryset()
		return queryset.filter(created_by=self.request.user)

	def form_valid(self, form):
		post = form.save(commit=False)
		post.updated_by = self.request.user
		post.updated_at = timezone.now()
		post.save()
		return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

