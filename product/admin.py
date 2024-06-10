from django.contrib import admin
from .models import products
# Register your models here.
@admin.register(products)
class adminProd(admin.ModelAdmin):
    list_display = ['title', 'image',]
