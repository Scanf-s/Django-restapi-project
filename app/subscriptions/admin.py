from django.contrib import admin
from subscriptions.models import Subscription
# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
