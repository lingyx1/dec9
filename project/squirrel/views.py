from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Squirrel
from .forms import SquirrelForm
  
def all_squirrels(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }   
    return render(request, 'squirrel/all.html', context)

def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        # check form data
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }
    return render(request, 'squirrel/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        # check form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm()
    
    context = {
        'form': form,
    }
    return render(request, 'squirrel/add.html', context)

def map(request):
    sightings = Squirrel.objects.all()[0:99]
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/map.html', context)

def stats_squirrel(request):
    is_adult = Squirrel.objects.filter(Age = 'Adult').count()
    is_gray = Squirrel.objects.filter(Primary_Fur_Color = 'Gray').count()
    is_climbing = Squirrel.objects.filter(Climbing = True).count()
    is_running = Squirrel.objects.filter(Running = True).count()
    is_chasing = Squirrel.objects.filter(Chasing = True).count()

    count = [
            is_adult, is_gray, is_climbing, is_running, is_chasing
     ]

    context = {
            'count':count
    }

    return render(request, 'squirrel/stats.html', context)
