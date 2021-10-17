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
        <h2>ADD YOUR OWN RECIPE</h2>
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
            const feedData = await CreatePost({'username':this.user.username,  'caption':this.caption, 'image':this.image})
            this.$emit('getPosts')
            return feedData   
        }
    }
}
</script>

<style>
.feed_form_input {
        display: flex;
        border: black solid 2px;
        /* margin: 5px 5px; */
        margin-top: 10px;
    }

.feed_form_button {
        margin-top: 10px;

    }
</style>


