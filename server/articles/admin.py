from django.contrib import admin

from django.template.loader import render_to_string

from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'category', 'created')

    list_filter = ('category', 'created')

    search_fields = ('name', 'content')

    fieldsets = (
        (None, {
            "fields": ('name', 'category')
        }),
        ('Content', {
            "fields": ('image', 'content')
        }),
    )
    
    
    def picture(self, obj):
        return render_to_string('articles/blocks/image.htm', {'image': obj.image})