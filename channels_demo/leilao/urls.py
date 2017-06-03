from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LeilaoListView.as_view(), name='leilao-list'),
    url(r'^leilao/(?P<pk>\d+)/$', views.LeilaoDetailView.as_view(), name='leilao-detail'),
    url(r'^lote/(?P<pk>\d+)$', views.LoteDetailView.as_view(), name='lote-detail'),
]
