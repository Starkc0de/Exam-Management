from django.urls import path
from . import views

urlpatterns = [

    path('', views.MyUploadView.as_view(), name="DataUpload"),
    path('delete-data/<int:id>/', views.DeleteDataView.as_view(), name="DeleteData")

]