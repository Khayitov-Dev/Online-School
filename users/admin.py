from django.contrib import admin
from .models import UserProfileInfo
# Register your models here.
# admin.site.register(UserProfileInfo)


@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['bio','profile_pic','user_type']
    list_filter = ['bio','user_type']
    search_fields = ['bio','user_type']
