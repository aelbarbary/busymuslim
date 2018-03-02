from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from busybeesapp.models import *
from django.urls import reverse
from django.conf import settings
import logging
from django.db.models import Max, Sum, Count
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from busybeesapp.forms import *
from django.contrib.auth.decorators import login_required
import json
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden
from django.db.models import Q
import os
import logging
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, render_to_response
from busybeesapp.email import EmailSender
from datetime import date, datetime, timedelta, time
from pytz import timezone
from django.db import connection
import random

def index(request):

    context = { }
    return render(request, 'index.html', context)

# class Register(CreateView):
#     success_url = '/'
#     template_name = 'registration/registration_form.html'
#     model = Profile
#     form_class = NewProfileForm
#     def form_valid(self, form):
#         response = super(Register, self).form_valid(form)
#         instance = self.object
#         user_name = '%s.%s' % (instance.first_name.replace(" ", "").lower(), instance.last_name.replace(" ", "").lower())
#         password = instance.password
#         # password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
#         print(instance)
#         count = Profile.objects.filter(username=user_name).count()
#
#         subject = 'Your account was created successfully!'
#         print(subject)
#         recepients = [instance.email]
#
#         message = "%s, Thank you for registering. your user information is listed below. \n" % (instance.first_name)
#         message = "User Name: %s \n" % user_name
#         message += "Password: %s\n" % password
#
#         EmailSender(instance, subject, message, recepients).start()
#
#         return response
