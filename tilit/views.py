#tilit app - views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def tunnukset(request):
    return render (request, 'tunnukset.html')


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'tunnukset.html'
    success_url = reverse_lazy('home')