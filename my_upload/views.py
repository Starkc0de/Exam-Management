from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from data_upload.models import DataUpload
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html"  

    def get(self, request):
        dataupload = DataUpload.objects.all()
        return render(request,  "my-upload.html",{'dataupload':dataupload}) 


class DeleteDataView(LoginRequiredMixin,generic.TemplateView):
    template_name = "my-upload.html" 

    def post(self, request, id,):
        DataUpload.objects.filter(id=id).delete()
        return render(request, "my-upload.html" )      
   