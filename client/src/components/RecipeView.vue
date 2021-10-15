<template>
<div>
  <div>
  <img :src="recipe.imageURL" />
  <h1>{{recipe.name}}</h1>
  <h3>{{ recipe.ingredients }}</h3>
  </div>
  <div>
  </div>
</div>
</template>

<script>
import recipes from '../data.json'
export default {
  name: 'RecipeView',
  data: () => ({
    recipe: null
  }),
  mounted: function() {
    this.recipe = recipes.find(
      recipe => recipe.id === parseInt(this.$route.params.recipe_id)
    )
  }
  
  } 
</script>

<style >
.listing-wrapper {
  width: 90%;
  margin: auto;
  border: 2px solid rgba(0, 0, 0, 0.3);
  border-radius: 6px;
}
.listing-header {
  display: flex;
  justify-content: space-around;
  width: 90%;
  margin: auto;
  border-bottom: 1px solid rgba(0, 0, 0, 0.3);
}

.header-content p,
.header-content h2 {
  margin: 0.5em auto;
}

.primary-image {
  text-align: center;
  padding: 1em 0;
  width: 80%;
  margin: auto;
  object-fit: contain;
}

.primary-image img {
  width: 100%;
}

.image-grid {
  display: grid;
  width: 100%;
  grid-template-columns: repeat(auto-fill, 200px);
  grid-gap: 1em;
  align-content: center;
  justify-content: center;
}

.grid-item {
  width: 100%;
  cursor: pointer;
}

.grid-item:hover {
  opacity: 0.7;
}

.grid-item img {
  object-fit: contain;
  width: 100%;
}
.listing-description {
  display: flex;
}

.left,
.right {
  flex: 1;
  padding: 1em;
  text-align: center;
}

.left h4,
.right h4 {
  text-decoration: underline;
}

div {
  color: white;
}
</style>
