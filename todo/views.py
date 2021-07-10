from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import AdditemForm,NewUserForm
from . models import works
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.views.generic import CreateView


def normalView(request):
	return HttpResponse("<html><h1>Hello</h1></html>")

def todoappView(request):
	if request.user.is_authenticated:
		current_user=request.user  
		all_to_do_items=works.objects.filter(user=current_user)
		context={
		'all_items':all_to_do_items
		}
		return render(request,'todo/todolist.html/',context)
	else:
		return HttpResponseRedirect('/login')

def ItemAddView(request):
	errors=None
	form=AdditemForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user=request.user
		instance.save()
		return HttpResponseRedirect("/todolist")
	if form.errors:
		errors=form.errors
	template_name='todo/form.html'
	context={"form":form,"errors":errors}
	return render(request,template_name,context)

def deleteTodoView(request, i):
    y = works.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todolist') 

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return HttpResponseRedirect('/todolist')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return HttpResponseRedirect('/login')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect('/todolist') 
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})