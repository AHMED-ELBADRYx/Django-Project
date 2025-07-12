from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class Female(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "female"
        ordering = ["name"]

class Male(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    relationship = models.OneToOneField(Female, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "male"
        ordering = ["name"]
    
class Product(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)
    watch = models.ManyToManyField(Video)

    def __str__(self):
        return self.name
    
class Login(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
