import operator

from django.views.generic import TemplateView

from vitex_feed.models import Update
from coingecko_feed.models import Coingecko
from .price_chart import candle_chart, vitex_price


class VitexHomeView(TemplateView):
    template_name = 'exchanges.html'

    def get_context_data(self, **kwargs):
        context = super(VitexHomeView, self).get_context_data(**kwargs)
        update = Update.objects.get(id=1)
        prices = Coingecko.objects.get(id=1)
        print(prices)
        bids = [[float(b[0]), float(b[1]), float(b[0]) * float(b[1])] for b in update.bids]
        asks = [[float(a[0]), float(a[1]), float(a[0]) * float(a[1])] for a in update.asks]
        asks.reverse()
        # context['vitex_logo'] = Exchange.objects.get(name='ViteX').image
        context['prices'] = prices
        context['trades'] = update.trades_list_with_datetime()
        context['vitex'] = update
        context['trades_bought'] = update.trades['stats']['bought']
        context['trades_sold'] = update.trades['stats']['sold']
        context['vitex_chart'] = candle_chart(update)
        # context['vitex_depth'] = vitex_depth(data)
        # context['vitex_volume'] = vitex_volume(data)
        context['vitex_change24h_percent'] = update.change['24h_percentage']
        context['vitex_change24h'] = update.change['24h_quota']
        context['vitex_asks'] = asks
        context['vitex_bids'] = bids
        context['best_trades'] = update.trades['stats']['highest']
        context['biggest_bid'] = sorted(bids, key=operator.itemgetter(1))[-1]
        context['biggest_ask'] = sorted(asks, key=operator.itemgetter(1))[-1]

        return context
