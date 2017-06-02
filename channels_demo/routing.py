from channels.routing import route

from .consumers import lote_connect, lote_disconnect, lote_receive, criar_lance


channel_routing = [
    route('websocket.connect', lote_connect, path=r'^/lote/(?P<lote_id>\d+)/$'),
    route('websocket.disconnect', lote_disconnect, path=r'^/lote/(?P<lote_id>\d+)/$'),
    route('websocket.receive', lote_receive, path=r'^/lote/(?P<lote_id>\d+)/$'),

    route('lote.criar_lance', criar_lance, command=r'^criar_lance$')
]
