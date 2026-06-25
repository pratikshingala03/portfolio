/* ============================================
   MAIN SCRIPT - Portfolio Interactivity
   ============================================ */

// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Close menu when nav link is clicked
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Active nav link highlighting
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Project card hover effects
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-8px)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// Download CV Button Analytics
document.querySelectorAll('[download]').forEach(link => {
    link.addEventListener('click', function() {
        console.log('CV downloaded at', new Date().toLocaleString());
    });
});

// Scroll to top button (optional future enhancement)
window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > 300) {
        // Could trigger a "scroll to top" button here
    }
});

// Initialize tooltips on external links
document.querySelectorAll('a[target="_blank"]').forEach(link => {
    link.setAttribute('rel', 'noopener noreferrer');
});

// Performance monitoring (optional)
window.addEventListener('load', () => {
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    console.log('Page load time:', pageLoadTime, 'ms');
});

// Accessibility: Keyboard navigation
document.addEventListener('keydown', (e) => {
    // Alt + H = Home
    if (e.altKey && e.key === 'h') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    // Alt + P = Projects
    if (e.altKey && e.key === 'p') {
        document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
    }
});

// Add loading state feedback
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function() {
        if (this.href && !this.href.startsWith('#')) {
            const originalText = this.textContent;
            // Optional: Add loading feedback
        }
    });
});

console.log('Portfolio website loaded successfully!');
