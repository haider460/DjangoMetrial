from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import NewUser
from django.utils.translation import ugettext_lazy as _
from django.forms import Textarea, TextInput


class MyuserAdmin(UserAdmin):
    model = NewUser
    list_display = ('username', 'email',
                    'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'phonenumber')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    formfield_overrides = {
        NewUser.phonenumber: {'widget': TextInput()},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phonenumber', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',  'email')

    ordering = ('username',)


admin.site.register(NewUser, MyuserAdmin)
