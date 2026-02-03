from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # List view in admin
    list_display = ('email', 'username', 'country', 'get_groups')
    list_filter = ('groups', 'is_superuser', 'is_staff', 'is_active')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])
    get_groups.short_description = 'Groups'

    # Field layout in detail (edit) view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'username', 'first_name', 'middle_name', 'last_name', 'profile_image',
                'salutation', 'gender', 'phone', 'affiliation', 'country',
                'bio', 'is_author'
            )
        }),
        (_('Permissions'), {
            'fields': ('is_superuser','is_staff','is_active', 'groups', 'user_permissions')
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Field layout in add-user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'middle_name', 'last_name',
                'password1', 'password2', 'profile_image', 'is_author',
                'is_active', 'is_staff', 'is_superuser', 'groups'
            )
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
