import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from './views/Posts.vue'

Vue.use(VueRouter)

export default new VueRouter({
    // The default mode for vue router is a hash mode.
    // It uses URL hashing to simulate a full URL so that the page won't be reloaded when URL changes.
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'posts',
            component: Posts,
        },
        
    ]
})