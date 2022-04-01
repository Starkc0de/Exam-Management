from django.urls import path
from . import views

urlpatterns = [

    path('', views.MyUploadView.as_view(), name="myupload"),
    path('/delete-data/<int:id>', views.DeleteDataView.as_view(), name="deletedata")

]