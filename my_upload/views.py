from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from data_upload.models import DataUpload
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html"  

    def get(self, request,*args, **kwargs):
        dataupload = DataUpload.objects.all()
        return render(request,  "my-upload.html",{'dataupload':dataupload}) 

@method_decorator(login_required(login_url=''), name="dispatch")
class DeleteDataView(generic.TemplateView):
    template_name = "my-upload.html" 

    def post(self, request, id,):
        DataUpload.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('My-Upload:myupload') )      
   