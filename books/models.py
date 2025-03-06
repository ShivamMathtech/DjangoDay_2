from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=1000)
    author=models.CharField(max_length=100)
    price =models.FloatField()
    description = models.TextField(blank=True, null=True)
    publish_date=models.DateField()

    def __str__(self):
        return self.title
        

class NewBook(models.Model):
    title=models.CharField(max_length=1000)
    author=models.CharField(max_length=100)
    price =models.FloatField()
    description = models.TextField(blank=True, null=True)
    publish_date=models.DateField()

    def __str__(self):
        return self.title
