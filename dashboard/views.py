from django.shortcuts import render
from django.views import generic
from data_upload.models import DataUpload,Course, Semester
from send_notification.models import SendNotification
from django.template.defaulttags import register
from django.template.loader import render_to_string

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = "base_template.html"

class DashboardView(generic.TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dataupload'] = DataUpload.objects.all()
        context['course'] = Course.objects.count()
        context['semester'] = Semester.objects.count()
        context['total_upload'] = DataUpload.objects.count()                 

        return context        


@register.filter(name='get_notification')
def get_notification(notification):
        get_data = SendNotification.objects.all()[:4]
        return render_to_string("notification.html", {"get_data": get_data})


@register.filter(name='count_notification')
def count_notification(notification):
        count_data = SendNotification.objects.count()
        return render_to_string("notification.html", {"count_data": count_data})        