from django.views import generic

from . import models


class LeilaoListView(generic.ListView):
    model = models.Leilao


class LeilaoDetailView(generic.DetailView):
    model = models.Leilao


class LoteDetailView(generic.DetailView):
    model = models.Lote
