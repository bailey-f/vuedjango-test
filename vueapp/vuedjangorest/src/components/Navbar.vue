<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light nav-1" id="navbar">
      <div class="container mw-0 px-3">

        <a class="navbar-brand" href="#">
        <img src="../assets/logo.jpg" width="" height="30" class="d-inline-block align-top rounded" alt="" loading="lazy">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
            <router-link :to = "{ name:'projects' }" exact>Projects</router-link>
            </li>
            <li class="nav-item mw-0 px-3">
            <router-link :to = "{ name:'albums' }" exact>Albums</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: 'Navbar',
  }
</script>

<style scoped>
  a {
    color:rgb(255, 255, 255);
  }
  #navbar {
    background: rgb(56, 56, 56);
  }
</style>