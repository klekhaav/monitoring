from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_email', 'title', 'address', 'protocol')
    list_filter = ('id', 'title', 'user_email', 'title', 'address', 'protocol')
    fieldsets = (
        ("User", {'fields': ('user_email',)}),
        ('Server info', {'classes': ('collapse',),
                         'fields': ('title', 'address', 'protocol')}),
    )

    search_fields = ('id', 'user_email', 'title', 'address', 'protocol')
    ordering = ('user_email',)
    empty_value_display = '-empty-'


admin.site.register(Server, ServerAdmin)
