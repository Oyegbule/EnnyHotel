from django import forms
from .models import *

class AddCategoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'amount']

class UpdateCategoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'amount']

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'name']

class UpdateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'name']

class NewBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('room', 'timestamp')

class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('room', 'timestamp')