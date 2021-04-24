from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput

# Register your models here.


class UserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    search_fields = ('email', 'user_name', 'first_name')
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        NewUser.About: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
