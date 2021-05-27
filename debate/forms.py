from django.db.models import fields
from . models import motion, argument, subpoint
from django import forms
from debate import models
from blog.models import BArticle


class motionCreate(forms.ModelForm):
    class Meta:
        model = motion
        fields = ['title', 'context', 'difficulty',]

class argumentCreate(forms.ModelForm):
    class Meta:
        model = argument
        fields = ['side', 'title', 'content']

class subpointCreate(forms.ModelForm):
    class Meta:
        model = subpoint
        fields = ['side', 'content',]

class blogCreate(forms.ModelForm):
    class Meta:
        model = BArticle
        fields = ['title', 'caption', 'content']
