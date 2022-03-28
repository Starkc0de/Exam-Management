from django.contrib import admin
from data_upload.models import Semester, Course , DataUpload 
# Register your models here.

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(DataUpload)