# coding=utf-8
from django.shortcuts import render
from django import forms

from web.models import Registration


def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            Registration(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                comment=form.cleaned_data['comment']
            ).save()
    return render(request, 'index.html')


def dress_code(request):
    return render(request, 'single.html')


class RegistrationForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea, max_length=1000)
