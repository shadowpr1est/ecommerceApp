from django.shortcuts import render
from django.urls import path, include
from ecommerce.views import profile, registration
from . import views



urlpatterns = [
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/registration/', registration, name='registration'),
    path('', views.products_list, name="home"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('search/', views.product_search, name="product_search"),
    path('vacancy/', views.leave_request, name='leave_request'),
    path('product/<int:pk>/reviews/new/', views.review_edit, name='review_create'),
    path('product/<int:pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('success/', lambda request: render(request, 'ecommerce/success.html'), name='success'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
]

