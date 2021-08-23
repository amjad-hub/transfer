from transferApp.models import user_account
from django.contrib import admin
from .models import transfer
# Register your models here.

admin.site.register(user_account)
admin.site.register(transfer)

