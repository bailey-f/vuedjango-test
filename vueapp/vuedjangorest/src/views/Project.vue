<template>
  <div class="album" id="album">
      <div class="album py-5">
          <div class="container">
            <div class="row">
                <div class="card mb-4 mx-4 border-secondary border-1 rounded col-md" id="card">
                  <div class="card-body" id="card2">
                      <h4 class=""><a class="text-secondary">{{project.title}}</a></h4>
                      <p class="card-text" id="contenttext">{{project.content}}</p>
                      <p class="text-muted" id="contenttext">{{project.date}}</p>
                      <img :src="project.img" class="d-inline-block align-top pb-3 img-fluid rounded max-height-250" alt="" width="250">
                      <div class="btn-group my-2 float-start">
                        <a :href="project.host" class="btn btn-sm btn-outline-primary" role="button" target="_blank" aria-pressed="true">View Host</a>
                      </div>
                </div>
                </div>
                <div class="card mb-4 mx-4 box-shadow border-secondary col-md" id="card">
                  <div class="card-body" id="card2">
                      <h4 class=""><a class="text-secondary">Todo</a></h4>
                      <p class="card-text" id="contenttext">{{project.todo}}</p>
                      <p class="text-success" id="contenttext" v-if="project.isdone">This project is complete.</p>
                      <p v-else class="text-warning" id="contenttext">This project is in progress...</p>
                  </div>
                  </div>
                <div class="card mb-4 mx-4 box-shadow border-secondary col-md" id="card">
                  <div class="card-body" id="card2">
                      <h4 class=""><a class="text-secondary">Notes</a></h4>
                      <p class="card-text" id="contenttext">{{project.notes}}</p>
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
    name: 'Project',
    data () {
      return {
          project: {}
        }
    },
    components: {
    },
    mounted () {
        this.getProject()
    },
    methods: {
        getProject() {
            const projectslug = this.$route.params.projectslug
            
            getAPI.get(`/projects${projectslug}`)
            .then(response => {
                console.log('Project API has recieved data')
                this.project = response.data
                this.project.img = 'http://127.0.0.1:8000' + this.project.img
                console.log(this.project)
                console.log(this.project.isdone)
            })
            .catch(err => {
                console.log(err)
          })
        }
    },
    computed: {
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
      max-width: 405px;
      background-color:#242627!important;
  }
  #card2{
      max-width: 450px;
      background-color:#242627!important;
  }
</style>