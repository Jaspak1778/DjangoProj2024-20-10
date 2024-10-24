# tilit/urls.py
from django.urls import path
from .views import tunnukset, SignUpView

#kommentit
urlpatterns = [
    path('luotunnus/', SignUpView.as_view(), name="signup"),
]