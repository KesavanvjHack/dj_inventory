from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'age','role','is_staff', 'is_active','date_joined', 'last_login')
    search_fields = ('id','username', 'email', 'first_name', 'last_name','role')
    ordering = ['id']

admin.site.register(User, UserAdmin)


# Register your models here.
