<template>
  <div>
    <div class="posts">
    <div class="post-article">
      <div class="post-content">
        <div class="blog-post-title">
            <a :href="'/blog/' + postId">
              {{postTitle}}
            </a>
        </div>
        <time class="post-date"> {{postDate}}</time>
        <div class="blog-post-content">
          {{postMiniInfo}}
        </div>
        <a
          :href="'/blog/' + postId"
          class="read-more"
          >Read more...</a
        >
      </div>
    </div>
    </div>
    <canvas></canvas>
  </div>
</template>

<script>
export default {
  name: "blog",
  data() {
    return {
      postTitle: 'Test',
      postId: 'test',
      postDate: 'April 23',
      postMiniInfo: 'Lorem Ipsum '
    };
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
  position: relative;
  display: flex;
  align-items: flex-start;
  width: 1000px;
  height: 200px;
  background: #2c2c2c;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  font-size: 1.5rem;
}
.post-content {
  margin-top: 0.5rem;
  margin-left: 1rem;
}
.post-date {
  letter-spacing: 3px;
  font-size: 1rem;
}
.blog-post-content {
  margin-top: 1rem;
  font-size: 1rem;
  color: #c0c0c0;
  margin-bottom: 0.5rem;
}
.read-more {
  font-size: 1rem;
}
a {
  color: #f1dcff;
}
</style>