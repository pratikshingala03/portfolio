/* ============================================
   SMOOTH SCROLL LIBRARY
   ============================================ */

/**
 * Smooth Scroll Module
 * Provides enhanced smooth scrolling functionality with ease effects
 */

const SmoothScroll = (() => {
    // Configuration
    const config = {
        duration: 1000, // milliseconds
        easing: 'easeInOutCubic',
        offset: 0
    };

    /**
     * Easing functions for smooth animation
     */
    const easingFunctions = {
        linear: (t) => t,
        
        easeInQuad: (t) => t * t,
        easeOutQuad: (t) => t * (2 - t),
        easeInOutQuad: (t) => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t,
        
        easeInCubic: (t) => t * t * t,
        easeOutCubic: (t) => (--t) * t * t + 1,
        easeInOutCubic: (t) => t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * (t - 2)) * (2 * (t - 2)) + 1,
        
        easeInQuart: (t) => t * t * t * t,
        easeOutQuart: (t) => 1 - (--t) * t * t * t,
        easeInOutQuart: (t) => t < 0.5 ? 8 * t * t * t * t : 1 - 8 * (--t) * t * t * t,
        
        easeInQuint: (t) => t * t * t * t * t,
        easeOutQuint: (t) => 1 + (--t) * t * t * t * t,
        easeInOutQuint: (t) => t < 0.5 ? 16 * t * t * t * t * t : 1 + 16 * (--t) * t * t * t * t,
        
        easeInExpo: (t) => t === 0 ? 0 : Math.pow(2, 10 * t - 10),
        easeOutExpo: (t) => t === 1 ? 1 : 1 - Math.pow(2, -10 * t),
        easeInOutExpo: (t) => {
            return t === 0 ? 0 : t === 1 ? 1 : t < 0.5 ? Math.pow(2, 20 * t - 10) / 2 :
                (2 - Math.pow(2, -20 * t + 10)) / 2;
        },
        
        easeInCirc: (t) => 1 - Math.sqrt(1 - Math.pow(t, 2)),
        easeOutCirc: (t) => Math.sqrt(1 - Math.pow(t - 1, 2)),
        easeInOutCirc: (t) => {
            return t < 0.5 ? (1 - Math.sqrt(1 - Math.pow(2 * t, 2))) / 2 :
                (Math.sqrt(1 - Math.pow(-2 * t + 2, 2)) + 1) / 2;
        }
    };

    /**
     * Get easing function
     * @param {string} name - Name of easing function
     * @returns {function} Easing function
     */
    const getEasingFunction = (name) => {
        return easingFunctions[name] || easingFunctions.easeInOutCubic;
    };

    /**
     * Scroll to element
     * @param {string|HTMLElement} target - Target element or selector
     * @param {object} options - Scroll options
     */
    const scrollToElement = (target, options = {}) => {
        const settings = { ...config, ...options };
        
        let targetElement;
        if (typeof target === 'string') {
            targetElement = document.querySelector(target);
        } else {
            targetElement = target;
        }

        if (!targetElement) {
            console.warn('Target element not found:', target);
            return;
        }

        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - settings.offset;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        const duration = settings.duration;
        const easing = getEasingFunction(settings.easing);

        let start = null;

        const animation = (currentTime) => {
            if (start === null) start = currentTime;
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            const ease = easing(progress);

            window.scrollTo(0, startPosition + distance * ease);

            if (elapsed < duration) {
                requestAnimationFrame(animation);
            }
        };

        requestAnimationFrame(animation);
    };

    /**
     * Scroll to position
     * @param {number} position - Y position to scroll to
     * @param {object} options - Scroll options
     */
    const scrollToPosition = (position, options = {}) => {
        const settings = { ...config, ...options };
        const startPosition = window.pageYOffset;
        const distance = position - startPosition;
        const duration = settings.duration;
        const easing = getEasingFunction(settings.easing);

        let start = null;

        const animation = (currentTime) => {
            if (start === null) start = currentTime;
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            const ease = easing(progress);

            window.scrollTo(0, startPosition + distance * ease);

            if (elapsed < duration) {
                requestAnimationFrame(animation);
            }
        };

        requestAnimationFrame(animation);
    };

    /**
     * Scroll to top
     * @param {object} options - Scroll options
     */
    const scrollToTop = (options = {}) => {
        scrollToPosition(0, options);
    };

    /**
     * Initialize smooth scroll for all anchor links
     */
    const initializeAnchorLinks = () => {
        document.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                if (targetId && targetId !== '#') {
                    scrollToElement(targetId, { duration: 800 });
                }
            });
        });
    };

    /**
     * Public API
     */
    return {
        scrollToElement,
        scrollToPosition,
        scrollToTop,
        initializeAnchorLinks,
        config: (newConfig) => {
            Object.assign(config, newConfig);
        }
    };
})();

// Initialize on document ready
document.addEventListener('DOMContentLoaded', () => {
    SmoothScroll.initializeAnchorLinks();
});

// Expose globally for external use
window.SmoothScroll = SmoothScroll;
