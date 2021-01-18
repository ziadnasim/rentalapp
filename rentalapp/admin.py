from django.contrib import admin
from .models import Profile, House, Address, Properties, HouseProperties, Review, Wishlist, Auth

# Register your models here.

admin.site.site_title = 'Home Rental App Login'
admin.site.site_header = 'Rental App'

admin.site.register(Profile)
admin.site.register(House)
admin.site.register(Address)
admin.site.register(Properties)
admin.site.register(HouseProperties)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Auth)