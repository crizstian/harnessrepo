from django.db import models

# Create your models here.

from django.db import models



class RequestEntry(models.Model):
    name= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)