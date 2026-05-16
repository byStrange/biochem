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
