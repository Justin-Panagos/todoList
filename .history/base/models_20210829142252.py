from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    
    STATUS= [(0,'P1'),(1,'P2'),(2,'P3'),]
    priority = models.CharField(max_length=5, choices=STATUS,default=0,)
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duedate = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create =models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    class Meta:
        ordering =['complete']