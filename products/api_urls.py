from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'products', api_views.ProductViewSet, basename='product')
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'comments', api_views.CommentViewSet)
router.register(r'vacancy', api_views.VacancyViewSet, basename='vacancy')

urlpatterns = [
    path('', include(router.urls)),
]
