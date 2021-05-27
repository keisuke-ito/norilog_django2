from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Noriori

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Noriori)