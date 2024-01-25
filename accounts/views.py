
# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Author
from pinterest.models import Post
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    context_object_name = 'signup'



