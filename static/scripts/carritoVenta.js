


// carrito
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


// Función para abrir el modal de comprobante
function abrirComprobanteModal() {    

    document.getElementById('payment-modal').style.display = 'block'; 
}

// Función para cerrar el modal de comprobante
function cerrarComprobanteModal() {
    document.getElementById('payment-modal').style.display = 'none'; 
}

// document.addEventListener('DOMContentLoaded', function () {
//     const jsonTipoVenta = document.getElementById('tipo_venta_choices').textContent;
//     const tipoVentasChoices = JSON.parse(jsonTipoVenta);
//     const selectTipoVenta = document.getElementById('sale-type');
    
//     selectTipoVenta.innerHTML = '';

//     for (let key in tipoVentasChoices) {
//         if (tipoVentasChoices.hasOwnProperty(key)) {
//             let option = document.createElement('option');
//             option.value = key;
//             option.textContent = tipoVentasChoices[key];
//             selectTipoVenta.appendChild(option);
//         }
//     }


//     const jsonTipoPago = document.getElementById('forma_pago_choices').textContent;
//     const tipoPagoChoices = JSON.parse(jsonTipoPago);
//     const selectTipoPago = document.getElementById('payment-method');
//     selectTipoPago.innerHTML = '';

//     for (let key in tipoPagoChoices) {
//         if(tipoPagoChoices.hasOwnProperty(key)){
//             let option = document.createElement('option');
//             option.value = key;
//             option.textContent = tipoPagoChoices[key];
//             selectTipoPago.appendChild(option);
//         }
//     }

//     const jsonTipoComprobante = document.getElementById('tipo_comprobante_choices').textContent;
//     const tipoComprobanteChoices = JSON.parse(jsonTipoComprobante);
//     const selectTipoComprobante = document.getElementById('receipt-type');
//     selectTipoComprobante.innerHTML = '';

//     for (let key in tipoComprobanteChoices) {
//         if(tipoComprobanteChoices.hasOwnProperty(key)){
//             let option = document.createElement('option');
//             option.value = key;
//             option.textContent = tipoComprobanteChoices[key];
//             selectTipoComprobante.appendChild(option);
//         }
//     }
// });


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




const closeModal = document.getElementsByClassName('close');
const cancelPayment = document.getElementById('cancel-payment');

closeModal.addEventListener('click', () => {
    paymentModal.style.display = 'none';
});

cancelPayment.addEventListener('click', () => {
    paymentModal.style.display = 'none';
});