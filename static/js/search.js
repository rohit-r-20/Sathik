/* Live instant search / filter helper */
function triggerSearch() {
  const input = document.getElementById('search-input');
  if (input) {
    const val = input.value.trim();
    const url = new URL(window.location.href);
    if (val) {
      url.searchParams.set('q', val);
    } else {
      url.searchParams.delete('q');
    }
    url.searchParams.delete('page');
    window.location.href = url.toString();
  }
}
