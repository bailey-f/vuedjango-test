<template>
  <div class="album" id="album">
      <div class="album py-5">
          <div class="container">
            <div class="row">
              <div v-for="album in APIData" :key="album.id" class="col-md-3">
                <div class="card mb-4 border-secondary">
                  <div class="card-body bg-light" id="card">
                      <h4 class=""><a class="text-secondary">{{album.title}}</a></h4>
                      <p class="card-text" id="contenttext">{{album.artist}}</p>
                      <p class="text-muted" id="contenttext">{{album.date}}</p>
                      <div class="btn-group ">
                      <a :href="album.host" class="btn btn-sm btn-outline-success" role="button" target="_blank" aria-pressed="true">View on Spotify</a>
                      <router-link :to="{ name: 'album', params: {albumslug: album.absolute_url} }" class="btn btn-sm btn-outline-primary mx-1" role="button" aria-pressed="true">View Tracklist</router-link>
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
    name: 'Albums',
    data () {
      return {
          APIData: []
        }
    },
    components: {
    },
    created () {
        getAPI.get('/albums/',)
          .then(response => {
            console.log('Album API has recieved data')
            this.APIData = response.data
            console.log(this.APIData)
          })
          .catch(err => {
            console.log(err)
          })
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
</style>