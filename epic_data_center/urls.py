from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from django.conf import settings

from coingecko_feed import views as coingecko_views
from explorer_feed import views as explorer_views
from bitmart_feed import views as bitmart_views
from vitex_feed import views as vitex_views
from esm_feed import views as esm_views


router = routers.DefaultRouter()

router.register(r'vitex/update', vitex_views.UpdateView, 'vitex-update')
router.register(r'vitex/history', vitex_views.HistoryView, 'vitex-history')
router.register(r'vitex/holders', vitex_views.HoldersView, 'vitex-holders')

router.register(r'bitmart/update', bitmart_views.UpdateView, 'bitmart-update')
router.register(r'bitmart/history', bitmart_views.HistoryView, 'bitmart-history')

router.register(r'explorer/blocks', explorer_views.BlockView, 'explorer-blocks')
router.register(r'coingecko', coingecko_views.CoingeckoView, 'coingecko')
router.register(r'esm', esm_views.ESMView, 'esm')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
