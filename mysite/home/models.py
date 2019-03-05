from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image', default=None, blank=True, null=True)
