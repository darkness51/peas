from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import ListView, DetailView, CreateView
from events.models import Event, Invitation
from events.forms import SendInvitation, ResponseInvitation

class EventListView(ListView):
    queryset = Event.objects.all().order_by('start')

class EventDetailView(DetailView):
    queryset = Event.objects.all()

class EventCreateView(CreateView):
    '''
    success_url = reverse('event_list')
    queryset = Event.objects.all()
    template_name = 'events/form.html'

    @login_required
    def dispatch(self, *args, **kwargs):
        super(EventCreateView).dispath(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)
    '''

@login_required
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
                    send_mail(subject, message, '0nur1nc3@gmail.com', [email])
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
        #mail_template.html in icine eklenecek
    else:
        form = SendInvitation()
    return render_to_response('events/invitation-form.html', 
                              {'form':form})

def response_invitation(request,id):
    if request.method == 'POST':
        form = ResponseInvitation(request.POST)
        if form.is_valid():
            response = request.POST['response']
            Invitation.objects.filter(id=id).update(status=response)
    else:
        form = ResponseInvitation()
    return render_to_response('events/response-form.html',{'form':form})
    