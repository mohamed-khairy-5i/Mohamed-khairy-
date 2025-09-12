#!/usr/bin/env python3
"""
Script to add mobile menu functionality to certificate pages
"""

import re
import os

def add_mobile_menu_to_certificate(filename):
    """Add mobile menu HTML and JavaScript to a certificate page"""
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add hamburger menu to nav (replace existing nav structure)
    nav_pattern = r'<nav class="flex items-center gap-6">\s*<a class="text-secondary.*?</nav>'
    nav_replacement = '''<nav class="hidden md:flex items-center gap-6">
          <a class="text-secondary text-sm font-medium hover:text-main transition-colors" href="certificates.html" data-lang-en="← Back to Certificates" data-lang-ar="← العودة للشهادات">← Back to Certificates</a>
        </nav>
        
        <!-- Mobile Hamburger Menu -->
        <div class="md:hidden">
          <div id="mobileMenuToggle" class="hamburger">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>'''
    
    content = re.sub(nav_pattern, nav_replacement, content, flags=re.DOTALL)
    
    # Add mobile menu HTML after header
    header_pattern = r'(</header>)\s*(<!-- Certificate Landing Page -->)'
    mobile_menu_html = '''      </header>

      <!-- Mobile Menu Overlay -->
      <div id="mobileMenuOverlay" class="fixed inset-0 bg-black bg-opacity-50 z-40 hidden md:hidden"></div>

      <!-- Mobile Menu -->
      <div id="mobileMenu" class="mobile-menu fixed top-0 left-0 h-full w-80 bg-main z-50 shadow-2xl md:hidden">
        <div class="flex flex-col h-full">
          <!-- Mobile Menu Header -->
          <div class="flex items-center justify-between p-6 border-b border-subtle">
            <div class="flex items-center gap-3">
              <div class="flex items-center justify-center w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg">
                <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0L19.2 12l-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/>
                </svg>
              </div>
              <span class="text-main font-bold text-lg">Mohamed Khairy</span>
            </div>
            <button id="closeMobileMenu" class="p-2 hover:bg-subtle rounded-lg transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Mobile Navigation Links -->
          <nav class="flex-1 px-6 py-4">
            <ul class="space-y-2">
              <li>
                <a href="index.html" class="mobile-nav-link block px-4 py-3 text-main font-medium transition-all duration-200" data-lang-en="Home" data-lang-ar="الرئيسية">Home</a>
              </li>
              <li>
                <a href="about.html" class="mobile-nav-link block px-4 py-3 text-secondary hover:text-main font-medium transition-all duration-200" data-lang-en="About" data-lang-ar="عنّي">About</a>
              </li>
              <li>
                <a href="projects.html" class="mobile-nav-link block px-4 py-3 text-secondary hover:text-main font-medium transition-all duration-200" data-lang-en="Projects" data-lang-ar="المشاريع">Projects</a>
              </li>
              <li>
                <a href="certificates.html" class="mobile-nav-link block px-4 py-3 text-main font-semibold bg-subtle rounded-lg transition-all duration-200" data-lang-en="Certificates" data-lang-ar="الشهادات">Certificates</a>
              </li>
              <li>
                <a href="contact.html" class="mobile-nav-link block px-4 py-3 text-secondary hover:text-main font-medium transition-all duration-200" data-lang-en="Contact" data-lang-ar="تواصل">Contact</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>

      <!-- Certificate Landing Page -->'''
    
    content = re.sub(header_pattern, mobile_menu_html, content, flags=re.DOTALL)
    
    # Add mobile menu JavaScript before closing script tag
    js_pattern = r'(document\.querySelectorAll\(\'\.animate-on-scroll\'\)\.forEach\(el => observer\.observe\(el\)\);)'
    js_addition = '''      document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
      
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
      });'''
    
    content = re.sub(js_pattern, js_addition, content)
    
    # Write the updated content back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename} with mobile menu functionality")

def main():
    certificate_files = [
        'certificate-social-media.html',
        'certificate-online-selling.html'
    ]
    
    for filename in certificate_files:
        if os.path.exists(filename):
            add_mobile_menu_to_certificate(filename)
        else:
            print(f"File {filename} not found")

if __name__ == "__main__":
    main()