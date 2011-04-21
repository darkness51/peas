from django import forms
from events.models import Event, Invitation

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user',)
        
class SendInvitation(forms.Form):
    emails = forms.CharField(widget=forms.Textarea)
    
class ResponseInvitation(forms.Form):
    class Meta:
        model = Invitation
        fields = ('status')
        
