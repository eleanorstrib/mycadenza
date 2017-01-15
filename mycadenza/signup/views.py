from django.shortcuts import render

def signup(request):
    return render(request, 'signup/signup.html',{})

# Create your views here.
