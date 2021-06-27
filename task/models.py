from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Navchang(models.Model):
    text=models.CharField(max_length=100)
    link=models.URLField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Bannerchange(models.Model):
     photo = models.ImageField( upload_to='photos/%Y/%m/%d')
     created_date = models.DateTimeField(auto_now_add=True)


class Albumzone(models.Model):
    img = models.ImageField( upload_to='photos/%Y/%m/%d')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



