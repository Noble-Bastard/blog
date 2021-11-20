<template>
  <menu class="main-menu">
    <div class="main-menu__top">
      <a class="logo" rel="home" href="/">
        <span>A&A</span>
      </a>
    </div>
    <nav class="main-menu_nav">
      <a rel="about" href="/about">About</a>
      <a rel="skills" href="/skills">My Skills</a>
      <a rel="work" href="/portfolio">Portfolio</a>
      <a rel="blog" href="blog">Blog</a>
      <a rel="contact" href="/contact">Contact</a>
    </nav>
    <ul class="social">
      <li>
        <a href="https://twitter.com/assabyn">
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="twitter"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            width="448"
            height="512"
            style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
          >
            <path
              d="M21.579 6.855c.14-.465 0-.806-.662-.806h-2.193c-.558 0-.813.295-.953.619 0 0-1.115 2.719-2.695 4.482-.51.513-.743.675-1.021.675-.139 0-.341-.162-.341-.627V6.855c0-.558-.161-.806-.626-.806H9.642c-.348 0-.558.258-.558.504 0 .528.79.65.871 2.138v3.228c0 .707-.127.836-.407.836-.743 0-2.551-2.729-3.624-5.853-.209-.607-.42-.852-.98-.852H2.752c-.627 0-.752.295-.752.619 0 .582.743 3.462 3.461 7.271 1.812 2.601 4.363 4.011 6.687 4.011 1.393 0 1.565-.313 1.565-.853v-1.966c0-.626.133-.752.574-.752.324 0 .882.164 2.183 1.417 1.486 1.486 1.732 2.153 2.567 2.153h2.192c.626 0 .939-.313.759-.931-.197-.615-.907-1.51-1.849-2.569-.512-.604-1.277-1.254-1.51-1.579-.325-.419-.231-.604 0-.976.001.001 2.672-3.761 2.95-5.04z"
              class=""
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a href="https://pl.linkedin.com/">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="448"
            height="512"
            style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
          >
            <path
              d="M20 3H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1zM8.339 18.337H5.667v-8.59h2.672v8.59zM7.003 8.574a1.548 1.548 0 1 1 0-3.096 1.548 1.548 0 0 1 0 3.096zm11.335 9.763h-2.669V14.16c0-.996-.018-2.277-1.388-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248h-2.667v-8.59h2.56v1.174h.037c.355-.675 1.227-1.387 2.524-1.387 2.704 0 3.203 1.778 3.203 4.092v4.71z"
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a href="https://www.facebook.com/">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="448"
            height="512"
            style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
          >
            <path
              d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l.002.001-.314 4.692c.46 0 .663-.211.921-.46l2.211-2.15 4.599 3.397c.848.467 1.457.227 1.668-.785l3.019-14.228c.309-1.239-.473-1.8-1.282-1.434z"
            ></path>
          </svg>
        </a>
      </li>
      <li>
        <a href="contact">
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="twitter"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            width="448"
            height="512"
            style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
          >
            <path
              d="M21 2H6a2 2 0 0 0-2 2v3H2v2h2v2H2v2h2v2H2v2h2v3a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1zm-8 2.999c1.648 0 3 1.351 3 3A3.012 3.012 0 0 1 13 11c-1.647 0-3-1.353-3-3.001 0-1.649 1.353-3 3-3zM19 18H7v-.75c0-2.219 2.705-4.5 6-4.5s6 2.281 6 4.5V18z"
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
  background-color: #202020;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  height: 100vh;
  position: fixed;
  left: 0;
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
  background: transparent;
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
  font-family: "Open Sans";
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
  -webkit-transition: color 0.3s, background-color 0.3s;
  -o-transition: color 0.3s, background-color 0.3s;
  transition: color 0.3s, background-color 0.3s;
}
details,
menu {
  display: block;
}
nav,
section {
  display: block;
}
a {
  text-decoration: none;
  background-color: transparent;
}
a:hover {
  color: #6f00cc;
}
.social li {
  text-align: center;
}
.social li a {
  padding: 2rem 7px;
}

/* svg:not(:root) {
  overflow: hidden;
}
svg {
  will-change: transform;
} */
.social svg {
  margin-top: 1rem;
  width: 1.5rem;
}
.social svg path {
  transition: fill 0.3s;
  fill: #909096;
}
.logo span {
  font-family: "WindsorC";
  color: #e6e6fa;
  margin-top: 0.4px;
  font-size: 3rem;
}
</style>