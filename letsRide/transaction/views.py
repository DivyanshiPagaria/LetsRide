from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
from .models import *

def index(request):
	return render(request, 'transaction/index.html')

def requesterr(request):
	if request.method == "POST":
		current_user = request.user
		location_from = request.POST['from']
		location_to = request.POST['to']
		quantity = request.POST['no_assets']
		date = request.POST['dateTime']
		asset_type = request.POST['asset_type']
		asset_sensitivity = request.POST['asset_sensitivity']
		receiver = request.POST['receiver']
		print(location_from)
		requester_details = requester(user = current_user, location_from = location_from, location_to = location_to, quantity = quantity, date = date, asset_type = asset_type, asset_sensitivity = asset_sensitivity, receiver = receiver)
		requester_details.save()

	return redirect('/')

def riderr(request):
	if request.method == "POST":
		current_user = request.user
		location_from = request.POST['from']
		location_to = request.POST['to']
		quantity = request.POST['no_assets']
		date = request.POST['dateTime']
		travel_medium = request.POST['travel_medium']

		rider_details = rider(user = current_user, location_from = location_from, location_to = location_to, quantity = quantity, date = date, travel_medium = travel_medium)
		rider_details.save()

	return redirect('/')

def profile(request):
	current_user = request.user

	request_by_user = requester.objects.filter(user = current_user)
	rider_by_user = rider.objects.filter(user = current_user)

	print(request_by_user, rider_by_user)