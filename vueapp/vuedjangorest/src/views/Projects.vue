<template>
  <div class="projects" id="projects">
      <div class="album py-5">
          <div class="container">
            <div class="row">
              <div v-for="project in APIData" :key="project.id" class="col-md-4">
                <div class="card mb-4 border-secondary">
                  <div class="card-body bg-light" id="card">
                      <h4 class=""><a class="text-secondary">{{project.title}}</a></h4>
                      <p class="card-text" id="contenttext">{{project.content}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                      <router-link :to="{ name: 'project', params: {projectslug: project.absolute_url} }" class="btn btn-sm btn-outline-primary mx-1" role="button" aria-pressed="true">View</router-link>
                      </div>
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
    name: 'Projects',
    data () {
      return {
          APIData: []
        }
    },
    components: {
    },
    created () {
        getAPI.get('/projects/',)
          .then(response => {
            console.log('Project API has recieved data')
            this.APIData = response.data
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
  #projects{
    background-color: #27292A!important;
  }
  #card{
      background-color:#242627!important;
    }
</style>