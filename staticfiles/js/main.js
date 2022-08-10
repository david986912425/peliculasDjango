var menu = document.querySelector('.menu-icon');
var navbar = document.querySelector('.navbar');
menu.onclick = () => {
  navbar.classList.toggle('open-menu');
  menu.classList.toggle('move');
};
window.onscroll = () => {
  navbar.classList.remove('open-menu');
  menu.classList.remove('move');
}

var swiper = new Swiper(".popular-content", {
  slidesPerView: 1,
  spaceBetween: 10,
  centeredSliders: true,
  autoplay: {
    delay:7500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    280:{
      slidesPerView: 1,
      spaceBetween: 10,
    },
    320:{
      slidesPerView: 2,
      spaceBetween: 10,
    },
    510:{
      slidesPerView: 2,
      spaceBetween: 10,
    },
    758:{
      slidesPerView: 3,
      spaceBetween: 15,
    },
    900:{
      slidesPerView: 4,
      spaceBetween: 10,
    },

  }
});