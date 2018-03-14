from django.db import models
from django.utils import timezone
from apps.OTC.models import OTCRegistration
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.


class RegistrationTry(models.Model):
    username = models.CharField(max_length=100,  blank=True, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=200,  blank=True, null=True)
    country = CountryField()
    city = models.CharField(max_length=60)
    extra_data = models.TextField(blank=True, null=True)
    otc = models.ForeignKey(OTCRegistration,on_delete=models.CASCADE, related_name='reg_otc', null=True, blank = True)
    created_in = models.DateTimeField(auto_now_add= True)
    is_finished = models.BooleanField(default=False)
    finished_in = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return "ID: %s, Created: %s, E-mail: %s" % \
               (self.id, self.created_in, self.email)

    def finish(self):
        self.is_finished = True     #utilization
        self.finished_in = timezone.now()
        self.otc.apply()            #utilization
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            new_otc = OTCRegistration.objects.create()
            self.otc = new_otc
            # somewhere in this place send link (OTC.link) to self.user_email
        return super().save(*args, **kwargs)