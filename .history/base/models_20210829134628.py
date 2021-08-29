from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duedate = models.DateTimeField(null=True, blank=True, auto_now_add=False)
    level = ((p1,'low'),(P2,'med'), (P3,'high'))
    complete = models.BooleanField(default=False)
    create =models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
     
    class Meta:
        ordering =['complete']