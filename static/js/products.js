/* Product gallery thumbnail switcher & quote modal handler */
function switchMainImage(thumbEl, url) {
  const mainImg = document.getElementById('main-product-image');
  if (mainImg) {
    mainImg.src = url;
  }
  document.querySelectorAll('.thumb-frame').forEach(el => el.classList.remove('active'));
  if (thumbEl) thumbEl.classList.add('active');
}

function prepareQuoteModal(productName, productId, sku) {
  const nameEl = document.getElementById('modal-product-name');
  const idEl = document.getElementById('modal-product-id');
  const skuEl = document.getElementById('modal-product-sku');

  if (nameEl) nameEl.value = productName || '';
  if (idEl) idEl.value = productId || '';
  if (skuEl) skuEl.value = sku || '';

  if (window.openModal) {
    window.openModal('quote-modal');
  }
}
