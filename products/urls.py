from django.shortcuts import render
from django.urls import path
from . import views



urlpatterns = [
    path('', views.products_list, name="home"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('search/', views.product_search, name="product_search"),
    path('vacancy/', views.leave_request, name='leave_request'),
    path('product/<int:pk>/reviews/new/', views.review_edit, name='review_create'),
    path('product/<int:pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('success/', lambda request: render(request, 'ecommerce/success.html'), name='success'),
]

