from django.shortcuts import render
from django.views import generic
from .models import AboutUs

# Create your views here.


class AboutUsView(generic.TemplateView):
    template_name = "about.html"  

    def get(self, request):
        about = AboutUs.objects.all()
        return render(request,  "about.html",{'about':about})
