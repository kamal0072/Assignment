from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
class BlogpostList(ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    pagination_class=PageNumberPagination   

class BlogPostRUD(RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    pagination_class=PageNumberPagination   
