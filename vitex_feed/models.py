from datetime import datetime

from django.db import models


class Update(models.Model):
    """Storing latest Vitex data updated every X time"""
    timestamp = models.DateTimeField(default=datetime.now)
    price = models.JSONField(default=dict)
    change = models.JSONField(default=dict)
    volume = models.JSONField(default=dict)
    trades = models.JSONField(default=dict)
    bids = models.JSONField(default=dict)
    asks = models.JSONField(default=dict)
    candles = models.JSONField(default=dict)
    tickers = models.JSONField(default=dict)

    class Meta:
        ordering = ('-timestamp', )

    def __repr__(self):
        return f"VitexUpdate [{str(self.timestamp)}]"


class History(models.Model):
    """Snapshot of Vitex data saved every X time"""
    timestamp = models.DateTimeField(default=datetime.now)
    price = models.JSONField(default=dict)
    volume = models.JSONField(default=dict)
    trades = models.JSONField(default=dict)

    class Meta:
        ordering = ('-timestamp', )

    def __repr__(self):
        return f"VitexHistory [{str(self.timestamp)}]"


class Holders(models.Model):
    """Storing latest Vitex Holders data updated every X time"""
    timestamp = models.DateTimeField(default=datetime.now)
    holders_count = models.IntegerField()
    holders_stats = models.JSONField(default=dict)

    class Meta:
        ordering = ('-timestamp', )

    def __repr__(self):
        return f"VitexHolders [{str(self.timestamp)}]"

