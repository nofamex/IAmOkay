from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    return render(request,'announce.html')