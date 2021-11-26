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
      postTitle: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      postId: '1',
      postDate: 'April 23',
      postMiniInfo: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam accumsan felis id quam fringilla varius. Ut eget nibh scelerisque odio pharetra rutrum in ut neque.'
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
  height: 180px;
  background: #202020;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  font-size: 1.2rem;
}

.post-content {
  margin-top: 0.5rem;
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