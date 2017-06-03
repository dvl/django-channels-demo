from channels.generic.websockets import WebsocketDemultiplexer

from . import bindings


class Demultiplexer(WebsocketDemultiplexer):
    consumers = {
        'lances': bindings.LanceBinding.consumer,
    }

    groups = ['leilao.lances']

    http_user = True
