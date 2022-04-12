from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from data_upload.models import DataUpload
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@method_decorator(login_required(login_url='/'), name="dispatch")
class MyUploadView(LoginRequiredMixin,generic.TemplateView):
    template_name = "my-upload.html"  

    def get(self, request,*args, **kwargs):
        dataupload = DataUpload.objects.all().order_by('-id')

        p = Paginator(dataupload, 8)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page()
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        return render(request,  "my-upload.html",{'dataupload':dataupload, 'page_obj':page_obj}) 

@method_decorator(login_required(login_url='/'), name="dispatch")
class DeleteDataView(LoginRequiredMixin,generic.TemplateView):
    template_name = "my-upload.html" 

    def post(self, request, id,):
        DataUpload.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('My-Upload:myupload') )      
   