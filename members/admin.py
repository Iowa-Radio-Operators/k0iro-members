from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'call_sign', 'membership_expires', 'is_active', 'dues_paid')
    list_filter = ('is_active', 'membership_expires', 'dues_paid')
    search_fields = ('first_name', 'last_name', 'email', 'call_sign')
