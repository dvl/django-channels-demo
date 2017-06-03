from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^leilao/', include('channels_demo.leilao.urls', namespace='leilao')),
    url(r'^chat/', include('channels_demo.chat.urls', namespace='chat')),

    url(r'^admin/', admin.site.urls),
]
