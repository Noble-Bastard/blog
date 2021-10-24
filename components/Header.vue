<template>
  <menu class="main-menu">
    <div class="main-menu__top">
      <a class="logo" rel="home" href="#">
        <span>AssaByn</span>
      </a>

    </div>
    <nav class="main-menu_nav">
      <a rel="about" href="">About</a>
      <a rel="skills" href="">My Skills</a>
      <a rel="work" href="">Work</a>
      <a rel="blog" href="">Blog</a>
      <a rel="contact" href="">Contact</a>
    </nav>
    <ul class="social">
      <li>
        <a href="https://twitter.com/assabyn" target="_blank">
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="twitter"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            class="svg-inline--fa fa-twitter fa-w-16 fa-5x"
          >
            <path
              fill="currentColor"
              d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"
              class=""
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a
          href="https://pl.linkedin.com/"
          target="_blank"
        >
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="linkedin-in"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 448 512"
            class="svg-inline--fa fa-linkedin-in fa-w-14 fa-5x"
          >
            <path
              fill="currentColor"
              d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
              class=""
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a
          href="https://www.facebook.com/"
          target="_blank"
        >
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="facebook-f"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 320 512"
            class="svg-inline--fa fa-facebook-f fa-w-10 fa-5x"
          >
            <path
              fill="currentColor"
              d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"
              class=""
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a href="contact" target="_blank">
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fas"
            data-icon="rss"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 448 512"
            class="svg-inline--fa fa-rss fa-w-14 fa-5x"
          >
            <path
              fill="currentColor"
              d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"
              class=""
            ></path>
          </svg>
        </a>
      </li></ul
  ></menu>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style>
.main-menu {
    width: 13rem;
    background-color: #181818;
    height: 100vh;
    position: fixed;
    lefT: 0;
    top: 0;
    right: auto;
    bottom: 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    z-index: 3;

    flex-direction: column;

    justify-content: space-between;

    align-items: center;
    margin: 0;
    padding: 0;
}
.main-menu__top {
    background: #000;
    width: 100%;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;
    padding: 2rem 0;
}
.main-menu_nav {
    width: 100%;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;
    border-top: 1px solid #282828;
}
.social {
    color: #909096;
    margin: 0;
    padding: 0;
    list-style: none;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
 
    flex-wrap: wrap;
    height: 20rem;
}
.logo {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    flex-direction: column;
 
    justify-content: center;

    align-items: center;
}

.main-menu__top > span {
    font-family: 'Open Sans';
    color: #a5a5a5;
    font-size: 1.2rem;
    margin-top: 1rem;
}
.main-menu_nav a {
    text-align: center;
    width: 100%;
    display: block;
    font-size: 1.3rem;
    color: #909096;
    line-height: 5rem;
    border-bottom: 1px solid #282828;
    -webkit-transition: color .3s,background-color .3s;
    -o-transition: color .3s,background-color .3s;
    transition: color .3s,background-color .3s;
}
details, menu {
    display: block;
}
nav, section {
    display: block;
}
a {
    
    color: #08fdd8;
    -webkit-transition: color .3s;
    -o-transition: color .3s;
    transition: color .3s;
    text-decoration: none;
    background-color: transparent;
}
a:hover {
    color: #019e86;
}
.social li {
    text-align: center;
}
.social li a {
    padding: 2rem 7px;
}
a {
    color: #08fdd8;
    -webkit-transition: color .3s;
    -o-transition: color .3s;
    transition: color .3s;
    text-decoration: none;
}
.logo svg {
    width: 6rem;
    height: auto;
}
svg:not(:root) {
    overflow: hidden;
}
svg {
    will-change: transform;
}
.social svg {
    width: 1.3rem;
}
.social svg path {
    -webkit-transition: fill .3s;
    -o-transition: fill .3s;
    transition: fill .3s;
    fill: #909096;
}
.logo span {
    font-family: 'Coolvetica';
    color: #E6E6FA;
    margin-top: 1px;
    font-size: 2.7rem;
}
.social svg.fa-facebook-f {
    width: 0.9rem;
}
</style>