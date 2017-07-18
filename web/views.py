# coding=utf-8
from django.shortcuts import render
from django import forms

from web.models import Registration, Hotel


def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            Registration(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                comment=form.cleaned_data['comment']
            ).save()
            return render(request, 'index.html', {"registered": True})
        else:
            return render(request, 'index.html', {"errors": True})
    return render(request, 'index.html')


def dress_code(request):
    return render(request, 'dress-code.html')


def hotel(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            Hotel(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                comment=form.cleaned_data['comment']
            ).save()
        return render(request, 'hotel.html', {"registered": True})
    return render(request, 'hotel.html')


class RegistrationForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea, max_length=1000, required=False)

