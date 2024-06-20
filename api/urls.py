# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CustomerSignup.as_view(), name='customer-signup'),
    path('login/', views.CustomerLogin.as_view(), name='customer-login'),
    path('products/', views.GetProducts.as_view(), name='products'),
    path('orders/', views.OrderList.as_view(), name='order-list'),

]
