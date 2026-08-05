/* Admin portal scripts */
document.addEventListener('DOMContentLoaded', () => {
  // Confirm deletions
  document.querySelectorAll('.btn-delete').forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (!confirm('Are you sure you want to delete this item?')) {
        e.preventDefault();
      }
    });
  });
});
