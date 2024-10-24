#main app - urls.py
#E:\Koodi\DJANGO\drfsocialapp\main\main\urls.py

from .views import home
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tunnukset/', include('tilit.urls')),

]

