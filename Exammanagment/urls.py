"""Exammanagment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('user.urls', 'user'), namespace='User')),
    path('Dashboard', include(('dashboard.urls', 'Dashboard'), namespace='Dashboard')),
    path('Data-Upload', include(('data_upload.urls', 'Data-Upload'), namespace='Data-Upload')),
    path('My-upload', include(('my_upload.urls', 'My-Upload'), namespace='My-Upload')),
    path('Rejected-Upload', include(('rejected_upload.urls', 'Rejected-Upload'), namespace='Rejected-Upload')),
    path('View-Paper', include(('view_paper.urls', 'View-Paper'), namespace='View-Paper')),
    path('Send-Notification', include(('send_notification.urls', 'Send-Notification'), namespace='Send-Notification')),
    path('My-Account', include(('my_account.urls', 'My-Account'), namespace='My-Account')),
    path('About-Us', include(('about_us.urls', 'About-Us'), namespace='About-Us')),
    path('Contact-Us', include(('contact_us.urls', 'Contact-Us'), namespace='Contact-Us')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
