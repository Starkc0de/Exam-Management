from django.shortcuts import get_object_or_404, render
from django.views import generic
from user.models import User
# Create your views here.


class MyAccountView(generic.TemplateView):
    template_name = "my-account.html"  
   

class EditUser(generic.TemplateView): 
    template_name = "my-account.html"  
     
    def get(self, request, id, *args, **callback_kwargs):
        instance = get_object_or_404(User, id=id)   

        return render(request, "my-account.html", {'instance':instance})        
















