// Mock data (in a real application, this would come from your Django backend)
let ventas = [
    { id: 1, fecha_venta: "20-10-2024", tipo_venta: "contado", forma_pago: "efectivo", items: [{producto: "pan", precio_unitario: "$20", cantidad: "10"}, {producto: "galletas", precio_unitario: "$20", cantidad: "20"}], total: "$600", observacion: "gr"},
    { id: 2, fecha_venta: "20-10-2024", tipo_venta: "contado", forma_pago: "efectivo", items: [{producto: "torta", precio_unitario: "$2000", cantidad: "1"}, {producto: "tarta", precio_unitario: "$500", cantidad: "2"}], total: "$3000", observacion: "gr"},
    { id: 3, fecha_venta: "20-10-2024", tipo_venta: "contado", forma_pago: "efectivo", items: [{producto: "facturas", precio_unitario: "$200", cantidad: "10"}, {producto: "alfajor", precio_unitario: "$100", cantidad: "5"}], total: "$2500", observacion: "gr"},
];

function populateTable() {
    const tableBody = document.querySelector('#ventas-table tbody');
    tableBody.innerHTML = ''; 
    ventas.forEach(venta => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td data-label="Nro. Comprobante">${venta.id}</td>
            <td data-label="Fecha">${venta.fecha_venta}</td>
            <td data-label="Total">${venta.total}</td>
            <td data-label="Detalles">
                <button class="details-btn" data-id="${venta.id}">Ver</button>
            </td>
        `;
        tableBody.appendChild(row);
    });

    

    // evento boton mas detalles
    document.querySelectorAll('.details-btn').forEach(button => {
        button.addEventListener('click', function() {
            const id = parseInt(this.getAttribute('data-id'));
            openDetailsModal(id);
        });
    });
}



function openDetailsModal(id) {
    const venta = ventas.find(s => s.id === id);
    if (venta) {
        document.getElementById('comprobante').value = venta.id;
        document.getElementById('fecha-venta').value = venta.fecha_venta;
        document.getElementById('tipo-venta').value = venta.tipo_venta;
        document.getElementById('forma-pago').value = venta.forma_pago;
        const ventasItems = document.getElementById('items');
        ventasItems.innerHTML = '';
        venta.items.forEach(item => {
            const itemRow = document.createElement('div');
            itemRow.innerHTML = `
                <strong>Producto:</strong> ${item.producto} x <strong>${item.cantidad}</strong><br>
                <strong>Precio unitario:</strong> ${item.precio_unitario}<br>
                <strong>Total:</strong> $${(parseFloat(item.precio_unitario.replace('$', '').replace(',', '')) * item.cantidad).toFixed(2)}<br>
                <hr>
            `;
            ventasItems.appendChild(itemRow);
        });
        document.getElementById('total').value = venta.total;
        document.getElementById('observacion').value = venta.observacion;
        detailsModal.style.display = "block";
    }
}



// modal  detalles
const detailsModal = document.getElementById('details-modal');
const closeBtn = detailsModal.getElementsByClassName('close')[0];
const detailsForm = document.getElementById('details-form');

closeBtn.onclick = function() {
    detailsModal.style.display = "none";
}



// cerrar modal al tocar fuera
window.onclick = function(event) {    
    if (event.target == detailsModal) {
        detailsModal.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    populateTable();
});