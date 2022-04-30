from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id','author','title','body','created_at','updated_at']