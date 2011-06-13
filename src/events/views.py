from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _
from django.conf import settings
from events.models import Event, Invitation
from events.forms import EventForm, InvitationForm, RsvpForm
from django.template.context import RequestContext


class EventListView(ListView):
    queryset = Event.objects.all().order_by('start')

class EventDetailView(DetailView):
    queryset = Event.objects.all()

class EventCreateView(CreateView):
    form_class = EventForm
    template_name = 'events/form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, _('Event is created successfully'))
        return super(EventCreateView, self).form_valid(form)

class EventUpdateView(UpdateView):
    form_class = EventForm
    model = Event
    template_name = 'events/form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, _('Event is updated successfully'))
        return super(EventUpdateView, self).form_valid(form)

class InvitationView(FormView, SingleObjectMixin):
    form_class = InvitationForm
    template_name = 'events/invitation_form.html'
    queryset = Event.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InvitationView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        event = self.get_object()
        count = 0
        site = Site.objects.get_current()
        subject = event.name
        for email in form.cleaned_data['emails']:
            invitation, c = Invitation.objects.get_or_create(event=event, email=email, 
                                                             defaults={'sent': True})
            message = render_to_string('events/invitation_email.html',
                                       {'event': event, 'invitation': invitation,
                                        'site': site})
            message = mark_safe(message)
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            except:
                # failed to send e-mail; set `sent` to False
                invitation.sent = False
                invitation.save()
            else:
                count += 1
        messages.info(self.request, _('%(count)s invitations sent successfully' % {'count': count}))
        return super(InvitationView, self).form_valid(form)
    
    def get_success_url(self):
        return self.get_object().get_absolute_url()

class InvitationRsvpView(View, SingleObjectMixin):
    def get(self, request, hash):
        invitation = get_object_or_404(Invitation, hash=hash)
        form = RsvpForm({'status': invitation.status})
        return render_to_response('events/rsvp.html',
                                  {'invitation': invitation, 'form': form},
                                  context_instance=(RequestContext(request)))
        
    def post(self, request, hash):
        status = request.POST.get('status')
        if not status in ('N', 'A', 'M'):
            raise Http404
        invitation = get_object_or_404(Invitation, hash=hash)
        invitation.status = status
        invitation.save()
        return HttpResponseRedirect(invitation.event.get_absolute_url())
    