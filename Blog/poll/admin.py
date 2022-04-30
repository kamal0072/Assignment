from django.contrib import admin
from .models import BlogPost
# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['id','author','title','body','created_at','updated_at']
    

