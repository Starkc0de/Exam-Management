from django.contrib import admin
from .models import User,Role

# Now register the new UserModelAdmin...

admin.site.register(User)
admin.site.register(Role)
