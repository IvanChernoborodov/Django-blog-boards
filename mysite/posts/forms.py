# -*- coding: utf-8 -*-
from django import forms
from posts.models import Post , Category
from pagedown.widgets import PagedownWidget
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	content = forms.CharField(widget= PagedownWidget(show_preview=False))
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['content'].widget.attrs.update({'class': 'XXXXX'})
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			'category',
			'slug',
			]
