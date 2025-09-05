from django.contrib import admin
from app1.models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id', 'roll', 'name', 'city', 'email')

#admin.site.register(Profile, ProfileAdmin) decorator used place of it.

