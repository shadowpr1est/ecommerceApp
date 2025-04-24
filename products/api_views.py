from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from django.shortcuts import get_object_or_404

from .models import Product, Category, Comment
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer, VacancySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get', 'post'])
    def reviews(self, request, pk=None):
        product = self.get_object()

        if request.method == 'GET':
            comments = product.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(
                    product=product,
                    user_name=request.user.username,
                    user_id=request.user.id,
                    created_date=now()
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class VacancyViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"status": "vacancy submitted"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
