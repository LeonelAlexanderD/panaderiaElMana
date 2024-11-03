// const products = [
//     { id: 1, name: "Sourdough Bread", category: "breads", description: "Artisanal sourdough bread", price: 5.99, image: "/placeholder.svg?height=200&width=200" },
//     { id: 2, name: "Chocolate Chip Cookies", category: "biscuits", description: "Classic chocolate chip cookies", price: 3.99, image: "/placeholder.svg?height=200&width=200" },
//     { id: 3, name: "Croissant", category: "sweet-doughs", description: "Buttery French croissant", price: 2.49, image: "/placeholder.svg?height=200&width=200" },
//     { id: 4, name: "Red Velvet Cake", category: "cakes", description: "Delicious red velvet cake with cream cheese frosting", price: 24.99, image: "/placeholder.svg?height=200&width=200" },
// ];


// Function to create product cards
// function createProductCard(product) {
//     const card = document.createElement('div');
//     card.className = 'product-card';
//     card.innerHTML = `
//         <img src="${product.image}" alt="${product.name}" class="product-image">
//         <h4 class="product-name">${product.name}</h4>
//         <p class="product-description">${product.description}</p>
//         <p class="product-price">$${product.price.toFixed(2)}</p>
//         <button class="add-to-cart" data-id="${product.id}">Agregar</button>
//     `;
//     return card;
// } 

// Populate products
// products.forEach(product => {
//     const container = document.getElementById(`${product.category}-products`);
//     if (container) {
//         container.appendChild(createProductCard(product));
//     }
// });

// Shopping cart functionality


const cartToggle = document.getElementById('cart-toggle');
const cartElement = document.getElementById('cart');
const cartItems = document.getElementById('cart-items');
const cartTotal = document.getElementById('cart-total');
const paymentButton = document.getElementById('payment-button');
const paymentModal = document.getElementById('payment-modal');
const closeModal = document.getElementsByClassName('close')[0];
const paymentForm = document.getElementById('payment-form');
const cancelPayment = document.getElementById('cancel-payment');
const hideCartButton = document.getElementById('hide-cart');

cartToggle.addEventListener('click', () => {
    cartElement.classList.toggle('open');
    if (cartElement.classList.contains('open')) {
        cartToggle.textContent = 'Hide Cart';
    } else {
        cartToggle.textContent = 'Show Cart';
    }
});

hideCartButton.addEventListener('click', () => {
    cartElement.classList.remove('open');
    cartToggle.textContent = 'Show Cart';
});

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('add-to-cart')) {
        const productId = parseInt(e.target.getAttribute('data-id'));
        addToCart(productId);
    }
});

// function addToCart(productId) {
//     const product = products.find(p => p.id === productId);
//     const existingItem = cart.find(item => item.id === productId);

//     if (existingItem) {
//         existingItem.quantity++;
//     } else {
//         cart.push({ ...product, quantity: 1 });
//     }

//     updateCart();
// }

// function updateCart() {
//     cartItems.innerHTML = '';
//     let total = 0;

//     cart.forEach(item => {
//         const itemElement = document.createElement('div');
//         itemElement.className = 'cart-item';
//         itemElement.innerHTML = `
//             <div class="cart-item-info">
//                 <h4>${item.name}</h4>
//                 <p>$${item.price.toFixed(2)} x ${item.quantity}</p>
//             </div>
//             <div class="cart-item-quantity">
//                 <button class="decrease-quantity" data-id="${item.id}">-</button>
//                 <input type="number" value="${item.quantity}" min="1" data-id="${item.id}">
//                 <button class="increase-quantity" data-id="${item.id}">+</button>
//             </div>
//             <button class="remove-item" data-id="${item.id}">Remove</button>
//         `;
//         cartItems.appendChild(itemElement);

//         total += item.price * item.quantity;
//     });

//     cartTotal.textContent = `Total: $${total.toFixed(2)}`;
// }

// cartItems.addEventListener('click', (e) => {
//     const id = parseInt(e.target.getAttribute('data-id'));
//     if (e.target.classList.contains('decrease-quantity')) {
//         updateQuantity(id,   -1);
//     } else if (e.target.classList.contains('increase-quantity')) {
//         updateQuantity(id, 1);
//     } else if (e.target.classList.contains('remove-item')) {
//         removeItem(id);
//     }
// });

// cartItems.addEventListener('change', (e) => {
//     if (e.target.tagName === 'INPUT') {
//         const id = parseInt(e.target.getAttribute('data-id'));
//         const newQuantity = parseInt(e.target.value);
//         setQuantity(id, newQuantity);
//     }
// });

// function updateQuantity(id, change) {
//     const item = cart.find(item => item.id === id);
//     if (item) {
//         item.quantity = Math.max(1, item.quantity + change);
//         updateCart();
//     }
// }

// function setQuantity(id, quantity) {
//     const item = cart.find(item => item.id === id);
//     if (item) {
//         item.quantity = Math.max(1, quantity);
//         updateCart();
//     }
// }

function removeItem(id) {
    const index = cart.findIndex(item => item.id === id);
    if (index !== -1) {
        cart.splice(index, 1);
        updateCart();
    }
}

paymentButton.addEventListener('click', () => {
    paymentModal.style.display = 'block';
    updateOrderSummary();
});

closeModal.addEventListener('click', () => {
    paymentModal.style.display = 'none';
});

cancelPayment.addEventListener('click', () => {
    paymentModal.style.display = 'none';
});

window.addEventListener('click', (e) => {
    if (e.target === paymentModal) {
        paymentModal.style.display = 'none';
    }
});

function updateOrderSummary() {
    const orderSummary = document.getElementById('order-summary');
    const orderTotal = document.getElementById('order-total');
    let total = 0;

    orderSummary.innerHTML = '';
    cart.forEach(item => {
        const itemElement = document.createElement('p');
        itemElement.textContent = `${item.name} x ${item.quantity}: $${(item.price * item.quantity).toFixed(2)}`;
        orderSummary.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    orderTotal.textContent = `Total: $${total.toFixed(2)}`;
}

paymentForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Here you would typically send the form data to your Django backend
    // For this example, we'll just log the data to the console
    console.log('Payment form submitted');
    console.log('Sale Date:', document.getElementById('sale-date').value);
    console.log('Sale Type:', document.getElementById('sale-type').value);
    console.log('Payment Method:', document.getElementById('payment-method').value);
    console.log('Receipt Type:', document.getElementById('receipt-type').value);
    console.log('Receipt Number:', document.getElementById('receipt-number').value);
    console.log('Additional Observations:', document.getElementById('additional-observations').value);
    console.log('Order:', cart);

    // Clear the cart and close the modal
    cart.length = 0;
    updateCart();
    paymentModal.style.display = 'none';
    alert('Thank you for your purchase!');
});