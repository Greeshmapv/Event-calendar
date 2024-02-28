from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .models import Details

from .forms import EventForm
def index(request):
    return render(request,'index.html')

def addevent(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = EventForm(request.POST)
        else:
            event = get_object_or_404(Event, pk=id)
            form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        if id == 0:
            form = EventForm()
        else:
            event = get_object_or_404(Event, pk=id)
            form = EventForm(instance=event)

    return render(request, "addevent.html", {'form': form})

def events(request):
    context={'event_list':Event.objects.all(),}
    return render(request,'events.html',context)
def event_display(request):
    dict_eve={
        'eve':Details.objects.all()
    }
    return render(request,'event_display.html',dict_eve)

def edit_event(request, id):
    event = get_object_or_404(Event, pk=id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm(instance=event)

    return render(request, "edit_event.html", {'form': form, 'event': event})

def delete_event(request, id):
    event = get_object_or_404(Event, pk=id)

    if request.method == "POST":
        event.delete()
        return redirect('events')

    return render(request, "delete_event.html", {'event': event})
