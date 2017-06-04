const app = new Vue({
  el: '#app',

  data () {
    return {
      lances: null,
      lanceAtual: null,
      segundosRestantes: null
    }
  },

  created () {
    this.connect()
  },

  mounted () {
    this.fetchData()
    setInterval(() => this.atualizarContador(), 1000)
  },

  methods: {
    connect () {
      this.ws = new channels.WebSocketBridge()
      this.ws.connect('/leilao/stream/')
      this.ws.listen()

      // TODO(andre): ouvir os eventos de close e error para definir
      // se precisamos buscar todos os lances novamente do servidor
      // em caso de falha na conexão.

      this.ws.demultiplex('lances', (payload) => {
        if (payload.data.lote == LOTE_PK) {
          this.lances.splice(0, 0, payload.data)
        }
      }
)    },

    fetchData () {
      axios.get(`/api/lances/?lote=${LOTE_PK}`)
        .then((response) => {
          this.lances = response.data
        })
    },

    enviarLance () {
      let msg = {
        action: 'create',
        data: {
          valor: this.lanceAtual,
          lote: LOTE_PK
        }
      }

      this.ws.stream('lances').send(msg)

      this.lanceAtual = parseInt(this.lanceAtual) + 5
    },

    atualizarContador () {
      if (this.lances) {
        let agora = moment(new Date()),  // agora deve vir do servidor
            fim = moment(this.lances[0].criado_em).add(120, 's')

        let restante = moment.duration(fim.diff(agora))

        this.segundosRestantes = restante.minutes() + ':' + restante.seconds()
      }
    }
  }
})
