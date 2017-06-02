from django.views import generic

from . import models


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class LotesListView(generic.ListView):
    model = models.Lote


class LoteDetailView(generic.DetailView):
    model = models.Lote
