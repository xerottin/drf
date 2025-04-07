from django.db import models

# Create your models here.

class Women(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title