from django.utils import timezone

from channels.binding.websockets import WebsocketBinding

from . import models


class LanceBinding(WebsocketBinding):
    model = models.Lance
    stream = 'lances'
    fields = (
        'lote',
        'usuario',
        'valor',
        'criado_em',
    )

    @classmethod
    def group_names(cls, *args, **kwargs):
        return [
            'leilao.lances',
        ]

    def has_permission(self, user, action, pk):
        return True

    def create(self, data):
        self.model(
            lote_id=data['lote'],
            valor=data['valor'],
            usuario=self.user
        ).save()
