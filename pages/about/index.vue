<template>
  <div class="home">
    <section class="section-home">
      <div class="main-title">
        <div class="main-text">
          <h1>
            Aibyn Askarbekuly
            <!-- <p class="dev">15 years old.</p> -->
          </h1>
        </div>
        <p class="gray-text">
          Father of one cat and one dog, beloved son and FullStack developer
          (but I'm more preferable to the backend).<br />
          I live in Almaty, I study in the 11th grade.<br />
          In the evenings I watch TV series / anime and drink tea. I was very
          fond of teas, as well as the process of drinking tea itself. <br />I
          am fond of the history of the world and politics. I love swimming and
          reading novels. And I read manhwa / manga.
        </p>
      </div>
      <div class="timedate">
        <p class="clock">{{ hour }}:{{ (minutes < 10) ? "0" + minutes : minutes }}</p>
      </div>
    </section>
    <canvas></canvas>
  </div>
</template>

<script>
export default {
  name: "about",
  data() {
    return {
      hour: 0,
      minutes: 0,
      myInterval: 0
    };
  },
  mounted() {
    this.myInterval = setInterval(this.clock, 1000);
  },
  methods: {
    clock: function () {
      var today = new Date();
      this.hour = today.getHours();
      this.minutes = today.getMinutes();
    },
  },
  beforeDestroy() {
    clearInterval(this.myInterval);
  },
};
</script>

<style>
.home {
  margin: 0;
  padding: 0;
}
canvas {
  height: 70rem;
  width: 100%;
}
.section-home {
  position: absolute;
  overflow: hidden;
  user-select: none;
  display: flex;
  align-items: center;
  margin-top: 17rem;
  padding-left: 13rem;
}
.main-title {
  padding-left: 5rem;
}
.main-text {
  font-size: 2.4rem;
  color: e6e6fa;
}
.gray-text {
  font-size: 1rem;
  margin-top: 1.5rem;
  color: white;
}
.gray-text:hover {
  color: #e6e6fa;
}
.timedate {
  font: "Dejavu Sans";
  margin-left: 5rem;
  padding-left: 3rem;
  font-size: 3rem;
  letter-spacing: 0.3rem;
  color: #fff;
  border-left: 5px solid #202020;
}
@media screen and (max-width: 1200px) {
  .timedate {
  font: "Dejavu Sans";
  margin-left: 3rem;
  padding-left: 1rem;
  font-size: 2rem;
  letter-spacing: 0.3rem;
  color: #fff;
  border-left: 5px solid #202020;
}
}
</style>