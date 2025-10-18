from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('telefon_raqam', 'first_name', 'last_name', 'viloyat', 'is_staff', 'is_superuser')
    search_fields = ('telefon_raqam', 'first_name', 'last_name')
    ordering = ('telefon_raqam',)

    fieldsets = (
        (None, {'fields': ('telefon_raqam', 'password')}),
        ('Shaxsiy ma\'lumotlar', {'fields': ('first_name', 'last_name', 'otasining_ismi', 'mutaxassisligi')}),
        ('Qo‘shimcha ma\'lumotlar', {'fields': ('viloyat', 'tuman', 'maktab_raqami', 'sinf', 'fan')}),
        ('Ruxsatlar', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tizim ma\'lumotlari', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telefon_raqam', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
