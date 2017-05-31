from channels import Group


def ws_receive(message):
    Group("chat").send({
        "text": message.content['text'],
    })


def ws_connect(message):
    # Accept the incoming connection
    message.reply_channel.send({'accept': True})
    # Add them to the chat group
    Group('chat').add(message.reply_channel)


def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
