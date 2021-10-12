from django.contrib import admin
from .models import UserProfile


# Admin display for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_first_name',
        'default_last_name',
    )

    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
