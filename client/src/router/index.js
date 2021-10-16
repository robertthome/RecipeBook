import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login'
import RecipeView from '../components/RecipeView'
import Feed from '../components/Feed'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', component: Login },
    { path: '/feed', component: Feed },
    { path: '/recipe/:recipe_id', component: RecipeView }
  ]
})
