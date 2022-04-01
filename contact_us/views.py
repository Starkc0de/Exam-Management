from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

# Create your views here.


class ContactUsView(generic.TemplateView):
    template_name = "contact-us.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()

        return context     

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()  
            messages.info(request, 'Your form Successfully submitted.')
            return render(request, "contact-us.html")
        else:
            messages.info(request, 'Your form has not submitted ! You fill the right information')
            form = ContactForm()
        return render(request, "contact-us.html")  
