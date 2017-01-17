from django.shortcuts import render

def dashboard(request):
    return render(request, 'reports/dashboard.html', {})
