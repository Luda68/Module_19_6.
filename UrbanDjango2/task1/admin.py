from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Buyer, Game

# Register your models here.
# admin.site.register(Buyer)
# admin.site.register(Game)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_filter = ('name', 'balance')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')
    search_fields = ('title',)
    list_filter = ('title', 'cost')
    fields = [('title', 'size', 'cost'), 'description', 'age_limited', 'buyer']