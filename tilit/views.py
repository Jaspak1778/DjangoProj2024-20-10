#tilit app - views.py
#E:\Koodi\DJANGO\drfsocialapp\main\tilit\views.py
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout
from django.views.decorators.cache import never_cache

@never_cache
def logout(request):
    auth_logout(request)  # Poistaa käyttäjän istunnon
    return render(request, 'loggedout.html')  # Ohjaa käyttäjän pääsivulle

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'tunnukset.html'
    success_url = reverse_lazy('home')


class login(LoginView):
    template_name = 'kirjaudu.html'
    redirect_authenticated_user = True


