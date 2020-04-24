from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basic_app.forms import UserForm, UserProfileInfoForm

#

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse #Django 3.0 removes the django.core.urlresolvers module, which was moved to django.urls
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request,'basic_app/index.html')

@login_required
def special(request):
	return HttpResponse("You are logged in, Nice!")

@login_required #this is django built in decorate function 
def user_logout(request):
	logout(request) #here i call dango bulit in logout function which i imported avobe
	return HttpResponseRedirect(reverse('index'))

def register(request):


	registered= False

	if request.method=="POST":
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user


			if 'profile_pic' in request.FILES:
				profile.profile_pic=request.FILES['profile_pic']

			profile.save()

			registered= True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form=UserForm()
		profile_form=UserProfileInfoForm()

	return render(request, 'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form, 
		                                                                             'registered':registered})

                                            

def user_login(request): #dango built in login function and self create function should not be same

	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username, password=password)

		if user:
			if user.is_active: #is_authenticated, is_active, and is_anonymous is the properties of django bulit in authenticate funcntion
				login (request, user) #here i call built in login function from django
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Account not activate")

		else:
			print("Someone tried to login and failed!")
			print("username:{} and password:{}" .format(username, password))
			print("Invalied login details supplied!")

	else:
		return render(request, 'basic_app/login.html', {})



def other(request):
	my_dict={'text':'hello World', 'number':100}
	return render(request, 'basic_app/other.html', my_dict)

def basic(request):
	return render(request, 'basic_app/basic.html')

def relative(request):
	return render(request, 'basic_app/relative_url_templates.html')
