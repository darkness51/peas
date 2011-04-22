from django.shortcuts import render_to_response, get_object_or_404
from events.models import Event, Invitation
from events.forms import EventForm, SendInvitation, ResponseInvitation
from django.core.context_processors import request
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
#from django.contrib.auth import authenticate, login

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render_to_response('events/detail.html',{'event':event})

def event_list(request):
    events = Event.objects.all().order_by('start')
    return render_to_response('events/list.html',{'events':events})


#@login_required
@csrf_exempt
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
@csrf_exempt
def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_list'))
    else:
        form = EventForm()
    return render_to_response('events/form.html', {'form':form})

@csrf_exempt
def send_invitation(request,slug):
    event = Event.objects.get(slug = slug)
    
    if request.method == 'POST':
        form = SendInvitation(request.POST)
        if form.is_valid():
            text = request.POST['emails']
            emails = text.split(";")        
            subject = event.name
        

            for email in emails:
                invitation = Invitation.objects.create(event = event, 
                                               email = email,
                                               sent = False,
                                               status='R')
                message = mark_safe(render_to_string('events/mail_template.html',
                                                      {'event':event,
                                                      'invitation':invitation}))
                try:
                    send_mail(subject, message,'0nur1nc3@gmail.com',[email])
                except:
                    sent = False
                else:
                    sent = True
                    
                Invitation.objects.filter(id=invitation.id).update(event = event, 
                                               email = email,
                                               sent = sent,
                                               status='R')
                
        #Invitation.objects.get_or_create 
        #multiple invitations for one email
        #http://mutlugunumuz.com{% url response_invitation id=invitation.id %}
        #mail_template.html in içine eklenecek
    else:
        form = SendInvitation()
    return render_to_response('events/invitation-form.html', {'form':form})

def response_invitation(request,id):
        
    if request.method == 'POST':
        form = ResponseInvitation(request.POST)
        if form.is_valid():
            response = request.POST['response']
            Invitation.objects.filter(id=id).update(status=response)
    
    else:
        form = ResponseInvitation()
    return render_to_response('events/response-form.html',{'form':form})

    
             
        
        
    
    