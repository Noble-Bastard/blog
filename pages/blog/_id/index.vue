<template>
  <div class="home">
    <div class="post">
      <div class="post-title">
        <h2 class="title">{{ posts.postTitle }}</h2>
      </div>
      <div class="post-date">
        {{ postDate }}
      </div>
      <div class="post-content">
        <p class="content">{{ posts.postBody }}</p>
      </div>
      <div class="back-button">
        <NuxtLink to="../blog" class="click-me">
          <button class="back-btn" type="submit">Back</button>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "blog-read",
  data() {
    return {
      posts: [],
      postDate: "April 23",
    };
  },
  mounted() {
    axios
      .get("http://assabyn.xyz:5000/blog/read/" + this.$route.params.id)
      .then((response) => (this.posts = response.data));
  },
};
</script>

<style>
.home {
  margin: 0;
  padding: 0;
}
.post {
  width: 80%;
  margin-top: 8rem;
  padding-left: 27rem;
}
.post-date {
  margin-top: 0.2rem;
  letter-spacing: 3px;
  font-size: 1rem;
  color: #909096;
}
.post-content {
  width: 80%;
  margin-top: 3rem;
  font-size: 1rem;
  color: rgb(252, 240, 255);
}
.back-btn {
  margin-top: 3rem;
  border: 1.5px solid rgb(91, 68, 95);
  color: rgb(249, 219, 255);
  background: none;
  width: 150px;
  height: 40px;
}
</style>