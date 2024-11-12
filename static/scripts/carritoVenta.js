setTimeout(function() {
    const alertContainer = document.querySelector('.alert-container');
    if (alertContainer) {
        alertContainer.style.transition = "opacity 1s";
        alertContainer.style.opacity = "0";
        setTimeout(() => alertContainer.style.display = "none", 1000);
    }
}, 3000); 


// carrito
const carritoShow = document.getElementById('cart-toggle');
const carritoHide = document.getElementById('hide-cart');
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


// Función para abrir el modal de comprobante
function abrirComprobanteModal() {    

    document.getElementById('payment-modal').style.display = 'block'; 
}

// Función para cerrar el modal de comprobante
function cerrarComprobanteModal() {
    document.getElementById('payment-modal').style.display = 'none'; 
}



//Funcion de arriba pero reformulada con gpt- funciona, no tocar-
function selectComprobantes(preId, selectId) {
    const preElement = document.getElementById(preId);
    const selectElement = document.getElementById(selectId);

    try {
        const options = JSON.parse(preElement.textContent);
        for (const key in options) {
            if (options.hasOwnProperty(key)) {
                const option = document.createElement('option');
                option.value = key;
                option.textContent = options[key];
                selectElement.appendChild(option);
            }
        }
    } catch (error) {
        console.error(`no se puede mostrar por alguna razon, revisa`, error);
    }
}


document.addEventListener("DOMContentLoaded", function() {
    selectComprobantes("tipo_venta_choices", "tipo_de_venta");
    selectComprobantes("forma_pago_choices", "forma_de_pago");
    selectComprobantes("tipo_comprobante_choices", "tipo_comprobante");
});




document.addEventListener('DOMContentLoaded', () => {
    const closeModal = document.getElementsByClassName('close')[0]; // Asegúrate de que el elemento exista
    const cancelPayment = document.getElementById('cancel-payment');
    const modalPago = document.getElementById('payment-modal');

    function cerrarModalPago() {
        if (modalPago) {
            modalPago.style.display = 'none';
        }
    }

    if (closeModal) {
        closeModal.addEventListener('click', cerrarModalPago);
    } else {
        console.error("No se encontró el elemento con la clase 'close'");
    }

    if (cancelPayment) {
        cancelPayment.addEventListener('click', cerrarModalPago);
    } else {
        console.error("No se encontró el botón con el id 'cancel-payment'");
    }
});


function mostrarTotalCarrito() {
    let total = 0;

    // Sumamos cada subtotal de los productos en el carrito
    document.querySelectorAll('.subtotal-value').forEach(subtotalElement => {
        total += parseFloat(subtotalElement.textContent);
    });

    // Mostramos el total en el carrito
    document.getElementById('cart-total').textContent = total.toFixed(2);

    // Mostramos el total en el modal de comprobante
    document.getElementById('total-pedido').textContent = `${total.toFixed(2)}`;
}

// Llamamos a la función cuando se carga la página
document.addEventListener('DOMContentLoaded', mostrarTotalCarrito);