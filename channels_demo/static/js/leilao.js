const ws = new channels.WebSocketBridge()
ws.connect('/leilao/stream/')
ws.listen((data) => console.log(data));
ws.demultiplex('lances', (payload, streamName) => {
  console.log(payload)
})

ws.socket.addEventListener('open', () => console.log('*** CONNECTED'))
ws.socket.addEventListener('close', () => console.log('*** DISCONNECTED'))
ws.socket.addEventListener('error', () => console.log('*** SERVER ERROR'))
ws.socket.addEventListener('message', (e) => console.log('*** MESSAGE', e))


const lance = document.getElementById('lance'),
      enviar = document.getElementById('enviar')

enviar.addEventListener('click', () => {
  let msg = {
    action: 'create',
    data: {
      lote: LOTE_PK,
      valor: lance.value
    }
  }

  ws.stream('lances').send(msg)

  console.log('*** LANCE ENVIADO', msg)
})
