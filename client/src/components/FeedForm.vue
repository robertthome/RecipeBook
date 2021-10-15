<template>
    <div class='feed_form'>
        <form @submit.prevent="handleSubmit" class="feed_form_form">
            <textarea 
            name="caption"
            type="text"
            :value="caption"
            placeholder="Name of Dish followed by ingredients and directions"
            @input="handleForm"
            class="feed_form_input info"
            />
        <input
            name="image"
            type="text"
            :value="image"
            placeholder="Enter Image"
            @input="handleForm"
            class="feed_form_input img"
            />
            <button type="submit" class="feed_form_button">
            Blog
            </button>
        </form>
    </div>
</template>

<script>
import {CreatePost} from '../services/posts'

export default {
    name:"FeedForm",
    data: () => ({
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
            const feedData = await CreatePost({'username':this.user.username, 'caption':this.caption, 'image':this.image, 'likes':this.likes})
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

