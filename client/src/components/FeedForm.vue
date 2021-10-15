<template>
    <div class='feed_form'>
        <form @submit.prevent="handleSubmit" class="feed_form_form">
        <input
            name="image"
            type="text"
            :value="image"
            placeholder="Enter Image"
            @input="handleForm"
            class="feed_form_input img"
            />
            <input name="recipe_name" 
            type="text" 
            :value="name" 
            placeholder="Name of Dish"
            @input="handlForm"
            class="feed_form_imput"    
            />
            <textarea
            name="ingredients" 
            type="text" 
            :value="ingrediants" 
            placeholder="Ingredients" 
            @input="handform" 
            class="feed_form_input"/>
            <textarea 
            name="caption"
            type="text"
            :value="caption"
            placeholder="Directions"
            @input="handleForm"
            class="feed_form_input info"
            />
            <button type="submit" class="feed_form_button">
            submit
            </button>
        </form>
    </div>
</template>

<script>
import {CreatePost} from '../services/posts'

export default {
    name:"FeedForm",
    data: () => ({
        name: '',
        ingredients: '',
        caption:'',
        image:''
    }),
    props:['user'],
    methods:{
        handleForm(e) {
            // console.log(e.target.value)
            if (e.target.name === "caption"){
                this.caption = e.target.value
            } else {
                this.image = e.target.value
            }
            
        },
        async handleSubmit() {
            const feedData = await CreatePost({'name':this.user.name, 'ingredients':this.ingredients, 'caption':this.caption, 'image':this.image})
            this.$emit('getPosts')
            return feedData   
        }
    }
}
</script>

<style>
 .feed_form {
        white-space: pre-wrap;
    }
</style>

