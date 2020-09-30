from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

RobowizardEmployee = get_user_model()


class RobowizardEmployeeAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['username', 'email', 'first_name', 'last_name', 'mid_name', 'position', 'birthday']
    fieldsets = (
        (None,
         {'fields': ('username', 'first_name', 'last_name', 'mid_name', 'email', 'position', 'birthday')}),
        ('Статус админа', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'mid_name', 'email', 'position',
                       'birthday', 'is_staff')}
         ),
    )


admin.site.register(RobowizardEmployee, RobowizardEmployeeAdmin)
