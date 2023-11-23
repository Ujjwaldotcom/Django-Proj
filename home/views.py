from django.shortcuts import render
from django.contrib.auth.decorators import login_required   #Add Authorization functionality of fucntion based views

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url = '/admin')  # Login URL redirects to the endpoint
def authorized(request):
    return render(request, 'authorized.html')
