from django.contrib import admin
from .models import *

class PersonsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_approved', 'wallet')
    list_filter = ('username', 'email', 'is_approved')
    search_fields = ('username', 'email', 'upi')  # Search across these fields

class LatestCampAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'is_active', 'expire', 'is_format', '_time')
    list_filter = ('name', 'is_active', 'is_format')
    search_fields = ('name', 'camp_secret', 'expire', 'link', 'terms_cond')

class CampHistoryAdmin(admin.ModelAdmin):
    list_display = ('_campID', 'email', 'name', 'is_verified', 'amount', 'date')
    list_filter = ('email', 'is_verified')
    search_fields = ('_campID', 'email', 'name', 'link')



'''class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date_time', 'is_verified', 'is_cancel','email')
    list_filter = ('is_verified', 'is_cancel')
    search_fields = ('amount','email')
    '''

class WithdrawHistoryAdmin(admin.ModelAdmin):
    list_display = ('email','amount', 'date_time', 'is_verified', 'is_cancel')
    list_filter = ('is_verified', 'is_cancel')
    search_fields = ('amount','email')

admin.site.register(Persons, PersonsAdmin)
admin.site.register(LatestCamp, LatestCampAdmin)
admin.site.register(CampHistory, CampHistoryAdmin)
admin.site.register(Withdraw_history, WithdrawHistoryAdmin)

admin.site.register(Notice)