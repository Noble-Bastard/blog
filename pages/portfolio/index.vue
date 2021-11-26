<template>
  <div>
    <div class="projects">
      <div class="project-article">
        <div class="project-content">
          <div class="project-image">
            <img
              src="../../assets/project.jpg"
              alt=""
              width="90px"
              height="90px"
            />
          </div>
          <div class="project-text">
            <div class="project-title">
              <a :href="'/project/' + postId"> {{ postTitle }} 1 </a>
            </div>
            <div class="project-mini-info">
              {{ postMiniInfo }}
            </div>
            <a :href="'/project/' + postId" class="read-more">Read more...</a>
          </div>
        </div>
      </div>
      <div class="project-article">
        <div class="project-content">
          <div class="project-image">
            <img
              src="../../assets/project.jpg"
              alt=""
              width="90px"
              height="90px"
            />
          </div>
          <div class="project-text">
            <div class="project-title">
              <a :href="'/project/' + postId"> {{ postTitle }} 1 </a>
            </div>
            <div class="project-mini-info">
              {{ postMiniInfo }}
            </div>
            <a :href="'/project/' + postId" class="read-more">Read more...</a>
          </div>
        </div>
      </div>
      <div class="project-article">
        <div class="project-content">
          <div class="project-image">
            <img
              src="../../assets/project.jpg"
              alt=""
              width="90px"
              height="90px"
            />
          </div>
          <div class="project-text">
            <div class="project-title">
              <a :href="'/project/' + postId"> {{ postTitle }} 1 </a>
            </div>
            <div class="project-mini-info">
              {{ postMiniInfo }}
            </div>
            <a :href="'/project/' + postId" class="read-more">Read more...</a>
          </div>
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
      postTitle: "Lorem ipsum",
      postId: "1",
      postImg: "../../assets/project.jpg",
      postMiniInfo: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    };
  },
};
</script>

<style>
.projects {
  position: absolute;
}
canvas {
  height: 100%;
  width: 100%;
}

.project-article {
  color: #f1dcff;
  margin-left: 18rem;
  margin-top: 2rem;
  display: flex;
  width: 800px;
  height: 140px;
  background: #202020;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  font-size: 1.2rem;
}

.project-content {
  margin-top: 1rem;
  margin-left: 1rem;
  display: flex;
}
.project-image {
  margin-top: 0.7rem;
  margin-left: 1rem
}
.project-text {
  margin-top: 0.4rem;
  margin-left: 2rem
}
.project-mini-info {
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