from django.shortcuts import render
from .models import profile
# Create your views here.
def home(request):
    Profile = profile.objects
    return render(request,'portapp/home.html',{'profile': Profile})