from django.db import models

class VitexUpdate(models.Model):
    btc_price = models.CharField(max_length=128)
    usd_price = models.CharField(max_length=128)
    holders_count = models.IntegerField()
    holders_stats = models.JSONField(default={})


