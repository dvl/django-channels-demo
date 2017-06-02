const lote_id = window.app['lote_id']

const CRIAR_LANCE = 'criar_lance'

const ws = new channels.WebSocketBridge()
ws.connect(`/lote/${lote_id}/`)

ws.socket.addEventListener('open', () => console.log('conectado'))
ws.socket.addEventListener('close', () => console.log('desconectado'))
ws.socket.addEventListener('error', () => console.log('server error'))

const lance = document.getElementById('lance'),
      enviar = document.getElementById('enviar'),
      tbody = document.getElementById('tbody')

enviar.addEventListener('click', () => {
  ws.send({
    command: CRIAR_LANCE,
    lote_id: lote_id,
    valor: lance.value
  })

  lance.value = null

  console.log('lance enviado')
})


ws.listen((data) => {
  console.log(data)

  if (data.command == CRIAR_LANCE) {
    let row = document.createElement('tr'),
        arrematante = document.createElement('td'),
        valor = document.createElement('td'),
        horario = document.createElement('td')

    arrematante.innerHTML = data.arrematante
    valor.innerHTML = 'R$ ' + data.valor
    horario.innerHTML = data.horario

    row.appendChild(arrematante)
    row.appendChild(valor)
    row.appendChild(horario)

    tbody.insertBefore(row, tbody.childNodes[0])
  }
})
