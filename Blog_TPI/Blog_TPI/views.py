from django.shortcuts import render


def Home(request):
	return render(request,'home.html')


def Search(request):
	return render(request,'search.html')