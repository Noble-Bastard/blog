<template>
  <div class="container">
    <Header/>
    <nuxt/>
  </div>
</template>

<script>
import Header from "../components/Header";
export default {
  components: {
    Header
  }
};
</script>


<style>
body {
    font-size: 1.6rem;
    line-height: 1.5;
    background: #1d1d1d;
    display: block;
    min-width: 320px;
    font-family: "Open Sans",sans-serif;
    color: #fff;
    /* margin: 0;
    padding: 0; */
    padding-left: 13rem;
    overflow-y: scroll;
    overflow-x: hidden;
    box-sizing: border-box;
    margin: 0;
}
</style>