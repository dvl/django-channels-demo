from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import api


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^leilao/', include('channels_demo.leilao.urls', namespace='leilao')),

    url(r'^api/', include(api.router.urls, namespace='api')),

    url(r'^admin/', admin.site.urls),
]
