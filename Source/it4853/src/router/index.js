import Vue from 'vue'
import Router from 'vue-router'
import SearchHome from '@/components/SearchHome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SearchHome',
      component: SearchHome
    }
  ]
})
