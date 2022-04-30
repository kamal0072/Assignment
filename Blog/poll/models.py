from django.db import models
from django.contrib.auth.models import User 
# # Create your models here.
class BlogPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField()
    body=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    
    def __str__(self):
        return self.author