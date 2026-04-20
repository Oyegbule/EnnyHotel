from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_names = models.CharField(max_length=100)
    guest_email = models.EmailField(max_length=100)
    guest_phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False)