from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mycadenza.serializers import CadenzaUserSerializer
from .forms import CadenzaUserForm
from .models import CadenzaUser


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

@api_view(['GET'])
def api_get_user(request, id):
    try:
        user = CadenzaUser.objects.get(id=request.user.id)
    except CadenzaUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CadenzaUserSerializer(user)
        return Response(serializer.data)
