from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserFollower

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    list_display = ['username', 'email', 'is_staff', 'is_active']

admin.site.register(UserFollower)
.
