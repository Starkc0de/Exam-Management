from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import FeedBack
from django.contrib import messages
from data_upload.models import DataUpload
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class PaperView(LoginRequiredMixin,generic.TemplateView):
    template_name = "view-paper.html"  

    def get(self, request):
        dataupload = DataUpload.objects.all()
        return render(request,  "view-paper.html",{'dataupload':dataupload})     


class FeedBackView(LoginRequiredMixin,generic.TemplateView):
    template_name = "feedback.html"  

    def post(self,request, *args, **kwargs): 
        comment= request.POST.get('comment')
        return_feedback= request.POST.get('return_feedback')
        status= request.POST.get('status')
        feedback_by= request.POST.get('feedback_by')
        form = FeedBack(comment=comment, return_feedback = return_feedback, status=status, feedback_by = feedback_by,) 
        form.save()
        messages.info(request, 'Your Feedback Send to Student.')
        return HttpResponseRedirect(reverse('View-Paper:paper'))
        # if request.POST.get('Approved'):
        #     form.status = "Approved"
        #     print("gvhjbkl;kjhkljhklhkh")
        # elif request.POST.get('Rejected'):
        #     form.status = "Rejected"
        #     form.save()
        #     return render(request, "feedback.html")  
        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     instance.user = request.user
        #     instance.save()  
        #     messages.info(request, 'Your Feedback Send to Student.')
        #     return HttpResponseRedirect(reverse('Dashboard:dashboard'))
        # else:
        #     messages.info(request, 'Your Feedback has not Send Student ! Please Checked')
        #     form = FeedBackForm()
        # return render(request, "feedback.html")      