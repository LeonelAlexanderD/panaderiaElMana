
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


function agregarAlCarrito(productoId) {
    fetch('/agregar_al_carrito/',{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'producto_id': productoId, 'cantidad': 1 })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('cart-total-value').innerText = data.total;
    });
}

function generarComprobante(){
    let tipoPago = document.getElementById('sale-type').value;
    let medioPago = document.getElementById('payment-method').value;
    let tipoComprobante = document.getElementById('receipt-type').value;
    let observacion = document.getElementById('additional-observations').value;
    
    fetch('/generar_comprobante/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'tipo_de_venta': tipoPago,
            'forma_de_pago': medioPago,
            'tipo_comprobante': tipoComprobante,
            'observacion': observacion
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.msj){
            alert(data.msj);
        } else {
            alert(data.error);
        }
    });
}