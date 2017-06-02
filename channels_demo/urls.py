from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^lotes/$', views.LotesListView.as_view(), name='lotes-list'),
    url(r'^lotes/(?P<pk>\d+)/$', views.LoteDetailView.as_view(), name='lotes-detail'),

    url(r'^admin/', admin.site.urls),
]
