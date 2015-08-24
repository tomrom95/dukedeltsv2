from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from news.models import Story
from .forms import AlumniForm, RushForm
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.contrib import messages
from core.models import Background
from exec_board.utils import ordered_list
import json
import random

def home(request):
    alumni_form = AlumniForm()
    rush_form = RushForm()
    context = RequestContext(request,
                           {'request': request,
                            'background': sorted(Background.objects.all(), key=lambda x: random.random()),
                            'user': request.user,
                            'story': Story.objects.all(),
                            'range': range(0,len(Story.objects.all())),
                            'board': ordered_list()})
    return render_to_response('dukedelts/home.html',
                             {'alumni_form': alumni_form,
                             'rush_form': rush_form},
                             context_instance=context)

def alumni(request):
    if request.method == 'POST':
        alumni_form = AlumniForm(request.POST)
        message = alumni_email(alumni_form)
        return HttpResponse(json.dumps({'message': message}))
    return HttpResponseRedirect('/')

def rush(request):
    if request.method == 'POST':
        rush_form = RushForm(request.POST)
        message = rush_email(rush_form )
        return HttpResponse(json.dumps({'message': message}))
    return HttpResponseRedirect('/')

def brothers(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    return render_to_response('dukedelts/brothers.html',
                             context_instance=context)

def adminlogin(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('dukedelts/adminlogin.html', context_instance=context)

def alumni_email(form):
    if form.is_valid():
        subject = "DukeDelts Alumni Response: " + form.cleaned_data['subject']
        message = "From: %s\n" %form.cleaned_data['name']
        message += "Email: %s\n" %form.cleaned_data['email']
        message += "To: Delt Alumni Chair\n\n"
        message += form.cleaned_data['message']
        sender = form.cleaned_data['email']

        recipients = ['tomrom95@gmail.com', 'aaron.jung1399@gmail.com']
        #recipients = ['tomrom95@gmail.com']
        send_mail(subject, message, EMAIL_HOST_USER, recipients)
        return "Success!"
    return "Failure!"

def rush_email(form):
    if form.is_valid():
        subject = "Rush Sign Up- %s" %form.cleaned_data['name']
        message = "Please sign this respondent to our rush list:\n\n"
        message += form.cleaned_data['name'] + "\n"
        message += "Class of: %s\n" %form.cleaned_data['year']
        message += form.cleaned_data['phone_number'] + "\n"
        message += form.cleaned_data['email']

        recipients = ['tomrom95@gmail.com', 'connor.garet@gmail.com']
        #recipients = ['tomrom95@gmail.com']
        send_mail(subject, message, EMAIL_HOST_USER, recipients)
        return True
    return False
