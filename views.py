import datetime
from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from models import userprofile 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def home(request):
	return HttpResponse("<a href='http://127.0.0.1:8000/login'>login here</a>")


def hello(request):

    now= datetime.datetime.now()
    return HttpResponse(str(now) + "\n" +"Hello world")

def time(request):
	
	now= datetime.datetime.now()
	return HttpResponse(now)
# Create your views here.
def login_form(request):
    return render(request, 'login_form.html')

def submit(request):
	name=request.POST['username']
	pwd=request.POST['password']
	user = authenticate(username=name, password=pwd)
	
	if user is not None:

		if user.is_active:
			users=userprofile.objects.get(username=name)
			d=users.hostel_name
			return render(request,d+'hostel.html')
		else:
			return HttpResponse('the password is valid, account is disabled')
	else:
		return HttpResponse('the username and password does not match')






	
