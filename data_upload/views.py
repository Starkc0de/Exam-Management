from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from data_upload.models import Course, Semester, DataUpload
from data_upload.forms import DataUploadForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from send_notification.models import SendNotification

# Create your views here.

class DataUploadView(generic.TemplateView):
    template_name = "data-upload.html" 

    def get(self, request):
        course_list = Course.objects.all()
        sem = Semester.objects.all()
        return render(request,  "data-upload.html",{'course_list':course_list, 'sem':sem}) 

    def post(self,request):
        if request.method == 'POST':
            form = DataUploadForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()  
                title = 'new ' + instance.subject +' paper uploaded by '+ request.user.fullname
                message="Please Check Your Paper"
                notification=SendNotification.objects.create(title=title,message=message)
                notification.send_notification_by.add()
                notification.save()
                messages.info(request, 'Your Data Successfully Upload.')
                return HttpResponseRedirect(reverse('My-Upload:myupload'))
            else:
                messages.info(request, 'Your Data has not Upload ! You fill the right Data')
                form = DataUploadForm()
            return render(request, "data-upload.html")  

@method_decorator(login_required(login_url=''), name="dispatch")
class EditDataView(generic.TemplateView):
    template_name = "data-upload.html" 
    form = DataUploadForm

    def get(self, request, id, *args, **callback_kwargs):
        instance = get_object_or_404(DataUpload, id=id)
        sem = Semester.objects.all()
        course_list = Course.objects.all()
        
        return render(request, "data-upload.html", {'instance':instance, 'sem':sem, 'course_list':course_list,})

    def post(self, request, id, *args, **kwargs):
        data = get_object_or_404(DataUpload, id=id)    
        form = DataUploadForm(request.POST, request.FILES or None, instance=data )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save() 
            messages.info(request, 'Your Data Successfully Updated.')        
            return HttpResponseRedirect(reverse('My-Upload:myupload') ,{'form':form})  
        else:
            context = {"form": form , "data":data}
            messages.info(request, 'Your Data Not Updated')        
            return render(request, "data-upload.html", context)                  
