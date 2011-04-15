from django import forms
from events.models import Event, EventType

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user',)
        
class SendInvitation(forms.Form):
    emails = forms.Textarea()
        
#class EventTpye(forms.ModelForm):
#    class Meta:
#        model = EventType
#        exclude = ('user',)