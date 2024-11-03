const carrito = [];
const carritoTotal = document.getElementById("cart-total-value");
const carritoItems = document.getElementById("cart-items");

function actualizarCarrito(){
    carritoItems.innerHTML = '';
    let total = 0;

    carrito.forEach((item, index) => {
        const itemDiv = document.createElement("div");
        itemDiv.className = "cart-item";

        itemDiv.innerHTML = `
        <img src="${item.imagen}" alt="${item.nombre}" class="product-image">
        <span>${item.nombre}</span>
        <button onclick="modificarCantidad(${index}, -1)">-</button>
        <span>${item.cantidad}</span>
        <button onclick="modificarCantidad(${index}, 1)">+</button>
        <span>${item.total.toFixed(2)}</span>
        <button onclick="eliminarProducto(${index})">Eliminar</button>
        `;

        carritoItems.appendChild(itemDiv);
        total += item.total;
    });

    carritoTotal.innerText = total.toFixed(2);
}

//agregar producto al carrito
function agregarAlCarrito(producto){
    const index = carrito.findIndex(item => item.id === producto.id);

    if(index !== -1) {
        carrito[index].cantidad++;
        carrito[index].total = carrito[index].cantidad * carrito[index].precio;
    } else{
        carrito.push({
            id: producto.id,
            nombre: producto.nombre,
            precio: producto.precio,
            imagen: producto.imagen,
            cantidad: 1,
            total: producto.precio
        });
    }
    actualizarCarrito();
}

//cantidad de producto en carrito
function modificarCantidad(index, cambio){
    if(carrito[index].cantidad + cambio > 0){
        carrito[index].cantidad += cambio;
        carrito[index].total = carrito[index].cantidad * carrito[index].precio;
    }
    actualizarCarrito();
}

//eliminar objeto del carrito
function eliminarProducto(index){
    carrito.splice(index, 1);
    actualizarCarrito();
}

// abrir payment-modal
document.getElementById("payment-button").onclick = function(){
    const resumenPedido = document.getElementById("resumen-pedido");
    const totalPedido = document.getElementById("total-pedido");

    resumenPedido.innerHTML = '';
    let total = 0;

    carrito.forEach(item => {
        const resumenItem = document.createElement("div");
        resumenItem.className = "summary-item";

        resumenItem.innerHTML = `
            <span>${item.nombre}</span>
            <span>Precio: $${item.precio.toFixed(2)}</span>
            <span>Cantidad: ${item.cantidad}</span>
            <span>Total: $${item.total.toFixed(2)} </span>
        `;

        resumenPedido.appendChild(resumenItem);
        total += item.total;
    });

    totalPedido.innerText = total.toFixed(2);
    document.getElementById("payment-modal").style.display = "block";
};


//cerrar modal
document.querySelector(".close").onclick = function(){
    document.getElementById("payment-modal").style.display = "none";
};

document.getElementById("cancel-payment").onclick = function(){
    document.getElementById("payment-modal").style.display = "none";
};


//mostrar carrito
const carritoShow = document.getElementById('cart-toggle');
const carritoHide = document.getElementById('hide-cart')
const CarritoMenu = document.getElementById('cart');

carritoShow.addEventListener('click', () => {
    CarritoMenu.classList.toggle('open');
    if (CarritoMenu.classList.contains('open')) {
        carritoShow.textContent = 'Ocultar';
    } else {
        carritoShow.textContent = 'Carrito';
    }
});

carritoHide.addEventListener('click', () => {
    CarritoMenu.classList.remove('open');
    carritoShow.textContent = 'Carrito';
});
