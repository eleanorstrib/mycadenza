from django.shortcuts import render
from django.http import HttpResponse
from .forms import CadenzaUserForm

def signup(request):
    if request.method == 'POST':
        form = CadenzaUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("oops")
    else:
        form = CadenzaUserForm()

    return render(request, 'signup/signup.html',{ 'form': form})
