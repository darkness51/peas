from django.shortcuts import render_to_response, get_object_or_404
from events.models import Event
from events.forms import EventForm, EventType
from django.core.context_processors import request
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
#from django.contrib.auth import authenticate, login

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render_to_response('events/detail.html',{'event':event})

def event_list(request):
    events = Event.objects.all().order_by('start')
    return render_to_response('events/list.html',{'events':events})


#@login_required
def event_form(request, id=None):
    if id:
        instance = get_object_or_404(Event, id=id)
    else:
        instance = None
    if request.method == 'POST':
        form = EventForm(data=request.POST, instance=instance)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return HttpResponseRedirect(reverse('event_list'))
        else:
            form = EventForm(instance=instance)
    else:
        form = EventForm(instance=instance)
    return render_to_response('events/form.html',
                              {'form':form},
                              context_instance=RequestContext(request))

def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_list'))
    else:
        form = EventForm()
    return render_to_response('events/form.html', {'form':form})

#def event_type(request):
#    if request.method == 'POST':
#        form = EventType(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('event_list'))
#    else:
#        form = EventType()
#    return render_to_response('events/type_form.html', {'form':form})

    
             
        
        
    
    