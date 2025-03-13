"use strict";

// Combine everything into one DOMContentLoaded event listener,
// so all logic properly initializes once the DOM is ready.

document.addEventListener('DOMContentLoaded', () => {
  // 1) Responsive Navigation Toggle
  const navToggle = document.getElementById('nav-toggle');
  const siteNav = document.getElementById('site-nav');
  if (navToggle && siteNav) {
    navToggle.addEventListener('click', () => {
      const navUl = siteNav.querySelector('ul');
      navUl.classList.toggle('show-nav');
      // Optional small animation
      if (navUl.classList.contains('show-nav')) {
        navUl.style.animation = 'slideDown 0.3s ease';
      }
    });
  }

  // 2) Modal Overlay for Delete Confirmation
  const deleteLinks = document.querySelectorAll('.delete-link');
  const modalOverlay = document.getElementById('modal-overlay');
  const confirmBtn = document.getElementById('confirm-delete');
  const cancelBtn = document.getElementById('cancel-delete');

  let deleteUrl = null;

  if (deleteLinks.length > 0 && modalOverlay) {
    deleteLinks.forEach(link => {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        deleteUrl = link.href;
        showModalOverlay(modalOverlay);
      });
    });
  }

  if (confirmBtn) {
    confirmBtn.addEventListener('click', () => {
      if (deleteUrl) {
        window.location.href = deleteUrl;
      } else {
        // Slight shake animation if there's no valid URL
        modalOverlay.querySelector('.modal-box').classList.add('shake');
        setTimeout(() => {
          modalOverlay.querySelector('.modal-box').classList.remove('shake');
        }, 400);
      }
    });
  }

  if (cancelBtn) {
    cancelBtn.addEventListener('click', () => {
      hideModalOverlay(modalOverlay);
      deleteUrl = null;
    });
  }

  // 3) Scroll-to-Top Button
  const scrollTopBtn = createScrollTopButton();
  document.body.appendChild(scrollTopBtn);

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }
  });

  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
  });

  // 4) Clickable row logic for .clickable-row
  const rows = document.querySelectorAll('.clickable-row');
  rows.forEach(row => {
    row.addEventListener('click', (evt) => {
      // If user clicked an <a> (like End Trip or another link), skip.
      if (evt.target.closest('a')) {
        return;
      }
      const url = row.dataset.href;  // e.g. "/trips/1/"
      if (url) {
        window.location.href = url;
      }
    });
  });
});

/**
 * Show the modal overlay with a fade-in effect.
 * @param {Element} overlay - The modal overlay element.
 */
function showModalOverlay(overlay) {
  overlay.classList.add('active');
  const modalBox = overlay.querySelector('.modal-box');
  if (modalBox) {
    modalBox.classList.remove('shake');
  }
}

/**
 * Hide the modal overlay with a fade-out effect.
 * @param {Element} overlay - The modal overlay element.
 */
function hideModalOverlay(overlay) {
  overlay.classList.remove('active');
}

/**
 * Create a scroll-to-top button with default styling.
 * @returns {Element} The newly created button element.
 */
function createScrollTopButton() {
  const btn = document.createElement('button');
  btn.classList.add('scroll-top-btn');
  btn.textContent = '↑ Top';
  return btn;
}


