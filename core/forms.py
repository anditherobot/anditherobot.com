from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.models import User
from django import forms
from .models import *
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })
    class Meta:
        model = ContactMessage
        fields = '__all__'
        widgets = {
            'contact_message': forms.Textarea(attrs={'placeholder': u'Insert Message Here'}),
        }
