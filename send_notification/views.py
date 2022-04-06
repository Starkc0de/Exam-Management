from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .forms import SendNotificationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required(login_url=''), name="dispatch")
class SendNotificationView(generic.TemplateView):
    template_name = "send-notification.html"  

    def post(self,request,*args, **kwargs):
        form = SendNotificationForm(request.POST)
        if form.is_valid():
            print(form)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save() 
            messages.info(request, 'Your Notification Successfully Send.')
            return HttpResponseRedirect(reverse('Send-Notification:sendnotification'))             
        else:
            messages.info(request, 'Your Notification has not Send ! You fill the right information')
            form = SendNotificationForm()
            return render(request, "send-notification.html")
                