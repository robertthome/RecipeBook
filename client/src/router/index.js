import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login'
import Recipes from '../components/Recipes'
import RecipeView from '../components/RecipeView'
import Feed from '../components/Feed'
import GetHere from '../components/GetHere'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', component: Login },
    { path: '/feed', component: Feed },
    { path: '/gethere', component: GetHere },
    { path: '/recipe/:recipe_id', component: RecipeView }
  ]
})
