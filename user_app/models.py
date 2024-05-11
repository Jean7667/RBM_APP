from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    location = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    is_customer = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class Skill(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    level = models.SmallIntegerField()  
    def __str__(self):
        return self.name

class Expert(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='expert')
    skills = models.ManyToManyField(Skill, related_name='experts')
    start_date = models.DateField(null=True)

class Booking(models.Model):
    id= models.AutoField(primary_key=True)
    BookingExpert = models.ForeignKey(CustomUser, related_name='expert_bookings', on_delete=models.CASCADE)
    CustomerUser = models.ForeignKey(CustomUser, related_name='customer_bookings', on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
  ##  Refering the model,