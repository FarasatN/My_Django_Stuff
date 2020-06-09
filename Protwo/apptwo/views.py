from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
# from django.template import Template, Context, loader
from apptwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'apptwo/users.html',{'form':form})
