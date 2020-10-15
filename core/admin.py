from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext as _
from core import models

class UserAdmin(BaseUserAdmin):
    ordering=['id']
    list_display=['email','name']
    fieldsets = (
            (
                None,
                {'fields': ('email','name')}
            ),
            (
                _('Permissions'),
                {'fields':('is_active','is_staff')}
            ),
            (
                _('Last login or last seen dates'),
                  {'fields':('last_login',)}
            )
        )
    add_fieldsets = (
            (None,
            {
                'classes': {'wide'},
                'fields': ('email','password1', 'password2')
            }),

        )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)