from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from explorer_feed import views as ex_view
from vitex_feed import views as vi_view


router = routers.DefaultRouter()
router.register(r'block', ex_view.BlockView, 'block')
router.register(r'vitex', vi_view.VitexUpdateView, 'vitex')
router.register(r'vitex_holders', vi_view.VitexHoldersUpdateView, 'vitex_holders')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    ]
