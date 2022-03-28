import imp
from django.shortcuts import get_object_or_404, render
from django.views import generic
from user.models import User
# Create your views here.


class MyAccountView(generic.TemplateView):
    template_name = "my-account.html"  

    # def get(self, request, id, *args, **kwargs):
    #     instance = get_object_or_404(User, id=id)
    #     userprofile = User.objects.get(user_id=instance)


    #     return render(request, "my-account.html", {'userprofile':userprofile})