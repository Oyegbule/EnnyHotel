from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *

@login_required
def add_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AddCategoryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category added to manage rooms')
            return redirect('add-category')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('add-category')
    else:
        form = AddCategoryform()
        context = {'form':form, 'categories':categories}
    return render(request, 'room/add_category.html', context)    
    
def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCategoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category informations is updated and saved')
            return redirect(reverse('add-category'))
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect(reverse('update-category',args=[category.pk]))
    else:
        form = UpdateCategoryform(instance=category)
        context = {'form':form}
    return render(request, 'room/update_category.html', context)

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.success(request, 'Category is now deleted')
    return redirect('add-category')

def add_room(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New room information added and saved')
            return redirect('add-room')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('add-room')
    else:
        form = AddRoomForm()
        context = {'form':form, 'rooms':rooms}
    return render(request, 'room/add_room.html', context)

def update_room(request, pk):
    room = Room.objects.get(pk=pk)
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = UpdateRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form info is updated and saved')
            return redirect(reverse('add-room'))
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect(reverse('update-room',args=[room.pk]))
    else:
        form = UpdateRoomForm(instance=room)
        context = {'form':form, 'room':room, 'rooms':rooms}
    return render(request, 'room/update_room.html', context)

def all_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'room/all_rooms.html', context)

def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    messages.success(request, 'Room has been deleted')
    return redirect('add-room')

def new_booking(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewBookingForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.room = room
            room.is_available = False
            var.save()
            room.save()
            messages.success(request, 'New Booking has been made')
            return redirect('all-rooms')
        else:
            messages.warning(request, 'Something went wrong. Please check')
            return redirect(reverse('new-booking', args=[room.pk]))
    else:
        form = NewBookingForm()
        context = {'form':form, 'room':room}
    return render(request, 'room/new_booking.html', context)

def update_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
           form.save()
           messages.success(request, 'Booking info has been updated and saved')
           return redirect(reverse('update-booking', args=[booking.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please check')
            return redirect(reverse('update-booking', args=[booking.pk]))
    else:
        form = UpdateBookingForm(instance=booking)
        context = {'form':form, 'booking':booking}
    return render(request, 'room/update_booking.html', context)

def checkout_guest(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.checked_out = True

    # get linked room
    room = Room.objects.get(pk=booking.room.pk)
    room.is_available = True
    room.save()
    booking.save()
    messages.success(request, 'Guest has been checked out and room is now available for use.')
    return redirect('dashboard')

def guest_history_per_room(request, pk):
    room = Room.objects.get(pk=pk)
    guests = room.booking_set.all().order_by('checked_out')
    context = {'guests':guests}
    return render(request, 'room/guest_history_per_room.html', context)

def all_active_guests(request):
    guests = Booking.objects.filter(checked_out=False)
    context = {'guests':guests}
    return render(request, 'room/all_active_guests.html', context)

def active_guests_per_room(request, pk):
    room = Room.objects.get(pk=pk)
    guests = room.booking_set.all()
    context = {'guests':guests}
    return render(request, 'room/active_guests_per_room.html', context)