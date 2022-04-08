from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.TextField()
    brand = models.CharField(max_length=150)
    size = models.IntegerField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField()

    def __str__(self):
        return self.name

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)
COUNTRY_CHOICES = (
    ('vietNam','Việt Nam'),
    ('unitedStates', 'United States'),
    ('russia','russia'),
)
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default = 'female')
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='vietNam')

    def __str__(self):
        return self.user.username
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
