from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from user.models import User
from .models import FeedBack
from django.contrib import messages
from data_upload.models import DataUpload
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required(login_url=''), name="dispatch")
class PaperView(generic.TemplateView):
    template_name = "view-paper.html"  

    def get(self, request):
        dataupload = DataUpload.objects.all()
        return render(request,  "view-paper.html",{'dataupload':dataupload})     

@method_decorator(login_required(login_url=''), name="dispatch")
class FeedBackView(generic.TemplateView):
    template_name = "feedback.html"  

    def post(self,request,id, *args, **kwargs): 
        comment = request.POST.get('comment')
        return_feedback = request.POST.get('return_feedback')
        status = request.POST.get('status')
        paper_data = DataUpload.objects.get(id=id)
        form = FeedBack(comment = comment, return_feedback = return_feedback, feedback_by = request.user, paper_data=paper_data) 
        form.save()
        paper_data.status=status
        paper_data.save()
        messages.info(request, 'Your Feedback Send to Student.')
        return HttpResponseRedirect(reverse('View-Paper:paper'))








