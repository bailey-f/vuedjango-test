<template>
  <div class="song" id="song">
      <div class="song py-5">
          <div class="container">
            <div class="row">
              <div v-for="album in APIData" :key="album.id" class="col-md-4">
                <div class="card mb-4 box-shadow border-2" id= "thing">
                  <div class="card-body bg-light" id="card">
                      <h4 class=""><a class="text-secondary">{{album.title}}</a></h4>
                      <p class="card-text" id="contenttext">{{album.artist}}</p>
                      <p class="text-muted" id="contenttext">{{album.date}}</p>
                      <img :src="album.img" class="d-inline-block align-top pb-3 img-fluid rounded" alt="" loading="lazy">
                      <a :href="album.host" class="btn btn-sm btn-outline-success mb-3" role="button" target="_blank" aria-pressed="true">View on Spotify</a>
                    <div v-for="song in APIDataSongs" :key="song.id" class="col-md-12">
                      <h4 class=""><a class="text-muted float-start mx-1">{{song.tracklist}}.</a><p class="card-text" id="contenttext">{{song.title}}</p></h4>
                    </div>
                </div>
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
    name: 'Songs',
    data () {
      return {
          APIData: [],
          APIDataSongs: []
        }
    },
    components: {
    },
    created () {
        getAPI.get('/albums/',)
          .then(response => {
            console.log('Albums API has recieved data')
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          }),
          getAPI.get('/songs/',)
          .then(response => {
            console.log('Songs API has recieved data')
            this.APIDataSongs = response.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    computed: {
        cssProps(k) {
            return {
                '--albumprim': (this.APIData[k-1].primcolour),
                '--albumacc': (this.APIData[k-1].accentcolour)
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
  #song{
    background-color: #27292A!important;
  }
  #card{
      background-color:#242627!important;
  }
  #thing{
      background: linear-gradient(to top, rgb(206, 46, 46), rgb(93,170,190))
  }
</style>