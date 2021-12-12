<template>
  <div class="home">
    <div class="contacts">
      <div class="leftside">
        <p class="contact-me">Write me</p>
        <input class="name" placeholder="Name" type="text" name="name" />
        <input class="email" placeholder="Email" type="email" name="email" />
        <textarea
          class="msg"
          placeholder="Message"
          type="text"
          name="msg"
        ></textarea>
        <form>
          <button class="send-msg" type="submit">Send message</button>
        </form>
      </div>
      <div class="rightside">
        <p class="contact-info">Contact Information</p>
        <span class="info-mini"
          >Im open for any suggestion or just to have a chat</span
        >
        <div class="social-contact">
          <div class="social-types social-vk">
            <a href="https://vk.com/assabyn">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="33"
                height="32"
                viewBox="0 0 22 27"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="M21.579 6.855c.14-.465 0-.806-.662-.806h-2.193c-.558 0-.813.295-.953.619 0 0-1.115 2.719-2.695 4.482-.51.513-.743.675-1.021.675-.139 0-.341-.162-.341-.627V6.855c0-.558-.161-.806-.626-.806H9.642c-.348 0-.558.258-.558.504 0 .528.79.65.871 2.138v3.228c0 .707-.127.836-.407.836-.743 0-2.551-2.729-3.624-5.853-.209-.607-.42-.852-.98-.852H2.752c-.627 0-.752.295-.752.619 0 .582.743 3.462 3.461 7.271 1.812 2.601 4.363 4.011 6.687 4.011 1.393 0 1.565-.313 1.565-.853v-1.966c0-.626.133-.752.574-.752.324 0 .882.164 2.183 1.417 1.486 1.486 1.732 2.153 2.567 2.153h2.192c.626 0 .939-.313.759-.931-.197-.615-.907-1.51-1.849-2.569-.512-.604-1.277-1.254-1.51-1.579-.325-.419-.231-.604 0-.976.001.001 2.672-3.761 2.95-5.04z"
                ></path>
              </svg>
            </a>
            <span class="social-id">VK: @assabyn</span>
          </div>
          <div class="social-types">
            <a href="whatsapp://send?text=Hello World!&phone=+77087639679">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="33"
                height="32"
                viewBox="0 0 22 27"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  fill-rule="evenodd"
                  cdivp-rule="evenodd"
                  d="M18.403 5.633A8.919 8.919 0 0 0 12.053 3c-4.948 0-8.976 4.027-8.978 8.977 0 1.582.413 3.126 1.198 4.488L3 21.116l4.759-1.249a8.981 8.981 0 0 0 4.29 1.093h.004c4.947 0 8.975-4.027 8.977-8.977a8.926 8.926 0 0 0-2.627-6.35m-6.35 13.812h-.003a7.446 7.446 0 0 1-3.798-1.041l-.272-.162-2.824.741.753-2.753-.177-.282a7.448 7.448 0 0 1-1.141-3.971c.002-4.114 3.349-7.461 7.465-7.461a7.413 7.413 0 0 1 5.275 2.188 7.42 7.42 0 0 1 2.183 5.279c-.002 4.114-3.349 7.462-7.461 7.462m4.093-5.589c-.225-.113-1.327-.655-1.533-.73-.205-.075-.354-.112-.504.112s-.58.729-.711.879-.262.168-.486.056-.947-.349-1.804-1.113c-.667-.595-1.117-1.329-1.248-1.554s-.014-.346.099-.458c.101-.1.224-.262.336-.393.112-.131.149-.224.224-.374s.038-.281-.019-.393c-.056-.113-.505-1.217-.692-1.666-.181-.435-.366-.377-.504-.383a9.65 9.65 0 0 0-.429-.008.826.826 0 0 0-.599.28c-.206.225-.785.767-.785 1.871s.804 2.171.916 2.321c.112.15 1.582 2.415 3.832 3.387.536.231.954.369 1.279.473.537.171 1.026.146 1.413.089.431-.064 1.327-.542 1.514-1.066.187-.524.187-.973.131-1.067-.056-.094-.207-.151-.43-.263"
                  class=""
                ></path>
              </svg>
            </a>
            <span class="social-id">WhatsApp: +7(708)-763-9679</span>
          </div>
          <!-- <div>
            <a href="https://www.divnkedin.com/in/aibyn-askarbekuly-0b8694213/">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="70"
                height="52"
                viewBox="0 0 70 52"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="M20 3H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1zM8.339 18.337H5.667v-8.59h2.672v8.59zM7.003 8.574a1.548 1.548 0 1 1 0-3.096 1.548 1.548 0 0 1 0 3.096zm11.335 9.763h-2.669V14.16c0-.996-.018-2.277-1.388-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248h-2.667v-8.59h2.56v1.174h.037c.355-.675 1.227-1.387 2.524-1.387 2.704 0 3.203 1.778 3.203 4.092v4.71z"
                ></path>
              </svg>
            </a>
          </div> -->
          <div class="social-types">
            <a href="https://t.me/bastardsama">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="33"
                height="32"
                viewBox="0 0 22 27"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l.002.001-.314 4.692c.46 0 .663-.211.921-.46l2.211-2.15 4.599 3.397c.848.467 1.457.227 1.668-.785l3.019-14.228c.309-1.239-.473-1.8-1.282-1.434z"
                ></path>
              </svg>
            </a>
            <span class="social-id">Telegram: @bastardSama</span>
          </div>
          <div class="social-types">
            <a href="tel:+77087639679">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="33"
                height="32"
                viewBox="0 0 22 27"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="M21 2H6a2 2 0 0 0-2 2v3H2v2h2v2H2v2h2v2H2v2h2v3a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1zm-8 2.999c1.648 0 3 1.351 3 3A3.012 3.012 0 0 1 13 11c-1.647 0-3-1.353-3-3.001 0-1.649 1.353-3 3-3zM19 18H7v-.75c0-2.219 2.705-4.5 6-4.5s6 2.281 6 4.5V18z"
                ></path>
              </svg>
            </a>
            <span class="social-id">Phone: +7(708)-763-9679</span>
          </div>
        </div>
      </div>
    </div>
    <canvas></canvas>
  </div>
</template>

<script>
export default {};
</script>

<style>
/*  */
.social-contact-info {
  position: absolute;
  margin-bottom: 3rem;
  color: #8d8d8d;
  font-size: 1rem;
}
.home {
  margin: 0;
  padding: 0;
}
canvas {
  height: 100%;
  width: 100%;
}
.contacts {
  position: absolute;
  display: flex;
  margin-top: 11rem;
  padding-left: 36rem;
}
.leftside {
  width: 400px;
  height: 600px;
  background: #2c2c2c;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  border-radius: 1rem 0 0 1rem;
}
.rightside {
  width: 400px;
  height: 600px;
  background: #191919;
  opacity: 0.8;
  filter: alpha(Opacity=80);
  border-radius: 0 1rem 1rem 0;
}
.contact-me {
  font-family: "WindsorC";
  margin-bottom: 0.3rem;
  margin-top: 1.8rem;
  color: #e6e6fa;
  font-size: 2rem;
  margin-left: 2rem;
}
.name,
.email,
.msg {
  width: 60%;
  border: none;
  border-bottom: 2px solid #191919;
  background: none;
  height: 40px;
  margin-left: 2rem;
  font-size: 16px;
  color: #8d8d8d;
  padding: 0 20px;
}
.email {
  margin-top: 1rem;
}
.msg {
  margin-top: 5rem;
  height: 30%;
}
.send-msg {
  margin-left: 2rem;
  margin-top: 3rem;
  border: 1.5px sodivd white;
  color: white;
  background: none;
  width: 150px;
  height: 40px;
}
.contact-info {
  font-family: "WindsorC";
  margin-bottom: 0.3rem;
  margin-top: 1.8rem;
  color: #e6e6fa;
  font-size: 2rem;
  margin-left: 2rem;
}
.info-mini {
  font-family: "WindsorC";
  margin-bottom: 3rem;
  margin-top: 1.8rem;
  color: #8d8d8d;
  font-size: 1.3rem;
  margin-left: 2rem;
}
.social-contact {
  font-size: 0.9rem;
  color: #909096;
  margin-top: 1rem;
  margin-left: 2rem;
}

.social-types {
  display: flex;
  align-items: center;
  margin-top: 2rem;
}
.social-vk {
  margin-top: 4rem;
}
.social-id {
  margin-left: 1rem;
  margin-bottom: 5px;
}

.social-contact svg path {
  transition: fill 0.3s;
  fill: #909096;
  margin-right: 1px;
}
@media screen and (max-width: 1200px) {
  .contacts {
    margin-left: -15rem;
  }
}
</style>