# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Addresscorrection(models.Model):

    #__Addresscorrection_FIELDS__
    order_number = models.CharField(max_length=255, null=True, blank=True)
    carrier = models.CharField(max_length=255, null=True, blank=True)
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    shipping_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    original_address = models.CharField(max_length=255, null=True, blank=True)
    corrected_address = models.CharField(max_length=255, null=True, blank=True)
    at_fault = models.CharField(max_length=255, null=True, blank=True)
    clinic = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    charged = models.BooleanField()

    #__Addresscorrection_FIELDS__END

    class Meta:
        verbose_name        = _("Addresscorrection")
        verbose_name_plural = _("Addresscorrection")



#__MODELS__END
