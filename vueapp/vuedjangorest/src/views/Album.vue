<template>
  <div class="album" id="album">
      <div class="album py-5">
          <div class="container">
                <div class="card mb-4 border-1 border-top-0 col-md-3" id="thing" :style="cssProps">
                  <img :src="album.img" class="card-img-top" alt="">
                  <div class="card-body" id="card">
                      <h4 class=""><a class="text-secondary">{{album.title}}</a></h4>
                      <p class="card-text" id="contenttext">{{album.artist}}</p>
                      <p class="text-muted" id="contenttext">{{album.date}}</p>
                      <div v-for="song in filteredsongs" :key="song.id" class="">
                      <h5 class="" id="contenttext"><h5 class="text-muted float-start mx-1" id="contenttext">{{song.tracklist}}.</h5><p class="card-text" id="contenttext mx-auto">{{song.title}}</p></h5>
                      </div>
                      <div class="btn-group my-2">
                      <a :href="album.host" class="btn btn-sm btn-outline-success" role="button" target="_blank" aria-pressed="true">View on Spotify</a>
                      </div>
                    </div>
                </div>
          </div>
      </div>
  </div>
</template>




<script>
  import { getAPI } from '../axios-api'
  export default {
    name: 'Album',
    data () {
      return {
          album: {},
          songs: []
        }
    },
    components: {
    },
    mounted () {
        this.getAlbum()
    },
    methods: {
        getAlbum() {
            const albumslug = this.$route.params.albumslug
            
            getAPI.get(`/albums${albumslug}`)
            .then(response => {
                console.log('Album API has recieved data')
                this.album = response.data
                this.album.img = 'http://127.0.0.1:8000' + this.album.img
                console.log(this.album)
            })
            .catch(err => {
                console.log(err)
          })
          getAPI.get(`/songs/`)
            .then(response => {
                console.log('Album API has recieved data')
                this.songs = response.data
            })
            .catch(err => {
                console.log(err)
          })
        }
    },
    computed: {
        filteredsongs(){
          return this.songs.filter(song => song.album == this.album.id)
        },
        cssProps() {
            return {
                '--albumprimR': (parseInt(this.album.primcolourR)),
                '--albumprimG': (parseInt(this.album.primcolourG)),
                '--albumprimB': (parseInt(this.album.primcolourB)),
                '--albumaccR': (parseInt(this.album.accentcolourR)),
                '--albumaccG': (parseInt(this.album.accentcolourG)),
                '--albumaccB': (parseInt(this.album.accentcolourB)),
            }
        }
    }
  }

</script>

<style scoped>
  #contenttext{
    color: #AAA7A3;
  }
  #album{
    background-color: #27292A!important;
  }
  #card{
    background-color:#242627!important;
  }
  #thing{
    background: linear-gradient(to bottom, rgb(var(--albumprimR), var(--albumprimG), var(--albumprimB)), rgb(var(--albumaccR), var(--albumaccG), var(--albumaccB)));
  }
</style>