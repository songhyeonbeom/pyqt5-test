from django.contrib import admin
from .models import CartItem

# Register your models here.
@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = [
        'user',
        'photo',
        'quantity',
        'created_at',
    ]
