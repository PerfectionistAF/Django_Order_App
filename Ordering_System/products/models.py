from django.db import models

# Create your models here.
##Each order can have multiple products, 
##each product can be ordered by multiple orders; MANY TO MANY
##use intermediatary table

from core_users.models import User, Company
##CRUD: here we use migrate to create
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True) ##immutable field
    last_updated_at = models.DateTimeField(auto_now=True) ##mutable field
    is_active = models.BooleanField(default=True)

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('success', 'success'),
        ('failed', 'failed'),
    )
    id = models.AutoField(primary_key=True)  ###Amend to 1:1 relation, no need for OrderItem
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.PositiveIntegerField(null = True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.PositiveIntegerField()
