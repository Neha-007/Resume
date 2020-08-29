from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'me/index.html')

def about(request):
	return render(request, 'me/about.html')

def career(request):
	return render(request, 'me/career.html')

def projects(request):
	return render(request, 'me/projects.html')

def education(request):
	return render(request, 'me/education.html')

def contact(request):
	return render(request, 'me/contact.html')