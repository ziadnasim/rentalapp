from django.contrib import admin
from .models import Profile
# Register your models here.

admin.site.site_title = 'Home Rental App Login'
admin.site.site_header = 'Rental App'

admin.site.register(Profile)
