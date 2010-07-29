from django.contrib import admin
from garrettbjerkhoel.posts.models import Work

class WorkAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    # list_display = ('__unicode__', 'slug', 'created_at', 'updated_at')
    # prepopulated_fields = {"slug": ("title",)}
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'user', 'body',)
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('slug',)
    #     }),
    # )

admin.site.register(Work, WorkAdmin)
