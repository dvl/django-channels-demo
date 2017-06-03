from django_filters import rest_framework as filters

from . import models


class LanceFilter(filters.FilterSet):

    class Meta:
        model = models.Lance
        fields = [
            'lote',
        ]
