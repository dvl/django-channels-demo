import json

from django.core.serializers.json import DjangoJSONEncoder

from channels import Group, Channel
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import Lote, Lance

CRIAR_LANCE = 'criar_lance'


@channel_session_user_from_http
def lote_connect(message, lote_id):
    # Accept the incoming connection
    message.reply_channel.send({'accept': True})
    # Add them to the chat group
    Group(f'lote-{lote_id}').add(message.reply_channel)


@channel_session_user
def lote_disconnect(message, lote_id):
    Group(f'lote-{lote_id}').discard(message.reply_channel)


@channel_session_user
def lote_receive(message, lote_id):
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    payload['lote_id'] = lote_id

    Channel('lote.criar_lance').send(payload)


@channel_session_user
def criar_lance(message):
    lote_id = message.content['lote_id']
    valor = message.content['valor']

    lote = Lote.objects.get(pk=lote_id)
    lance = Lance.objects.create(lote=lote, valor=valor, usuario=message.user)

    payload = {
        'command': CRIAR_LANCE,
        'valor': lance.valor,
        'arrematante': lance.usuario.username,
        'horario': lance.criado_em,
    }

    Group(f'lote-{lote_id}').send({
        'text': json.dumps(payload, cls=DjangoJSONEncoder)
    })
