from django.contrib import admin
from .models import User,User_Cart,User_Order

# Register your models here.
admin.site.register(User)
admin.site.register(User_Cart)
admin.site.register(User_Order)
