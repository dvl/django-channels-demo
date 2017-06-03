from . import consumers

channel_routing = [
    consumers.Demultiplexer.as_route(path=r'^/stream/$'),
]
