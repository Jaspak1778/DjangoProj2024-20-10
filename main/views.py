#main app - views.py

from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect(reverse('kirjaudu'))