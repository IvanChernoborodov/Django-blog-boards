# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)	

class Category(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(max_length=200, unique=True	)

	class Meta:
		ordering = ['name']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('posts:category', args=[str(self.slug)]) 


class Post(models.Model):
	title = models.CharField(max_length = 100) 
	content = models.TextField(
		max_length = 600, default = 'cool' 
		)
	date_of_creating = models.DateTimeField(
		auto_now=False, auto_now_add=True
		)
	image = models.ImageField(
		upload_to=upload_location,
		null=True, 
		blank=True, 
		height_field="height_field", 
		width_field="width_field"
		)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0) 
	category = models.ForeignKey('Category')
	slug = models.SlugField(unique=True, blank=False)

	class Meta:
		ordering = ['title']
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		index_together = [
		['id', 'slug']
		]	 


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('posts:detail',
						 args=[str(self.slug)]
						 ) 
		# Или так например
		# kwargs={'slug': self.slug})









