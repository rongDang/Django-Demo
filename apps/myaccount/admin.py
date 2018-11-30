from django.contrib import admin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfile_Admin(admin.ModelAdmin):
    list_display = ('user', 'org', 'telephone', 'mod_date')
