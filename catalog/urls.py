from django.urls import path
from catalog import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts')
]