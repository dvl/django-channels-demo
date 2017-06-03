from channels import include

channel_routing = [
    include('channels_demo.leilao.routing.channel_routing', path=r'^/leilao')
]
