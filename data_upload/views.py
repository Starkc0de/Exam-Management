from django.shortcuts import render
from django.views import generic
from data_upload.models import Course, Semester
from data_upload.forms import DataUploadForm
from django.contrib import messages

# Create your views here.

class DataUploadView(generic.TemplateView):
    template_name = "data-upload.html" 

    def get(self, request):
        cousres = Course.objects.all()
        semseters = Semester.objects.all()
        return render(request,  "data-upload.html",{'cousres':cousres, 'semseters':semseters}) 

    def post(self,request):
        if request.method == 'POST':
            form = DataUploadForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()  
                messages.info(request, 'Your Data Successfully Upload.')
                return render(request, "data-upload.html")
            else:
                messages.info(request, 'Your Data has not Upload ! You fill the right Data')
                form = DataUploadForm()
            return render(request, "data-upload.html")  


