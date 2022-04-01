from django.shortcuts import render
from django.views import generic
from data_upload.models import DataUpload

# Create your views here.

class RejectedUploadView(generic.TemplateView):
    template_name = "rejected-upload.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dataupload'] = DataUpload.objects.all()    

        return context