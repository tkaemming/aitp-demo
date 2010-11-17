from django.contrib import admin
from aitp.blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_at'
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'author', 'content'),
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
    list_display = ('title', 'author', 'posted_at')
    prepopulated_fields = {
        'slug': ('title',)
    }

admin.site.register(Post, PostAdmin)