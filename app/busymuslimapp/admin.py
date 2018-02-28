from django.contrib import admin
from .models import  *
from .forms import *

admin.site.site_header = 'BusyMuslim admin'

class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(Profile, ProfileAdmin)
