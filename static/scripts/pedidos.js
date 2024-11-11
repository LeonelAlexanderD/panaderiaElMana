

function modalRealizarPedido() {
    const pedidoModal = document.getElementById('pedido-modal');
    if (pedidoModal) {
        pedidoModal.style.display = 'block';
    };
}

function cancelarPedidoModal(){
    const cancelModal = document.getElementById('cancel-modal');
    if(cancelModal) {
        cancelModal.style.display = 'block';
    };
}

function aceptarPedidoModal() {
    const recepcionModal = document.getElementById('recepcion-modal');
    if (recepcionModal) {
        recepcionModal.style.display = 'block';
    };
}

function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const pedidoModal = document.getElementById('pedido-modal');
            const cancelModal = document.getElementById('cancel-modal');
            const recepcionModal = document.getElementById('recepcion-modal');

            if (recepcionModal) {
                recepcionModal.style.display = 'none';
            };

            if(cancelModal) {
                cancelModal.style.display = 'none';
            };

            if (pedidoModal) {
                pedidoModal.style.display = 'none';
            }
            
        });
    });
}

closeModals()





document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("id_proveedor").addEventListener("change", function () {
        let proveedorId = this.value;
        let insumosContainer = document.getElementById("insumos-container");

        // Limpia el contenedor de insumos al cambiar de proveedor
        insumosContainer.innerHTML = '';

        if (proveedorId) {
            let url = obtenerInsumosUrl.replace('0', proveedorId);

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    data.insumos.forEach(insumo => {
                        let insumoDiv = document.createElement('div');
                        insumoDiv.innerHTML = `
                            <label>${insumo.nombre}</label>
                            <input type="number" name="insumo_${insumo.id}" min="0" value="0" placeholder="Cantidad">
                        `;
                        insumosContainer.appendChild(insumoDiv);
                    });
                })
                .catch(error => console.error('Error:', error));
        }
    });
});