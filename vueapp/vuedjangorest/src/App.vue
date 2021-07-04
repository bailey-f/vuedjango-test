<template>
  <div id="container-fluid">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from '../src/components/Navbar.vue'
export default {
    name: 'App',
    data () {
      return {
          APIData: []
        }
    },
    components: {
      Navbar
    }
  }
</script>

<style>
  body{
    margin: 0;
    padding: 0;
    background-color:rgb(31, 31, 31)!important;
  }
</style>
