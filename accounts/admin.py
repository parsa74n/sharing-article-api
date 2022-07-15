from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User


class CustomUserAdmin(UserAdmin):
    """
    custom admin for managing users.
    """

    form: UserChangeForm
    add_form: UserCreationForm

    model = User

    list_display = ['username', 'phone_number', 'email',
                    'is_active', 'staff', 'superuser', 'created', 'updated']
    list_filter = ['superuser','gender' ]

    fieldsets = (
        ('change user', {'fields': ['username','gender',
         'phone_number', 'email', 'password']}),
        ('permissions', {'fields': ['is_active', 'staff', 'superuser']})
    )

    add_fieldsets = (
        ('add user', {'fields': ['username', 'phone_number','gender'
         'email', 'password1', 'password2', 'staff', 'superuser']}),
    )

    search_fields = ['username', 'phone_number', 'email','gender']

    ordering = ['created', ]
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
