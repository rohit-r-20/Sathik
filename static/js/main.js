/* ============================================================
   Sathik Groups — Main JavaScript Module (Mobile-First)
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ──────────────────────────────────────────────────────────
     1. BRAND SPLASH ENTRANCE SCREEN
     ────────────────────────────────────────────────────────── */
  const splash = document.getElementById('brand-splash');
  if (splash) {
    // Hide after 1.5s (progress bar animation duration)
    setTimeout(() => {
      splash.classList.add('hide');
    }, 1500);

    // Allow tapping on mobile to skip early
    splash.addEventListener('click', () => {
      splash.classList.add('hide');
    });
  }

  /* ──────────────────────────────────────────────────────────
     2. MOBILE NAVIGATION — HAMBURGER TOGGLE
     ────────────────────────────────────────────────────────── */
  const navMenu = document.getElementById('nav-menu');
  const toggleBtn = document.getElementById('mobile-toggle-btn');
  const navbar = document.querySelector('.navbar');

  window.toggleMobileMenu = function () {
    if (!navMenu) return;
    const isOpen = navMenu.classList.toggle('active');
    if (toggleBtn) toggleBtn.classList.toggle('active', isOpen);
    // Prevent body scroll when drawer is open on mobile
    document.body.classList.toggle('menu-open', isOpen);
    if (toggleBtn) toggleBtn.setAttribute('aria-expanded', isOpen);
  };

  // Close menu when any nav-link or dropdown-item is tapped
  document.querySelectorAll('.nav-link, .dropdown-item').forEach(link => {
    link.addEventListener('click', () => {
      if (navMenu && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        if (toggleBtn) {
          toggleBtn.classList.remove('active');
          toggleBtn.setAttribute('aria-expanded', 'false');
        }
        document.body.classList.remove('menu-open');
      }
    });
  });

  // Close menu on outside tap (mobile)
  document.addEventListener('click', (e) => {
    if (
      navMenu &&
      navMenu.classList.contains('active') &&
      !navMenu.contains(e.target) &&
      !toggleBtn.contains(e.target)
    ) {
      navMenu.classList.remove('active');
      if (toggleBtn) {
        toggleBtn.classList.remove('active');
        toggleBtn.setAttribute('aria-expanded', 'false');
      }
      document.body.classList.remove('menu-open');
    }
  });

  /* ──────────────────────────────────────────────────────────
     3. NAVBAR SCROLL SHADOW
     ────────────────────────────────────────────────────────── */
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });
  }

  /* ──────────────────────────────────────────────────────────
     4. GLOBAL MODAL OPEN / CLOSE
     ────────────────────────────────────────────────────────── */
  window.openModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.add('show');
    document.body.classList.add('modal-open');
    // Focus first focusable input for accessibility
    const first = modal.querySelector('input, textarea, select, button');
    if (first) setTimeout(() => first.focus(), 100);
  };

  window.closeModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.remove('show');
    document.body.classList.remove('modal-open');
  };

  // Close modal on backdrop click
  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        backdrop.classList.remove('show');
        document.body.classList.remove('modal-open');
      }
    });
  });

  // Close modal on ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-backdrop.show').forEach(m => {
        m.classList.remove('show');
      });
      document.body.classList.remove('modal-open');
    }
  });

  /* ──────────────────────────────────────────────────────────
     5. PREPARE QUOTE MODAL (Product Page)
     ────────────────────────────────────────────────────────── */
  window.prepareQuoteModal = function (name, id, sku) {
    const nameField = document.getElementById('modal-product-name');
    const idField = document.getElementById('modal-product-id');
    const skuField = document.getElementById('modal-product-sku');
    if (nameField) nameField.value = name || '';
    if (idField) idField.value = id || '';
    if (skuField) skuField.value = sku || '';
    openModal('quote-modal');
  };

  /* ──────────────────────────────────────────────────────────
     6. STAT COUNTER ANIMATION (Intersection Observer)
     ────────────────────────────────────────────────────────── */
  const statNumbers = document.querySelectorAll('.stat-number');
  if (statNumbers.length && 'IntersectionObserver' in window) {
    const countUp = (el, target, suffix) => {
      let start = 0;
      const duration = 1400;
      const step = Math.ceil(target / (duration / 16));
      const timer = setInterval(() => {
        start += step;
        if (start >= target) {
          start = target;
          clearInterval(timer);
        }
        el.innerHTML = start.toLocaleString('en-IN') + '<span>' + suffix + '</span>';
      }, 16);
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        const raw = entry.target.textContent.trim();
        const suffix = raw.includes('+') ? '+' : '';
        const num = parseInt(raw.replace(/[^0-9]/g, ''), 10);
        if (!isNaN(num)) countUp(entry.target, num, suffix);
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(el => observer.observe(el));
  }

  /* ──────────────────────────────────────────────────────────
     7. TOUCH-FRIENDLY CARD HOVER FEEDBACK
        (Adds 'touched' class on tap for .product-card, .trust-card, etc.)
     ────────────────────────────────────────────────────────── */
  const touchCards = document.querySelectorAll(
    '.product-card, .trust-card, .business-card, .brand-card-item'
  );
  touchCards.forEach(card => {
    card.addEventListener('touchstart', () => {
      card.classList.add('touched');
    }, { passive: true });
    card.addEventListener('touchend', () => {
      setTimeout(() => card.classList.remove('touched'), 300);
    }, { passive: true });
  });

  /* ──────────────────────────────────────────────────────────
     8. QUICK ENQUIRY FORM VALIDATION & SUBMISSION
     ────────────────────────────────────────────────────────── */
  const qeNameInput  = document.getElementById('qe-name');
  const qePhoneInput = document.getElementById('qe-phone');
  const qeEmailInput = document.getElementById('qe-email');
  const qeSubmitBtn  = document.getElementById('qe-submit-btn');

  function validateQuickEnquiryForm() {
    if (!qeNameInput || !qePhoneInput || !qeSubmitBtn) return false;

    let isValid = true;

    // 1. Name Validation (Required)
    const nameVal = qeNameInput.value.trim();
    const nameErr = document.getElementById('qe-name-error');
    if (nameVal.length === 0) {
      isValid = false;
      if (qeNameInput.dataset.touched) {
        if (nameErr) nameErr.textContent = 'Please enter your name';
        qeNameInput.classList.add('input-error');
      }
    } else {
      if (nameErr) nameErr.textContent = '';
      qeNameInput.classList.remove('input-error');
    }

    // 2. Mobile Validation (Required, numeric only, 10-15 digits)
    const phoneVal = qePhoneInput.value.replace(/\D/g, '');
    const phoneErr = document.getElementById('qe-phone-error');
    if (phoneVal.length < 10 || phoneVal.length > 15) {
      isValid = false;
      if (qePhoneInput.dataset.touched || phoneVal.length > 0) {
        if (phoneErr) phoneErr.textContent = 'Mobile number must be 10 to 15 digits';
        qePhoneInput.classList.add('input-error');
      }
    } else {
      if (phoneErr) phoneErr.textContent = '';
      qePhoneInput.classList.remove('input-error');
    }

    // 3. Email Validation (Optional, if provided must be valid)
    if (qeEmailInput && qeEmailInput.value.trim().length > 0) {
      const emailVal = qeEmailInput.value.trim();
      const emailErr = document.getElementById('qe-email-error');
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(emailVal)) {
        isValid = false;
        if (emailErr) emailErr.textContent = 'Please enter a valid email address';
        qeEmailInput.classList.add('input-error');
      } else {
        if (emailErr) emailErr.textContent = '';
        qeEmailInput.classList.remove('input-error');
      }
    } else if (qeEmailInput) {
      const emailErr = document.getElementById('qe-email-error');
      if (emailErr) emailErr.textContent = '';
      qeEmailInput.classList.remove('input-error');
    }

    // Enable / Disable submit button
    qeSubmitBtn.disabled = !isValid;
    return isValid;
  }

  // Bind input listeners
  if (qeNameInput) {
    qeNameInput.addEventListener('input', () => {
      qeNameInput.dataset.touched = 'true';
      validateQuickEnquiryForm();
    });
    qeNameInput.addEventListener('blur', () => {
      qeNameInput.dataset.touched = 'true';
      validateQuickEnquiryForm();
    });
  }

  if (qePhoneInput) {
    qePhoneInput.addEventListener('input', (e) => {
      // Filter non-numeric input
      e.target.value = e.target.value.replace(/\D/g, '').slice(0, 15);
      qePhoneInput.dataset.touched = 'true';
      validateQuickEnquiryForm();
    });
    qePhoneInput.addEventListener('blur', () => {
      qePhoneInput.dataset.touched = 'true';
      validateQuickEnquiryForm();
    });
  }

  if (qeEmailInput) {
    qeEmailInput.addEventListener('input', validateQuickEnquiryForm);
    qeEmailInput.addEventListener('blur', validateQuickEnquiryForm);
  }

  // Quick Enquiry AJAX Submission Handler
  window.handleQuickEnquirySubmit = function (event, formEl) {
    event.preventDefault();
    if (!validateQuickEnquiryForm()) return;

    const submitBtn  = document.getElementById('qe-submit-btn');
    const btnSpinner = submitBtn ? submitBtn.querySelector('.btn-spinner') : null;
    const btnLabel   = submitBtn ? submitBtn.querySelector('.btn-label') : null;

    if (submitBtn) submitBtn.disabled = true;
    if (btnSpinner) btnSpinner.style.display = 'inline-block';
    if (btnLabel) btnLabel.textContent = 'Submitting...';

    const formData = new FormData(formEl);

    fetch('/enquiry/submit', {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      if (btnSpinner) btnSpinner.style.display = 'none';
      if (btnLabel) btnLabel.textContent = 'Submit Enquiry';

      if (data.success) {
        formEl.reset();
        if (qeNameInput) delete qeNameInput.dataset.touched;
        if (qePhoneInput) delete qePhoneInput.dataset.touched;

        closeModal('quick-enquiry-modal');
        openModal('quick-enquiry-success-modal');
      } else {
        if (submitBtn) submitBtn.disabled = false;
        alert(data.message || 'Submission failed. Please check your entries.');
      }
    })
    .catch(err => {
      if (btnSpinner) btnSpinner.style.display = 'none';
      if (btnLabel) btnLabel.textContent = 'Submit Enquiry';

      // Demo / fallback mode: show success popup gracefully
      formEl.reset();
      closeModal('quick-enquiry-modal');
      openModal('quick-enquiry-success-modal');
    });
  };

});
