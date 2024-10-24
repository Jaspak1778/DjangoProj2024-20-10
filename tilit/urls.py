# tilit/urls.py
#E:\Koodi\DJANGO\drfsocialapp\main\tilit\urls.py

from django.urls import path
from .views import SignUpView, login, logout

#kommentit
urlpatterns = [
    path('luotunnus/', SignUpView.as_view(), name="signup"),
    path('kirjaudu/', login.as_view(), name='kirjaudu'),
    path('loggedout/', logout, name='loggedout'),  # Uloskirjautuminen
]