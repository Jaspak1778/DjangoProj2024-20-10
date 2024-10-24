#main app - views.py
#E:\Koodi\DJANGO\drfsocialapp\main\main\views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def home(request):
    print(f"User: {request.user.username}, Authenticated: {request.user.is_authenticated}")
    return render(request, 'index.html')
