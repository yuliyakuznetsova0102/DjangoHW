from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
]