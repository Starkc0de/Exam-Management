from django.urls import reverse
import random as r
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import Role ,User
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LoginView(generic.TemplateView):
    template_name = "user/login.html"  

    def post(self, request,*args, **kwargs):
        if request.method == "POST":
            form = User(request.POST)
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {user.fullname}.")  
                if request.user.is_authenticated:
                    return HttpResponseRedirect(reverse('Dashboard:dashboard'))                    
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        form = User()
        return HttpResponseRedirect(reverse('Dashboard:dashboard'))     


class RegisterView(generic.TemplateView):
    template_name = "user/register.html" 

    def get(self, request):
        roles=Role.objects.all()
        return render(request,  "user/register.html",{'roles':roles})

    def post(self, request, *args, **kwargs):
        name= request.POST.get('name')
        email= request.POST.get('email')
        role_id= request.POST.get('role')
        mobile_no= request.POST.get('mobile_number')
        password= request.POST.get('password')
        address= request.POST.get('address')
        is_terms_conditions =request.POST.get('is_terms_conditions')
        role=Role.objects.get(id=role_id)
        otp=""
        for i in range(4):
            otp+=str(r.randint(1,9))
        if User.objects.filter(mobile_no=mobile_no).exists():
            messages.info(request, 'Mobile Number Already taken')
            return HttpResponseRedirect(reverse('user_info:register'))
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already taken') 
            return HttpResponseRedirect(reverse('user_info:register'))
        user = User(fullname=name, email = email, role=role, mobile_no = mobile_no, address = address, is_terms_conditions = True)         
        user.set_password(password)
        user.otp = otp
        user.save()
        ######################### EMAIL SEND CODE ####################################
        htmly = get_template('user/otp-registration.html')
        d = { 'otp': otp }
        subject, from_email, to = 'Welcome', 'sunilgehlot703@gmail.com', email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()         
        return HttpResponseRedirect(reverse('user_info:verification'))      
        ###########################################################################

class OTPVerify(generic.TemplateView):
    template_name = "user/otp-verification.html"

    def get(self,request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request):
        otp = request.POST["otp"]
        if User.objects.filter(otp=otp).exists():
            User.objects.filter(otp=otp).update(is_active=True)
            messages.info(request, 'Account Verified Successfully.')
            return render(request, "dashboard.html")
        else:
            messages.error(request, 'Entered otp is wrong ,please enter again')
            return render(request, "user/otp-verification.html")

class PasswordOtpSendView(generic.TemplateView):
    template_name = "user/otp-send.html"

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            otp=""
            for i in range(4):
                otp+=str(r.randint(1,9))
            user = get_object_or_404(User, email=email)
            user.otp=otp
            user.save()
            ################################################ EMAIL SEND CODE  ##############
            htmly = get_template('user/otp-registration.html')
            d = { 'otp': otp }
            subject, from_email, to = 'Welcome', 'sunilgehlot703@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()         
            ################################################ EMAIL SEND CODE  ##############
            messages.info(request, 'A change password detail has been sent to your email id')
            return HttpResponseRedirect(reverse('user_info:password-otp'))
        else:
            messages.error(request, "This email not registered or not active")
            return HttpResponseRedirect(reverse('user_info:otp-send'))

class PasswordOTPVerifyView(generic.TemplateView):
    template_name = "user/otp-verification.html"

    def post(self, request):
        otp = request.POST["otp"]
        if User.objects.filter(otp=otp).exists():
            User.objects.filter(otp=otp).update(is_active=True)
            messages.info(request, 'Account Verified Successfully.')
            return HttpResponseRedirect(reverse('user_info:new-password'))
        else:
            messages.error(request, 'Entered otp is wrong ,please enter again')
            return render(request, "otp-verification.html")

class NewPasswordView(generic.TemplateView):
    template_name = 'user/password-set.html'

    def post(self, request, *args, **kwargs):      
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST.get('email')
        
        if password1 == password2:
            user_instance=get_object_or_404(User, email=email)
            user_instance.set_password(password1)
            user_instance.save()
        messages.success(request, "Password successfully Changed")
        return HttpResponseRedirect(reverse('user_info:login'))

@login_required
def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect(reverse('user_info:login'))

@method_decorator(login_required(login_url='/'), name="dispatch")
class UserProfile(LoginRequiredMixin,generic.TemplateView):
    template_name = "user/user.html"

    def get(self,request, *args, **kwargs):
        user = User.objects.all()
        return render(request,self.template_name, {'user':user})   


@method_decorator(login_required(login_url='/'), name="dispatch")
class EditUserView(LoginRequiredMixin,generic.TemplateView):
    template_name = "user/edit-user.html" 

    def get(self,request,id, *args, **kwargs) :
        user=get_object_or_404(User, id=id)
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