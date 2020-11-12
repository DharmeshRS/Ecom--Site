from django.contrib import admin

# Register your models here.
from .models import AddCatagoryModel,AddProductModell

admin.site.register(AddCatagoryModel)
admin.site.register(AddProductModell)
