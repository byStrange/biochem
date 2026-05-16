from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label=_('Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Your name')}),
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={'placeholder': _('your@email.com')}),
    )
    phone = forms.CharField(
        max_length=50,
        required=False,
        label=_('Phone'),
        widget=forms.TextInput(attrs={'placeholder': _('+1 234 567 890')}),
    )
    subject = forms.CharField(
        max_length=200,
        label=_('Subject'),
        widget=forms.TextInput(attrs={'placeholder': _('How can we help?')}),
    )
    message = forms.CharField(
        label=_('Message'),
        widget=forms.Textarea(attrs={'rows': 6, 'placeholder': _('Your message...')}),
    )
