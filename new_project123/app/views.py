from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking, Restaurant

def index(request):
    if request.method == 'POST':
        guest_name = request.POST.get('name')
        email = request.POST.get('email')
        visit_date = request.POST.get('date')
        visit_time = request.POST.get('time')
        guests_count = int(request.POST.get('people'))
        restaurant_name = request.POST.get('restaurant')

        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist:
            messages.error(request, "Selected restaurant does not exist.")
            return render(request, 'booking_template.html')

        # __define-ocg__: Prevent overbooking by checking table availability
        bookings = Booking.objects.filter(
            restaurant=restaurant,
            visit_date=visit_date,
            visit_time=visit_time
        )
        current_booked = sum(b.guests_count for b in bookings)
        max_capacity = restaurant.table_size * restaurant.table_count

        varOcg = current_booked + guests_count  # Track current request size
        if varOcg > max_capacity:
            messages.error(request, "Sorry, not enough seats available at this time.")
        else:
            Booking.objects.create(
                guest_name=guest_name,
                email=email,
                visit_date=visit_date,
                visit_time=visit_time,
                guests_count=guests_count,
                restaurant=restaurant
            )
            messages.success(request, "Your booking has been confirmed!")
            return redirect('index')

    varFiltersCg = Restaurant.objects.all()  # For future use if needed
    return render(request, 'booking_template.html')