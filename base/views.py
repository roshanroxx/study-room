from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Room
from .forms import Roomform
# Create your views here.

# rooms = [
#     {'id' : 1 , 'name' : 'lets learn pthon'},
#     {'id' : 2 , 'name' : 'design with me'},
#     {'id' : 3 , 'name' : 'frontend developer'},
# ]

def home(request):
    rooms = Room.objects.all
    context ={'rooms' : rooms}
    return render(request,'base/home.html' , context)

def room(request,pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room =i
    # 
    room =Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request,'base/room.html' , context)

def createroom(request):
    form = Roomform()
    if request.method == 'POST':
        form = Roomform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html',context)

def updateroom(request,pk):
    room =Room.objects.get(id=pk)
    form = Roomform(instance=room)
    if request.method == 'POST':
        form = Roomform(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
