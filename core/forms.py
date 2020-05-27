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
    class Meta:
        model = ContactMessage
        fields = '__all__'
        widgets = {
            'contact_message': forms.Textarea(attrs={'placeholder': u'Insert Message Here'}),
        }
