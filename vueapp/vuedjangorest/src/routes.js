import Vue from 'vue'
import VueRouter from 'vue-router'
import Projects from './views/Projects.vue'
import Project from './views/Project.vue'
import Albums from './views/Albums.vue'
import Album from './views/Album.vue'

Vue.use(VueRouter)

export default new VueRouter({
    // The default mode for vue router is a hash mode.
    // It uses URL hashing to simulate a full URL so that the page won't be reloaded when URL changes.
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'projects',
            component: Projects,
        },
        {
            path: '/',
            name: 'albums',
            component: Albums,
        },
        {
            path: '/projects/:projectslug',
            name: 'project',
            component: Project,
        },
        {
            path: '/albums/:albumslug',
            name: 'album',
            component: Album,
        }
    ]
})