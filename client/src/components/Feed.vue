<template>
  <div class="feed">
    <div class="header">
      <h1><b>R</b>ECIPE BOOK</h1>
      <h3 class="description">
        <b>E</b>xplore, <b>F</b>ind, And <b>C</b>reate Beatiful Recipes To Share
        With The World
      </h3>
    </div>
    <div class="recipes">
      <Recipes />
      <h1 class="head1">Featured Recipes From <b>Top</b> Chefs </h1>
      <Articles />
    </div>
    <div>
      <h1 class="head1">Create Your Own Recipes</h1>
    </div>
    <div class="feed_form">
      <FeedForm :user="user" @getPosts="getPosts" />
    </div>
    <div class="scroll-feed">
      <FeedCard
        v-for="post in posts"
        :key="post.id"
        :caption="post.caption"
        :image="post.image"
        :post_username="post.username"
        :user="user"
        :getUserData="getUserData"
        :post_id="post.id"
        @getPosts="getPosts"
      />
      
      </div>
  </div>
</template>
<script>
import { GetPosts } from '../services/posts'
import { FindUserById } from '../services/users'
import FeedCard from '../components/FeedCard.vue'
import FeedForm from './FeedForm.vue'
import Recipes from './Recipes.vue'
import Articles from './Article.vue'

export default {
  name: 'Feed',
  components: {
    FeedCard,
    FeedForm,
    Recipes,
    Articles
  },
  props: ['user'],

  data: () => ({
    posts: [],
    error: null
  }),
  mounted: function () {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      try {
        const res = await GetPosts()
        this.posts = res
      } catch (error) {
        console.log(error)
        this.error = error
      }
    },
    async getUserData(id) {
      const res = await FindUserById(id)
      console.log('getUserData', res.username)
      return res.username
    }
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@700&display=swap');


.header {
  color: black;
  font-size: 2em;
  margin-top: 5em;
  margin-left: 5em;
  padding: 5em;
  background-image: url();
  font-family: 'Libre Baskerville', serif;
}

b {
  color: red;
}

.recipes {
  margin-top: 10em;
}

.head1 {
  display: flex;
  justify-content: center;
  font-size: 5em;
  color: black;
  font-family: 'Libre Baskerville', serif;
}

.feed {
  padding: 1em;
  display: grid;
  gap: 1em;
  justify-content: center;
}
.feed_form {
  margin-left: 30em;
  top: 4rem;
}
.scroll-feed {
  padding: 1em;
  display: grid;
  grid-template-columns: repeat(2, 25em);

  justify-content: center;
  margin-right: 40em;
  /* flex: 1;
  overflow-y: scroll; */
  /* height: 100vh; */
}
.item-view {
  padding: 1em;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 1150px;
}
</style>