from django.contrib import admin
from .models import *
# Register your models here.
#here am registering models to appear in the admin panel
admin.site.register(Stock_Category)
admin.site.register(Product)