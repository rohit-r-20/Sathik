/* AJAX handler for enquiry / contact form submission */
function handleEnquirySubmit(event, formEl) {
  event.preventDefault();
  
  const submitBtn = formEl.querySelector('button[type="submit"]');
  const alertEl = formEl.querySelector('.form-alert');
  
  if (submitBtn) submitBtn.disabled = true;
  if (alertEl) {
    alertEl.style.display = 'none';
    alertEl.className = 'alert';
  }

  const formData = new FormData(formEl);

  fetch('/enquiry/submit', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    if (submitBtn) submitBtn.disabled = false;
    if (data.success) {
      if (alertEl) {
        alertEl.className = 'alert alert-success';
        alertEl.textContent = data.message;
        alertEl.style.display = 'block';
      } else {
        alert(data.message);
      }
      formEl.reset();
      setTimeout(() => {
        if (window.closeModal) window.closeModal('quote-modal');
      }, 2500);
    } else {
      const errText = data.errors ? Object.values(data.errors).join(', ') : (data.message || 'Submission failed');
      if (alertEl) {
        alertEl.className = 'alert alert-danger';
        alertEl.textContent = errText;
        alertEl.style.display = 'block';
      } else {
        alert(errText);
      }
    }
  })
  .catch(err => {
    if (submitBtn) submitBtn.disabled = false;
    alert('An error occurred. Please try again or contact us by phone.');
  });
}
