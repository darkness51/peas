import re
from django import forms
from django.core.validators import email_re
from django.utils.translation import ugettext as _
from django.forms import CharField, Textarea, ValidationError
from events.models import Event, Invitation, RSVP_STATUS_CHOICES


email_separator_re = re.compile(r'[^\w\.\-\+@_]+')

class EmailsListField(CharField):
    widget = Textarea

    def clean(self, value):
        super(EmailsListField, self).clean(value)
        emails = email_separator_re.split(value)
        if not emails:
            raise ValidationError(_(u'Enter at least one e-mail address'))
        for email in emails:
            if not email_re.match(email):
                raise ValidationError(_('%s is not a valid e-mail address') % email)
        return emails

class InvitationForm(forms.Form):
    emails = EmailsListField(help_text=_("Enter invitee's email addresses; 1 per line."))

class RsvpForm(forms.Form):
    status = forms.CharField(widget=forms.RadioSelect(choices=RSVP_STATUS_CHOICES))

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user',)
