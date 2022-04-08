from django.shortcuts import render
from django.views import generic
from user.models import Role, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required(login_url=''), name="dispatch")
class MyAccountView(LoginRequiredMixin,generic.TemplateView):
    template_name = "my-account.html"  

    def get(self,request) :
            user=User.objects.get(id=self.request.user.id)
            roles=Role.objects.all()
            return render(request,self.template_name,{"user":user,"roles":roles})  

    def post(self, request, *args, **kwargs):
        name= request.POST.get('fullname')
        email= request.POST.get('email')
        role_id= request.POST.get('role')
        mobile_no= request.POST.get('mobile_no')
        address= request.POST.get('address')
        role=Role.objects.get(id=role_id)
        User.objects.filter(id=request.user.id).update(name=name, email = email, role=role, mobile_no = mobile_no, address = address, is_terms_conditions = True)         
        
        return render(request,self.template_name)
     

















