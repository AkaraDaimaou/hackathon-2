// JavaScript code

document.addEventListener('DOMContentLoaded', () => {
    const navMenu = document.getElementById('nav-menu');
    const navToggle = document.getElementById('nav-toggle');
    const navClose = document.getElementById('nav-close');
    const cart = document.getElementById('cart');
    const cartShop = document.getElementById('cart-shop');
    const cartClose = document.getElementById('cart-close');
    const login = document.getElementById('login');
    const loginButton = document.getElementById('login-button');
    const loginClose = document.getElementById('login-close');

    // Show Menu
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.add('show-menu');
        });
    }

    // Hide Menu
    if (navClose) {
        navClose.addEventListener('click', () => {
            navMenu.classList.remove('show-menu');
        });
    }

    // Show Cart
    if (cartShop) {
        cartShop.addEventListener('click', () => {
            cart.classList.add('show-cart');
        });
    }

    // Hide Cart
    if (cartClose) {
        cartClose.addEventListener('click', () => {
            cart.classList.remove('show-cart');
        });
    }

    // Show Login
    if (loginButton) {
        loginButton.addEventListener('click', () => {
            login.classList.add('show-login');
        });
    }

    // Hide Login
    if (loginClose) {
        loginClose.addEventListener('click', () => {
            login.classList.remove('show-login');
        });
    }

    // Swiper
    var homeSwiper = new Swiper(".home-swiper", {
        spaceBetween: 30,
        loop: 'true',
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    var newSwiper = new Swiper(".new-swiper", {
        spaceBetween: 16,
        centeredSlides: true,
        slidesPerView: 'auto',
        loop: 'true',
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // Scroll Up
    function scrollUp() {
        const scrollUp = document.getElementById('scroll-up');
        if (this.scrollY >= 200) scrollUp.classList.add('show-scroll');
        else scrollUp.classList.remove('show-scroll');
    }
    window.addEventListener('scroll', scrollUp);
});
