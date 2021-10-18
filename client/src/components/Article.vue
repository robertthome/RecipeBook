<template>
  <div>
    <h2 class="article">{{ header }}</h2>
    <section class="">
      <div
        class=""
        :key="article.id"
        v-for="article in articles"
        @click="navigatItem(article.id)"
      >
        <div class="article-img">
          <img :src="article.imageURL" />
          <div class="side-content">
          <h1 class="dish">{{article.dish}}</h1>
          <h2>{{ article.by }}</h2>
          <p class="ingredients"><b>INGREDIENTS</b> {{article.ingredients}}</p>
          </div>
    
        </div>
        <div class="content">
          <div>
              
              <p class="steps"><b>DIRECTIONS</b>{{article.steps}}</p>
          </div>
        </div>

        <hr class="" />
        <div class="">
            
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import articles from '../articles.json' 


export default {
  name: 'Articles',
  props: {
    header: String
  },
  data: () => ({
    articles
  }),
  methods: {
    navigateItem(id) {
      console.log(id, "navigate item test")
      this.$router.push(`/article/${id}`)
    }
  }
}
</script>

<style>

.h1 {
  margin-bottom: 50px;
}

.dish {
  color: black;
  font-size: 32px;
  
}

.article-img {
  display: flex;
}



img {
  height: 30em;
  width: 40em;
}

.ingredients {

  white-space: pre-wrap;
  color: black;
  font-size: 1.5em;
  text-decoration: none;

}

.steps {
 white-space: pre-line;
  color: black;
  font-size: 1.5em;
  margin-left: 50px;
}

</style>