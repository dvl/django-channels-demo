const app = new Vue({
  el: '#app',

  data () {
    return {
      lanceAtual: null,
      lances: [/* Lance */]
    }
  },

  created () {
    this.connect()
  },

  mounted () {
    this.fetchData()
  },

  methods: {
    connect () {
      this.ws = new channels.WebSocketBridge()
      this.ws.connect('/leilao/stream/')
      this.ws.listen()

      this.ws.demultiplex('lances', (payload) => {
        if (payload.data.lote == LOTE_PK) {
          this.lances.splice(0, 0, payload.data)
        }
      })
    },

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
    }
  }

})
