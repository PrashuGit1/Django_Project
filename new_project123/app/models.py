from django.db import models

# __define-ocg__: Defining restaurant and booking structure

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    table_size = models.IntegerField()
    table_count = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.zone}) - Table Size: {self.table_size}"


class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    visit_date = models.DateField()
    visit_time = models.TimeField()
    guests_count = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.guest_name} at {self.restaurant.name}"