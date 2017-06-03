from django.views import generic

from rest_framework import viewsets

from . import models, serializers, filters


class LeilaoListView(generic.ListView):
    model = models.Leilao


class LeilaoDetailView(generic.DetailView):
    model = models.Leilao


class LoteDetailView(generic.DetailView):
    model = models.Lote


class LanceViewSet(viewsets.ModelViewSet):
    queryset = models.Lance.objects.all()
    serializer_class = serializers.LanceSerializer
    filter_class = filters.LanceFilter
