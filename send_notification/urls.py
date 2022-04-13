from django.urls import path
from . import views

urlpatterns = [

    path('', views.SendNotificationView.as_view(), name="sendnotification"),
    path('/status', views.NotificationStatus.as_view(), name="notificationstatus"),
    path('/all-notification', views.AllNotificationView.as_view(), name="allnotification"),

]