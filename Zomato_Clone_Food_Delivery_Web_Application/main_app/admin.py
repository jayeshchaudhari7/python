from django.contrib import admin
from .models import Restaurant, MenuItem, Cart, Order, Review

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)
    search_fields = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity')
    list_filter = ('user',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'ordered_at')
    list_filter = ('ordered_at', 'user')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'rating', 'created_at')
    list_filter = ('restaurant', 'rating')
    search_fields = ('user__username', 'restaurant__name')
