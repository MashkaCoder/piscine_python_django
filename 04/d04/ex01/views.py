from django.shortcuts import render, redirect
# Create your views here.

def display(request):
	return render(request, 'ex01/display.html')

def django(request):
	return render(request, 'ex01/django.html')

def templates(request):
	return render(request, 'ex01/templates.html')
