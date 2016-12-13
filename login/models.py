from django.db import models
from django import forms
from django.utils.timezone import now

# Create your models here.
class puser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(default=None)
    mobile = models.CharField(max_length=12)
    # file = forms.FileField()
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    resume = models.ImageField(upload_to = 'resume/', default = 'resume/None/no-img.jpg')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # email = models.CharField(max_length=30)
    # resume = models.CharField(max_length=50)

    def __str__(self):
        return self.name