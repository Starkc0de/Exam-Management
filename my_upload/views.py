from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from data_upload.models import DataUpload
# Create your views here.


class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html"  

    def get(self, request):
        dataupload = DataUpload.objects.all()
        return render(request,  "my-upload.html",{'dataupload':dataupload}) 




class DeleteDataView(generic.TemplateView):
    template_name = "my-upload.html" 

    def post(self, request, id, *args, **kwargs):
        service = get_object_or_404(DataUpload, id=id)
        service.delete()
        # return HttpResponseRedirect(reverse('My-Upload:DeleteData'))
        return render(request, "my-upload.html" )      
   