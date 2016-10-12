from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import CustomerChangeForm, CustomerCreationForm
from .models import Customer


class CustomerAdmin(BaseUserAdmin):
    form = CustomerChangeForm
    add_form = CustomerCreationForm

    list_display = ('id', 'email', 'first_name', 'last_name', 'is_admin', 'is_active', 'join_date')
    list_filter = ('is_admin', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'join_date')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Extra info', {'classes': ('collapse',),
                        'fields': ('first_name', 'last_name',)}),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    empty_value_display = '-empty-'
    readonly_fields = ('id',)
    filter_horizontal = ()


admin.site.register(Customer, CustomerAdmin)

admin.site.unregister(Group)