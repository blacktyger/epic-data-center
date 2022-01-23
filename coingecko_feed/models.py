from decimal import Decimal
from typing import Union
import requests
import json

from django.db import models


class Coingecko(models.Model):
    btc_feed_url = "https://blockchain.info"
    epic_feed_url = "https://api.coingecko.com/api/v3"

    timestamp = models.DateTimeField(auto_now=True)
    epic_vs_usd = models.DecimalField(decimal_places=8, max_digits=32)
    epic_vs_btc = models.DecimalField(decimal_places=8, max_digits=32)
    epic_vs_other = models.JSONField(default=dict)

    btc_vs_usd = models.DecimalField(decimal_places=8, max_digits=32)

    def price_epic_vs(self, currency: str):
        symbol = currency.upper()
        if len(symbol) == 3:
            try:
                url = f"{self.epic_feed_url}/simple/price?ids=epic-cash&vs_currencies={symbol}"
                data = json.loads(requests.get(url).content)
                return Decimal(data['epic-cash'][symbol.lower()])
            except json.JSONDecodeError as er:
                print(er)
                return 0

    def price_btc_vs(self, currency: str):
        symbol = currency.upper()
        if len(symbol) == 3:
            try:
                url = f"{self.btc_feed_url}/ticker"
                data = json.loads(requests.get(url).content)
                return Decimal(data[symbol]['last'])
            except json.JSONDecodeError as er:
                print(er)
                return 0

    def currency_to_btc(self, value: Union[Decimal, float, int], currency: str):
        """Find bitcoin price in given currency"""
        symbol = currency.upper()
        if len(symbol) == 3:
            try:
                url = f'{self.btc_feed_url}/tobtc?currency={currency}&value={value}'
                data = json.loads(requests.get(url).content)
                return Decimal(data)
            except json.JSONDecodeError as er:
                print(er)
                return 0

    def __str__(self):
        return f"Update [{str(self.timestamp)}]"

    def __repr__(self):
        return f"CoingeckoUpdate [{str(self.timestamp)}]"
