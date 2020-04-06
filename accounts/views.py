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

def room_aval ( request, ro ):
    user=Login.objects.get(roll=ro)
    context={'user':user}
    return render( request, 'accounts/rooms.html',context)

def confirm(request, pk1, pk2):
    user2 = Room.objects.get(number=pk2)
    user1=Login.objects.get(roll=pk1)
    context1 = {'user': user1}
    context2 = {'user': user2}
    print("YOOOOO")
    if request.method=='POST':
        print("YOOOOO")
        user2.aval -=1
        if user1.alloted != "NULL" :
            user3=Room.objects.get(number= user1.alloted)
            user3.aval +=1
            user3.save()
        user1.alloted= user2.number
        user2.save()
        user1.save()
        return render(request,"accounts/details.html",context1)
    return render(request, "accounts/confirm.html",context2)