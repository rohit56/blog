from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug'),
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug'),
    list_display = ('title', 'category', 'status', 'created', 'updated',)
    list_filter = ('status',)
    search_fields = ('title', 'body',)

admin.site.register(Post, PostAdmin)