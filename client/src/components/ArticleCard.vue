<template>
  <div class="feed_card">
    <div class="card_image">
      <img :src="image"/>
    </div>
    <div class="card_caption">
      <p class="caption">{{caption}}</p>
      <p class="user_name"><b>By Chef: </b>{{post_username}}</p>
      <button class="del_btn" @click="deletePost(post_id)">Delete Post</button>
    </div>
  </div>

</template>

<script>
import {FindUserById} from '../services/users'
import {DeletePost} from '../services/posts'



export default {
  name: 'FeedCard',
  props: ['caption', 'image','post_username', 'user', 'post_id', 'getPosts'],
  data: ()=>({
    users_post_id: []
  }),
  methods: {
    async userIdToUserName(id){
      const res =  await FindUserById(id)
      console.log(res)
      return res.username
    },
    async deletePost(post_id){
      if (this.user.username === this.post_username) {
        const res = await DeletePost(post_id)
        this.$emit('getPosts')
        return res
      }
    }
  }
}
</script>

<style>



.feed_card {
  color: black;
  background-color: rgb(255, 255, 255);
  border: 1px solid;
  border-radius: 8px;
  max-width: 25vw;
  margin: 1em auto;
  cursor: pointer;
  box-shadow: 7px 10px 24px 0px rgba(0, 0, 0, 0.39);
  transition: all .2s ease;
}

.feed_card:hover{
  opacity: .8;
}

.card_image img{
  width:  100%;
  height: 25em;
  object-fit: cover;
  border-radius: 4px 4px 0 0;
  /* border-radius: 50%; */
}


.user_name, .caption {
  margin-left: 5px;
  color: #000;
}

.caption {
  white-space: pre-wrap;
  color: #000;
}

.del_btn {
  width: 100%;
}

</style>