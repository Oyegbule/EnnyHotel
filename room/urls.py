from django.urls import path
from .views import *

urlpatterns = [
    path('add-category/', add_category, name='add-category'),
    path('update-category/<int:pk>/', update_category, name='update-category'),
    path('delete-category/<int:pk>/', delete_category, name='delete-category'),

    path('add-room/', add_room, name='add-room'),
    path('update-room/<int:pk>/', update_room, name='update-room'),
    path('all-rooms/', all_rooms, name='all-rooms'),
    path('delete-room/<int:pk>/', delete_room, name='delete-room'),

    path('new-booking/<int:pk>/', new_booking, name='new-booking'),
    path('update-booking/<int:pk>/', update_booking, name='update-booking'),

    path('checkout-guest/<int:pk>/', checkout_guest, name='checkout-guest'),

    path('guest-history-per-room/<int:pk>/', guest_history_per_room, name='guest-history-per-room'),
    path('all-active-guests', all_active_guests, name='all-active-guests'),
    path('active-guests-per-room/<int:pk>/', active_guests_per_room, name='active-guests-per-room')
]