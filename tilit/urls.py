# tilit/urls.py
from django.urls import path
from .views import tunnukset, SignUpView, login

#kommentit
urlpatterns = [
    path('luotunnus/', SignUpView.as_view(), name="signup"),
    path('kirjaudu/', login.as_view(), name='kirjaudu'),
]