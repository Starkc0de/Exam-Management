from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Now register the new UserModelAdmin...

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'mobile_number', 'address', 'terms_conditions', 'is_admin')
    
admin.site.register(User,UserModelAdmin)

