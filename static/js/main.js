(function () {
  'use strict';

  // Mobile menu toggle
  const menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', function () {
      const isOpen = document.body.classList.toggle('nav-open');
      this.setAttribute('aria-expanded', String(isOpen));
    });
  }

  // Accordion
  document.querySelectorAll('.accordion__header').forEach(function (header) {
    header.addEventListener('click', function () {
      const expanded = this.getAttribute('aria-expanded') === 'true';
      // Close siblings in same accordion
      const accordion = this.closest('.accordion');
      if (accordion) {
        accordion.querySelectorAll('.accordion__header').forEach(function (h) {
          h.setAttribute('aria-expanded', 'false');
        });
      }
      this.setAttribute('aria-expanded', String(!expanded));
    });
  });

  // Hero slider
  const heroSection = document.querySelector('[data-slider="true"]');
  if (heroSection) {
    const slides = heroSection.querySelectorAll('.hero-slide');
    const dots = heroSection.querySelectorAll('.hero-dot');
    const prevBtn = heroSection.querySelector('.hero-prev');
    const nextBtn = heroSection.querySelector('.hero-next');
    const total = slides.length;
    if (total > 1) {
      let current = 0;
      let timer = null;

      function goTo(index) {
        slides[current].classList.remove('active');
        if (dots[current]) dots[current].classList.remove('active');
        current = ((index % total) + total) % total;
        slides[current].classList.add('active');
        if (dots[current]) dots[current].classList.add('active');
      }

      function next() { goTo(current + 1); }
      function prev() { goTo(current - 1); }

      function start() {
        if (timer) clearInterval(timer);
        timer = setInterval(next, 5000);
      }
      function stop() {
        if (timer) clearInterval(timer);
      }

      if (prevBtn) prevBtn.addEventListener('click', function () { stop(); prev(); start(); });
      if (nextBtn) nextBtn.addEventListener('click', function () { stop(); next(); start(); });
      dots.forEach(function (dot) {
        dot.addEventListener('click', function () {
          stop();
          goTo(parseInt(this.getAttribute('data-index'), 10));
          start();
        });
      });

      heroSection.addEventListener('mouseenter', stop);
      heroSection.addEventListener('mouseleave', start);
      start();
    }
  }

  // Carousel scroll buttons
  document.querySelectorAll('.carousel').forEach(function (carousel) {
    const track = carousel.querySelector('.carousel__track');
    const prev = carousel.querySelector('.carousel__prev');
    const next = carousel.querySelector('.carousel__next');
    if (!track) return;

    const scrollAmount = 320;

    if (prev) {
      prev.addEventListener('click', function () {
        track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
      });
    }
    if (next) {
      next.addEventListener('click', function () {
        track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
      });
    }
  });
})();
