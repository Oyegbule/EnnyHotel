from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from room.models import Room
from django.utils import timezone

@login_required
def dashboard(request):
    # 1. Room Logic
    a_room = Room.objects.filter(is_available=True).count()
    o_room = Room.objects.filter(is_available=False).count()
    
    # 2. Shift Logic
    now = timezone.now()
    hour = now.hour

    if 6 <= hour < 14:
       shift = "Morning"
    elif 14 <= hour < 22:
       shift = "Afternoon"
    else:
       shift = "Night"
    
    # 3. Combine everything into context
    context = {
        'a_room': a_room,
        'o_room': o_room,
        'shift': shift
    }
    
    return render(request, 'dashboard/dashboard.html', context)