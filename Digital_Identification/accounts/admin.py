from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Beneficiary)
admin.site.register(Image)
# admin.site.register(Orginization)
# admin.site.register(User)
