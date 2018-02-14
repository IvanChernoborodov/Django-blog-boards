# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login 
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
	model = User
	template_name = 'my_account.html'
	fields = ('first_name', 'last_name', 'email', 'bio', 'location', 'birth_date', 'avatar', )
	success_url = reverse_lazy('my_account')

	def get_object(self):
		return self.request.user


def signup(request):
	html = 'signup.html'
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	context = {
		'form': form,
	}
	return render(request, html, context)











