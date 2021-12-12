<template>
  <div class="home">
    <section class="section-home">
      <div class="main-title">
        <div class="main-text">
          <h1>
            AssaByn
            <p class="dev">Web-Developer.</p>
          </h1>
        </div>
        <p class="gray-text">Fullstack Developer, but more Backend..</p>
      </div>
      <div class="hero">
        <div class="hero-box">
          <img
            class="hero-box-img"
            width="400"
            height="400"
            src="../assets/original.jpg"
            alt=""
          />
        </div>
      </div>
    </section>
    <canvas></canvas>
  </div>
</template>

<script>
export default {};
</script>

<style>
.home {
  margin: 0;
  padding: 0;
}
canvas {
  height: 100%;
  width: 100%;
}
.section-home {
  position: absolute;
  overflow: hidden;
  user-select: none;
  display: flex;
  align-items: center;
  margin-top: 12rem;
  padding-left: 13rem;
}
.main-title {
  padding-left: 5rem;
  padding-bottom: 11rem;
}
.main-text {
  font-size: 3rem;
}
.gray-text {
  font-size: 1.6rem;
  letter-spacing: 2px;
  margin-top: 1.5rem;
  color: #8d8d8d;
}
.gray-text:hover {
  color: #e6e6fa;
}
p {
  color: #e6e6fa;
  margin-top: 0;
}
.hero {
  padding-left: 14rem;
  padding-bottom: 11rem;
}
.hero-box {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 300px;
  height: 300px;
  overflow: hidden;
  border: 5px solid #202020;
  background: linear-gradient(to bottom, #323232 0%, #3f3f3f 40%, #1c1c1c 150%),
    linear-gradient(
      to top,
      rgba(255, 255, 255, 0.4) 0%,
      rgba(0, 0, 0, 0.25) 200%
    );
  background-blend-mode: multiply;
  animation: ava-animate 5s infinite alternate;
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
}

.hero-box-img {
  /* padding-left: 4px; */
  padding-top: 5rem;
  animation: ava-bg 3s infinite alternate;
  /* transform: rotate(270deg); */
}
@keyframes ava-animate {
  0% {
    border-radius: 52% 48% 46% 54% / 50% 50% 50% 50%;
  }

  30% {
    border-radius: 51% 49% 50% 50% / 28% 50% 50% 72%;
  }

  60% {
    border-radius: 51% 49% 50% 50% / 50% 24% 76% 50%;
  }

  100% {
    border-radius: 18% 82% 24% 76% / 43% 54% 46% 57%;
  }
}

@keyframes ava-bg {
  from {
    backdrop-filter: hue-rotate(0);
  }

  to {
    backdrop-filter: hue-rotate(90deg);
  }
}
@media screen and (max-width: 1200px) {
  .hero {
    padding-left: 5rem;
  }
}
</style>