from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)  ###Interface Segregation Principle
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name)   #self.id, self.name

##inherits from Abstract User, One to One
class User(AbstractUser):
    ROLE_CHOICES = (
        ('operator', 'operator'),
        ('viewer', 'viewer'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        if self.pk is None and self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)