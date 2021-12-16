<template>
  <div>
    <div class="posts">
      <div class="post-article" v-for="(post, index) in posts" :key="index">
        <div class="post-content">
          <div class="blog-post-title">
            <NuxtLink :to="`/blog/${post.id}`">{{ post.postTitle }}</NuxtLink>
          </div>
          <time class="post-date"> {{ postDate }}</time>
          <div class="blog-post-content">
            {{ post.postMiniInfo }}
          </div>
          <NuxtLink :to="`/blog/${post.id}`" class="read-more">Read more...</NuxtLink>
        </div>
      </div>
    </div>
    <canvas></canvas>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "blog",
  data() {
    return {
      posts: [],
      postDate: "April 23"
    };
  },
  mounted() {
    axios
      .get("http://assabyn.xyz:5000/blog/list")
      .then((response) => (this.posts = response.data));
  }
};
</script>

<style>
.posts {
  position: absolute;
}
canvas {
  height: 100%;
  width: 100%;
}

.post-article {
  color: #f1dcff;
  margin-left: 18rem;
  margin-top: 2rem;
  /* display: flex; */
  /* align-items: flex-start; */
  width: 1000px;
  height: 160px;
  background: #202020;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  font-size: 1.2rem;
}
.blog-post-title {
  font-size: 1.3rem;
}
.post-content {
  padding-top: 1rem;
  margin-left: 1rem;
}

.post-date {
  letter-spacing: 3px;
  font-size: 1rem;
  color: #909096;
}

.blog-post-content {
  margin-top: 1rem;
  font-size: 1rem;
  color: #909096;
  margin-bottom: 0.5rem;
}

.read-more {
  font-size: 1rem;
}

a {
  color: #f1dcff;
}
</style>