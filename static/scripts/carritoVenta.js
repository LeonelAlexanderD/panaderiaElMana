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

// carrito
// function adjustQuantity(button, change) {
//     // Obtener el contenedor principal del producto en el carrito
//     const cartItemDiv = button.closest(".cart-item-div");

//     // Obtener el input de cantidad y su valor actual
//     const quantityInput = cartItemDiv.querySelector(".quantity-input");
//     let currentQuantity = parseInt(quantityInput.value);
//     const newQuantity = currentQuantity + change;

//     // Calcular la nueva cantidad y ajustar si está dentro del rango permitido
//     if (newQuantity >= 1) {
//         quantityInput.value = newQuantity;

//         // Actualizar el subtotal
//         const price = parseFloat(cartItemDiv.querySelector(".subtotal-value").dataset.price); 
//         const subtotal = newQuantity * price;
//         cartItemDiv.querySelector(".subtotal-value").textContent = subtotal.toFixed(2);

//         // Actualizar el valor en el formulario oculto para enviar la cantidad correcta
//         const productoId = cartItemDiv.querySelector("input[name='producto_id']").value;
//         fetch("{% url 'ventas:actualizar_o_eliminar_producto' %}", {
//             method: "POST",
//             headers:{
//                 "Content-Type": "aplicaction/x-www-form-urlencoded",
//                 "X-CSRFToken": "{{ csrf_token }}"
//             },
//             body: new URLSearchParams({
//                 "producto_id": productoId,
//                 "cantidad": newQuantity,
//                 "accion": "actualizar"
//             })
//         })
//         .then(response => response.json())
//         .then(data=>{
//             if(data.success){
//                 document.getElementById("cart-total-value").textContent = data.total_carrito;
//             }
//         })



//         const hiddenInput = document.createElement("input");
//         hiddenInput.type = "hidden";
//         hiddenInput.name = "cantidad";
//         hiddenInput.value = newQuantity;
//         cartItemDiv.querySelector("form[action*='actualizar_o_eliminar_producto']").appendChild(hiddenInput);

//         // Opción: Enviar automáticamente la cantidad actualizada al backend (opcional)
//         sendUpdatedQuantity(cartItemDiv, newQuantity);
//     }
// }