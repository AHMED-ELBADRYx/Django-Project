from django.db import models

# Create your models here.

class Product(models.Model):
    group = [
        ('Homes', 'Homes'),
        ('Toys', 'Toys'),
        ('Decoration', 'Decoration'),
        ('Clothes', 'Clothes'),
        ('Electronics', 'Electronics'),
        ('Books', 'Books'),
        ('Sports', 'Sports'),
        ('Beauty', 'Beauty'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Automotive', 'Automotive'),
        ('Garden', 'Garden'),
        ('Tools', 'Tools'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Office Supplies', 'Office Supplies'),
        ('Animals', 'Animals'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images/%y/%m/%d', verbose_name='photo')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices = group)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "matter"
        ordering = ["price"]

class Test(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    