document.addEventListener('DOMContentLoaded', () => {
    const navMenu = document.getElementById('nav-menu'),
          navToggle = document.getElementById('nav-toggle'),
          navClose = document.getElementById('nav-close'),
          cart = document.getElementById('cart'),
          cartShop = document.getElementById('cart-shop'),
          cartClose = document.getElementById('cart-close'),
          login = document.getElementById('login'),
          loginButton = document.getElementById('login-button'),
          loginClose = document.getElementById('login-close'),
          accordionItems = document.querySelectorAll('.questions__item'),
          styleSwitcherToggle = document.querySelector('.style__switcher-toggler'),
          colorStyle = document.querySelector('.js-color-style'),
          themeColorsContainer = document.querySelector('.js-theme-colors');

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

    // Initialize Swipers
    var homeSwiper = new Swiper('.home-swiper', {
        spaceBetween: 30,
        loop: 'true',
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });

    var newSwiper = new Swiper('.new-swiper', {
        spaceBetween: 16,
        centeredSlides: true,
        slidesPerView: 'auto',
        loop: 'true',
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });

    // Scroll Up
    function scrollUp() {
        const scrollUp = document.getElementById('scroll-up');
        if (this.scrollY >= 350) {
            scrollUp.classList.add('show-scroll');
        } else {
            scrollUp.classList.remove('show-scroll');
        }
    }
    window.addEventListener('scroll', scrollUp);

    // Scroll Header Background Change
    function scrollHeader() {
        const header = document.getElementById('header');
        if (this.scrollY >= 50) {
            header.classList.add('scroll-header');
        } else {
            header.classList.remove('scroll-header');
        }
    }
    window.addEventListener('scroll', scrollHeader);

    // Accordion Functionality
    accordionItems.forEach((item) => {
        const accordionHeader = item.querySelector('.questions__header');
        accordionHeader.addEventListener('click', () => {
            const openItem = document.querySelector('.accordion-open');
            toggleItem(item);
            if (openItem && openItem !== item) {
                toggleItem(openItem);
            }
        });
    });

    function toggleItem(item) {
        const accordionContent = item.querySelector('.questions__content');
        if (item.classList.contains('accordion-open')) {
            accordionContent.removeAttribute('style');
            item.classList.remove('accordion-open');
        } else {
            accordionContent.style.height = accordionContent.scrollHeight + 'px';
            item.classList.add('accordion-open');
        }
    }

    // Style Switcher Toggle
    styleSwitcherToggle.addEventListener('click', () => {
        document.querySelector('.style__switcher').classList.toggle('open');
    });

    window.addEventListener('scroll', () => {
        if (document.querySelector('.style__switcher').classList.contains('open')) {
            document.querySelector('.style__switcher').classList.remove('open');
        }
    });

    // Theme Colors
    function themeColors() {
        themeColorsContainer.addEventListener('click', ({target}) => {
            if (target.classList.contains('js-theme-color-item')) {
                localStorage.setItem('color', target.getAttribute('data-js-theme-color'));
                setColors();
            }
        });

        function setColors() {
            let path = colorStyle.getAttribute('href').split('/');
            path = path.slice(0, path.length - 1);
            colorStyle.setAttribute('href', path.join('/') + '/' + localStorage.getItem('color') + '.css');

            const activeColorItem = document.querySelector('.js-theme-color-item.active');
            if (activeColorItem) {
                activeColorItem.classList.remove('active');
            }
            document.querySelector(`[data-js-theme-color="${localStorage.getItem('color')}"]`).classList.add('active');
        }

        if (localStorage.getItem('color') !== null) {
            setColors();
        } else {
            const defaultColor = colorStyle.getAttribute('href').split('/').pop().split('.').shift();
            document.querySelector(`[data-js-theme-color="${defaultColor}"]`).classList.add('active');
        }
    }

    themeColors();
});
