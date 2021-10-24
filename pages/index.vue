<template>
  <section class="section-home">
    <div class="main-title">
      <div class="main-text">
        <h1>
          AssaByn
          <p class="dev">Web-Developer.</p>
        </h1>
      </div>
      <p class="gray-text">Fullstack Developer, But more Backend..</p>
    </div>
    <div class="hero">
      <div class="hero-box">
        <img
          class="hero-box-img"
          width="300"
          height="300"
          src="../assets/11.png"
          alt=""
        />
      </div>
    </div>
  </section>
</template>

<script>
export default {
};
</script>

<style>
.section-home {
  height: 100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
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
p {
  color: #e6e6fa;
  margin-top: 0;
  /* margin-bottom: 1em; */
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
  border: 5px solid #8d8d8d;
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
  padding-top: 3px;
  animation: ava-bg 3s infinite alternate;
}
@keyframes ava-animate {
  0% {
    border-radius: 62% 38% 72% 28% / 67% 32% 68% 33%;
  }

  40% {
    border-radius: 37% 63% 53% 47% / 67% 32% 68% 33%;
  }

  60% {
    border-radius: 23% 77% 39% 61% / 78% 54% 46% 22%;
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
</style>