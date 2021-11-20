<template>
  <div class="portfolio">
    <header>
      <h1 class="glow">
        <span>S</span><span>O</span><span>O</span><span>N</span><span>.</span
        ><span>.</span><span>.</span>
      </h1>
    </header>
    <canvas></canvas>
  </div>
</template>

<script>
export default {};
</script>

<style>
canvas {
  width: 100%;
  height: 100%;
}
header {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  padding-top: 13rem;
}

header h1 {
  color: white;
  font-size: 10rem;
  letter-spacing: 1rem;
  /* text-shadow: 0 0 10px #fff, 0 0 10px #fff, 0 0 10px #fff; */
}

.glow span {
  transition: all 0.3s;
}

.glow span:hover {
  text-shadow: 0 0 10px #06f9fb, 0 0 30px #06f9fb, 0 0 80px #06f9fb;
  color: #fff;
}
</style>