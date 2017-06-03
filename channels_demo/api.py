from rest_framework import routers

from .leilao import views as leilao_views


router = routers.DefaultRouter()
router.register(r'lances', leilao_views.LanceViewSet, base_name='lance')
