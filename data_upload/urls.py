from django.urls import path
from . import views

urlpatterns = [

    path('', views.DataUploadView.as_view(), name="dataupload"),
    path('/update-data/<int:id>', views.EditDataView.as_view(), name="data-update"),

]