from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.


def index(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		return render(request, 'accounts/login.html')


def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		user = User.objects.filter(username=username)
		user2 = User.objects.filter(email=email)

		# if same username exits
		if user.exists():
			messages.error(request, "Account with entered username already exists")
			return redirect('/accounts')

		# if same email address already exits
		if user2.exists():
			messages.error(request, "Account with entered email already exists")
			return redirect('/accounts')

		# if password won't match
		if (pass1 != pass2):
			messages.error(request, "Passwords do not match")
			return redirect('/accounts')

		# Create the user
		user = User.objects.create_user(username, email, pass1)
		user.set_password(pass1)
		user.save()

		# log in user after signup
		user = authenticate(username=username, password=pass1)
		auth_login(request, user)

		return redirect('/')

	else:
		return render(request, 'error.html')


def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print(username, password)
		user = authenticate(username=username, password=password)

		if user is not None:
			auth_login(request, user)
			return redirect("/")
		else:
			messages.error(request, "Invalid credentials! Please try again")
			return redirect("/accounts")

	return render(request, "error.html")


def logout(request):
	auth_logout(request)
	messages.success(request, "Successfully Logged out")
	return redirect('/accounts')
