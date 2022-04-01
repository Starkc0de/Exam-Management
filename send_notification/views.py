import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .forms import SendNotificationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class SendNotificationView(LoginRequiredMixin, generic.TemplateView):
    template_name = "send-notification.html"  

    def post(self,request):
        form = SendNotificationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()  
            messages.info(request, 'Your Notification Successfully Send.')
            return HttpResponseRedirect(reverse('Send-Notification:sendnotification'))             
        else:
            messages.info(request, 'Your Notification has not Send ! You fill the right information')
            form = SendNotificationForm()
            return render(request, "send-notification.html")
                