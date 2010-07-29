from django.contrib import admin
from garrettbjerkhoel.posts.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('__unicode__', 'slug', 'created_at', 'updated_at')
    # list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'user', 'body', 'categories',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('__unicode__', 'slug', 'created_at', 'updated_at')
    # list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
