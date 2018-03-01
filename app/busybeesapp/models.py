from django.db import models
from django.conf import settings
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, datetime, timedelta, time
import urllib.parse as urlparse

from .email import EmailSender

class Profile(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    nick_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    photo = models.ImageField(upload_to='profile_pics', default = 'profile_pics/default.png' )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def json(self):
        return {
        'id' : self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'phone': self.phone,
        'gender': self.gender,
        'photo': self.photo.url,
        'age': calculate_age(self.dob),
        }


    @staticmethod
    def post_save(sender, created, **kwargs):
        if created:
            instance = kwargs.get('instance')
            subject = 'New Member'
            recepients = ['abdelrahman.elbarbary@gmail.com']

            message = "Tamkeener: %s %s\n" % (instance.first_name, instance.last_name)
            message += "Email: %s\n" % instance.email
            message += "Phone: %s" % instance.phone

            EmailSender(instance, subject, message, recepients).start()

post_save.connect(Profile.post_save, sender=Profile)
