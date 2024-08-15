
// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = e.target.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Filtering products based on category
const categoryFilter = document.getElementById('category-filter');
const productGrid = document.getElementById('product-grid');

categoryFilter.addEventListener('change', () => {
    const selectedCategory = categoryFilter.value;
    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach((card) => {
        const cardCategory = card.classList[1]; // Assumes the second class is the category
        if (selectedCategory === 'all' || cardCategory === selectedCategory) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
});

