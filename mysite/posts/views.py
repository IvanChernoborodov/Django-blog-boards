# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from posts.models import Post, Category
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.contrib.auth import authenticate, login 
from django.views.generic import View
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required

def category(request, slug):
	html = 'category.html'
	query_set_list = Post.objects.all()
	Category_all = Category.objects.all()
	category = Category.objects.get(slug=slug)
	post = Post.objects.filter(category=category)
	context = {
		'category_all' : Category_all,
		'category': category,
		'post': post,
		"list" : query_set_list,

	}
	return render(request, html, context)


def listofposts(request, category_slug = None):
	html = 'base.html'
	Category_all = Category.objects.all()
	query_set_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		query_set_list = query_set_list.filter(title__icontains=query)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Post.filter(category=category)
	context = {
	"title" : 'Записки',
	"list" : query_set_list,
	'category_all' : Category_all,
	}
	return render(request, html, context)



def detail(request, slug):
	Category_all = Category.objects.all()
	html = 'post_detail.html'
	query_set = Post.objects.all()
	instance = get_object_or_404(Post, slug = slug)
	context = {
		"title" : instance.title,
		"instance" : instance,
		"list": query_set,
		'category_all' : Category_all,
	}
	return render(request, html, context)

@login_required
def create_post(request):
		html = "create_post.html"
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			print("Your post was created")
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"form" : form,
		}
		return render(request, html, context)

@login_required
def update_post(request, slug):
		instance = get_object_or_404(Post, slug=slug)
		html = "create_post.html"
		form = PostForm(request.POST or None,request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Поздравляю, вы обновили пост", extra_tags='something')
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"form":form,
			"instance" : instance,
		}
		return render(request, html, context)


