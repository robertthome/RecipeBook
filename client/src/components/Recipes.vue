<template>
  <div>
    <h2 class="listing-header">{{ header }}</h2>
    <section class="listings">
      <div
        class="card col"
        :key="recipe.id"
        v-for="recipe in recipes"
        @click="navigatItem(recipe.id)"
      >
        <div class="image-wrapper">
          <img :src="recipe.imageURL" />
        </div>
        <div class="details row">
          <div>
            <h2>{{ recipe.name }}</h2>
          </div>
        </div>

        <hr class="rounded" />
        <div class="details row">
            <StarRating  v-bind:increment="0.5"
              v-bind:max-rating="5"
              inactive-color="#000"
              active-color="#f00"/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import recipes from '../data.json' 
import StarRating from 'vue-star-rating'

export default {
  name: 'Recipes',
  components: {
    StarRating
  },
  props: {
    header: String
  },
  data: () => ({
    recipes
  }),
  methods: {
    navigateItem(id) {
      console.log(id, "navigate item test")
      this.$router.push(`/recipe/${id}`)
    }
  }
}
</script>

<style>
.listing-header {
  text-align: center;
}

.listings {
  padding: 1em;
  display: grid;
  grid-template-columns: repeat(4, 18em);
  grid-gap: 1em;
  justify-content: center;
}

.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.col {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.card {
  width: 100%;
  border-radius: 6px;
  border: 2px solid rgba(0, 0, 0, 0.4);
  background: #fff;
  box-shadow: 4px 4px 14px 0px rgba(50, 50, 50, 0.39);
  transition: all 0.2s ease;
  cursor: pointer;
}

.card:hover {
  opacity: 0.5;
}
.card .image-wrapper {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}
.card img {
    width:  100%;
    height: 20em;
    object-fit: cover;
    border-radius: 4px 4px 0 0;
}

.card .details {
  padding: 0.5em 1em;
}

.details h2 {
  font-weight: 700;
}

.price {
  align-self: flex-start;
}
.badge {
  background-color: #c8e6c9;
  padding: 0.2em 0.6em;
  border-radius: 6px;
  color: #4caf50;
  height: 30px;
  line-height: 30px;
}
hr {
  background: #2c3e50;
  width: 90%;
} 

h2 {
  color: black;
}
</style>