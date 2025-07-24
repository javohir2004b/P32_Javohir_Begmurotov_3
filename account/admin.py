from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin

from account.models import CustomerUser, Profile

class ProfileAdmin(TabularInline ):
    model =Profile


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    inlines = [ProfileAdmin , ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info",{"fields": ("phone",)}),
    )
