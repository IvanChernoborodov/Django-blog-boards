# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from posts.models import Post, Category

class PostAdmin(admin.ModelAdmin):
	list_display = [

					"__str__", 
					"content", 
					"date_of_creating"
					]

	list_display_links = [
						"__str__", 
						"date_of_creating"
						]

	list_filter = [
					"content", 
					"date_of_creating"
					]

	search_fields = [
					"__str__",
					"content"
					]

	prepopulated_fields = {
							'slug': ('title', )
							}
	class Meta:
		model = Post


class CategoryAdmin(admin.ModelAdmin):
	list_display = [
					"__str__",
					'name', 
					'slug'
					]

	prepopulated_fields = {
							'slug': ('name', )
							}
	class Meta:
		model = Category

admin.site.register(Post, 
					PostAdmin)
admin.site.register(Category,
					 CategoryAdmin)