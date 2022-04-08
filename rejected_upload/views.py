from django.shortcuts import render
from django.views import generic
from data_upload.models import DataUpload
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@method_decorator(login_required(login_url=''), name="dispatch")
class RejectedUploadView(LoginRequiredMixin,generic.TemplateView):
    template_name = "rejected-upload.html"

    def get(self, request,*args, **kwargs):
        dataupload = DataUpload.objects.all()
        
        p = Paginator(dataupload, 8)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page()
        except EmptyPage:
            page_obj = p.page(p.num_pages)  

        return render(request,  "rejected-upload.html",{'dataupload':dataupload, 'page_obj':page_obj}) 