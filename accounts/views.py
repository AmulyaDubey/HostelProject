from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import Login,Room
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

def login( request):
    if request.method =='POST':
        print("HEELLOOOO")
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        try:
                 print("LOTTERRYY")
                 user=Login.objects.get(roll=username)
                 print(user)
                 print(user.pass_field)
                 if user.pass_field == password:
                        context = {'user': user}
                        return render(request, 'accounts/details.html', context)
                 else:
                        messages.info(request, 'Username OR password is incorrect')

        except:
                messages.info(request, 'Username OR password is incorrect')
    print("BYYYEEEE")
    form=AuthenticationForm()
    return render(request, "registration/login.html", {"form":form})

def home( request ):
    return render(request, 'accounts/login.html')


def details (request, pk ):
    user=Login.objects.get(id=pk)
    context={'user':user}
    return render(request, 'accounts/details.html', context)

def room_aval ( request ):
    return render( request, 'accounts/rooms.html',)

def confirm(request, pk):
    user = Room.objects.get(number=pk)
    context = {'user': user}
    return render( request, 'accounts/confirm.html',context)