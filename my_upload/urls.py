from django.urls import path
from . import views

urlpatterns = [

    path('', views.MyUploadView.as_view(), name="DataUpload")

]