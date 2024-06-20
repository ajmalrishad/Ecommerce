# customers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path("list/", views.customers_list, name="customer_list"),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:pk>/edit/', views.edit_customer, name='edit_customer'),
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    #Products Urls 
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    # Other URLs for customer-related views
]
