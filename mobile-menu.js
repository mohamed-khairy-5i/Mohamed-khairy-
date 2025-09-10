// Shared Mobile Menu JavaScript
document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu functionality
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const closeMobileMenu = document.getElementById('closeMobileMenu');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
  
  const openMobileMenu = () => {
    mobileMenu.classList.add('open');
    mobileMenuOverlay.classList.remove('hidden');
    mobileMenuToggle.classList.add('active');
    document.body.style.overflow = 'hidden';
  };
  
  const closeMobileMenuFunc = () => {
    mobileMenu.classList.remove('open');
    mobileMenuOverlay.classList.add('hidden');
    mobileMenuToggle.classList.remove('active');
    document.body.style.overflow = 'auto';
  };
  
  mobileMenuToggle?.addEventListener('click', openMobileMenu);
  closeMobileMenu?.addEventListener('click', closeMobileMenuFunc);
  mobileMenuOverlay?.addEventListener('click', closeMobileMenuFunc);
  
  // Close mobile menu when clicking on a link
  document.querySelectorAll('#mobileMenu a').forEach(link => {
    link.addEventListener('click', closeMobileMenuFunc);
  });
  
  // Close mobile menu with Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
      closeMobileMenuFunc();
    }
  });
});