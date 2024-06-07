from django.db import models


class Geonode(models.Model):
    ip_address = models.CharField(max_length=250, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    protocal = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    Uptime = models.CharField(max_length=250, null=True, blank=True)