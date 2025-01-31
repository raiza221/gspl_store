from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/list/', views.product_list, name='product-list-view'),
    path('login/', views.login_view, name='login'),
]
