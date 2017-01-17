from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadenzaUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse

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

    return render(request, 'signup/signup.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid() and request.user.is_authenticated():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was updated!')
            return redirect(change_password)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render (request, 'registration/change_password.html',
                    {'form': form}
                )

def get_data(request, id):
    user = CadenzaUser.objects.get(pk=id)
    data = serializers.serialize('json', [user])
    return JsonResponse(data, safe=False)
