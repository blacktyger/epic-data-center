from datetime import timedelta
from django.utils import timezone
from statistics import mean
from django import template
from decimal import Decimal

register = template.Library()


@register.filter()
def usd_to_btc(value):
    """
    Convert amount (value) of USD to BTC.
    """
    try:
        return Decimal(value) / d(CoinGecko.get.by_coin('BTC').latest().data['price'])
    except Exception as e:
        print(e)
        return value

@register.filter(name='multi')
def multi(value, num):
    return Decimal(value) * Decimal(num)


@register.filter(name='sub')
def subtract(value, arg):
    return value - arg


@register.filter()
def btc_to_usd(value):
    """
    Convert amount (value) of BTC to USD.
    """
    try:
        return Decimal(value) * Decimal(CoinGecko.get.by_coin('BTC').latest().data['price'])
    except Exception as e:
        print(e)
        return value


@register.filter(name='check_arrow')
def check_arrow(value):
    try:
        if Decimal(value) <= 0:
            return '<i class="fa fa-arrow-down color-red"></i>'
        else:
            return '<i class="fa fa-arrow-up color-green"></i>'
    except:
        pass

@register.filter(name='check_color')
def check_color(value):
    try:
        if Decimal(value) <= 0:
            return 'red'
        else:
            return 'green'
    except:
        pass

@register.filter
def get_dash(mapping, key):
    return mapping.get(key, '-')


@register.filter()
def minus_back(value, num):
    return Decimal(num) - Decimal(value)


@register.filter()
def add(value, num):
    return Decimal(value) + Decimal(num)


@register.filter()
def satoshi(value):
    return Decimal(value) * 100000000


@register.filter()
def times(value, num):
    return Decimal(value) * Decimal(num)


@register.filter()
def get_percent(value, num):
    """
    :param value:
    :param num:
    :return: rounded percentage value of num
    """
    return Decimal(Decimal(value) / Decimal(num) * 100)


@register.filter(name='colour')
def percentage_color(value):
    if value < 20:
        return f"progress-bar-danger"
    elif 20 <= value <= 50:
        return f"progress-bar-warning"
    else:
        return f"progress-bar-success"


@register.filter(name="epic_to")
def epic_to(value, target):
    """
    Convert amount (value) of Epic-Cash to given target - USD or Bitcoin.
    """
    try:
        return round(Decimal(Data.get.by_coin('EPIC').by_pair(target).latest().avg_price) * Decimal(value), 8)
    except Exception as e:
        print(e)
        return value


# def daily_mined(coin):
#     block_time = d(Explorer.get.by_coin(coin).latest().average_blocktime)
#     block_reward = d(Explorer.get.by_coin(coin).latest().reward)
#     return {'coins': d((86400 / block_time) * block_reward, 0),
#             'blocks': d(86400 / block_time, 0)}


# #     *** add all halvings data **
# def halving(coin):
#     """
#     Calculate time of next halving based on block height and average block time.
#     """
#     block_time = d(Explorer.get.by_coin(coin).latest().average_blocktime)
#     block_height = d(Explorer.get.by_coin(coin).latest().height)
#
#     def check_height():
#         if block_height < 480_960:
#             halving_height = 480_960
#         else:
#             halving_height = 1_157_760
#         return halving_height
#
#     time_left = ((check_height() - block_height) * block_time)
#     date = timezone.now() + timedelta(seconds=int(time_left))
#     return {'date': date, 'height': check_height()}


# def high_low_7d(coin, target=""):
#     data = [p for t, p in CoinGecko.get.by_coin(coin).latest().data['price_7d'+target]]
#     return {
#         'low': min(data),
#         'high': max(data),
#         'average': mean(data)
#         }



