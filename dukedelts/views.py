from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from news.models import Story
from .forms import AlumniForm, RushForm
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.contrib import messages
from core.models import Background
from exec_board.utils import ordered_list

def home(request, *args):
    alumni_form = AlumniForm()
    rush_form = RushForm()
    alumni_sent = 'alumni_sent' in args
    rush_sent = 'rush_sent' in args
    context = RequestContext(request,
                           {'request': request,
                            'background': Background.objects.all(),
                            'user': request.user,
                            'story': Story.objects.all(),
                            'range': range(0,len(Story.objects.all())),
                            'board': ordered_list()})
    if request.method == 'POST' and "alumni" in request.POST:
        alumni_form = AlumniForm(request.POST)
        alumni_sent = alumni_email(alumni_form)
        messages.success(request, 'Alumni email sent', extra_tags='alumni')
        return HttpResponseRedirect('/#alumni')
    elif request.method == 'POST' and "rush" in request.POST:
        rush_form = RushForm(request.POST)
        rush_sent = rush_email(rush_form)
        messages.success(request, 'Rush email sent', extra_tags='rush')
        return HttpResponseRedirect('/#recruitment')
    return render_to_response('dukedelts/home.html',
                             {'alumni_form': alumni_form,
                             'rush_form': rush_form,
                             'alumni_sent': alumni_sent,
                             'rush_sent': rush_sent},
                             context_instance=context)

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

        recipients = ['tomrom95@gmail.com']
        send_mail(subject, message, EMAIL_HOST_USER, recipients)
        return True
    return False

def rush_email(form):
    if form.is_valid():
        subject = "Rush Sign Up"
        message = "Please sign this respondent to our rush list:\n\n"
        message += form.cleaned_data['name'] + "\n"
        message += "Class of: %s\n" %form.cleaned_data['year']
        message += form.cleaned_data['phone_number'] + "\n"
        message += form.cleaned_data['email']

        recipients = ['tomrom95@gmail.com']
        send_mail(subject, message, EMAIL_HOST_USER, recipients)
        return True
    return False
