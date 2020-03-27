from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Login
from django.contrib.auth import authenticate
from django.contrib import messages

def login( request ):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:

            user = Login.objects.get(roll = username)
            if user.pass_field == password:
                context={'user':user}
                return render('/account/details', context)
            else:
                messages.info(request, 'Username OR password is incorrect')


        except Login.DoesNotExist:
            return render('account/')

    return render(request, 'login.html')

def home( request ):
    return render(request, 'accounts/login.html')
def details (request, pk ):
    user=Login.objects.get(id=pk)
    context={'user':user}
    return render(request, 'accounts/details.html', context)
def room_aval ( request ):
    return render( request, 'accounts/rooms.html')
def confirm(request):
    return render( request, 'accounts/confirm.html')