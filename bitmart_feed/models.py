from django.utils import timezone
from django.db import models


class Update(models.Model):
    """Storing latest Bitmart data updated every X time"""
    timestamp = models.DateTimeField(auto_now=True)
    price = models.JSONField(default=dict)
    change = models.JSONField(default=dict)
    volume = models.JSONField(default=dict)
    trades = models.JSONField(default=dict)
    bids = models.JSONField(default=dict)
    asks = models.JSONField(default=dict)
    candles = models.JSONField(default=dict)
    tickers = models.JSONField(default=dict)

    # def trades_list_with_datetime(self):
    #     new_list = []
    #
    #     for trade in self.trades['list']:
    #         new_list.append([trade[0], trade[1], arrow.get(trade[2]).datetime, trade[3]])
    #
    #     return new_list

    def __str__(self):
        return f"Update [{str(self.timestamp)}]"

    def __repr__(self):
        return f"BitmartUpdate [{str(self.timestamp)}]"


class History(models.Model):
    """Snapshot of Bitmart data saved every X time"""
    timestamp = models.DateTimeField(default=timezone.now)
    price = models.JSONField(default=dict)
    volume = models.JSONField(default=dict)
    trades = models.JSONField(default=dict)

    class Meta:
        ordering = ('-timestamp', )

    def __repr__(self):
        return f"BitmartHistory [{str(self.timestamp)}]"

