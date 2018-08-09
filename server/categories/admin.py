from django.contrib import admin

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('created',)
    search_fields = ('name',)