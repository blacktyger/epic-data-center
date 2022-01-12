from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from explorer_feed import views as explorer_views
from vitex_feed import views as vitex_views


router = routers.DefaultRouter()
router.register(r'vitex/update', vitex_views.UpdateView, 'vitex-update')
router.register(r'vitex/history', vitex_views.HistoryView, 'vitex-history')
router.register(r'vitex/holders', vitex_views.HolderseView, 'vitex-holders')
router.register(r'explorer/blocks', explorer_views.BlockView, 'explorer-blocks')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    ]
