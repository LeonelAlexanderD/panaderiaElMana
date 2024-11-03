// vista previa de la imagen que cargo en el form
document.getElementById('imagen').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const imagePreview = document.getElementById('image-preview');
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        }
        
        reader.readAsDataURL(file);
    } else {
        imagePreview.src = '#';
        imagePreview.style.display = 'none';
    }
});

//  modal de alta
function modalCargarProducto() {
    const productModal = document.getElementById('product-modal');
    if (productModal) {
        productModal.style.display = 'block';
    }
}

// modal agregar stock
function modalAgregarStock(){
    const stockModal = document.getElementById('stock-modal');
    if(stockModal){
        stockModal.style.display = 'block'
    }
}

// modal cambiar precio
function modalCambiarPRecio(){
    const precioModal = document.getElementById('precio-modal');
    if(precioModal){
        precioModal.style.display = 'block'
    }
}



//modal modificar
function mostrarModalModificar() {
    const modalEdit = document.getElementById("modify-modal");
    if(modalEdit){
        modalEdit.style.display = 'block';
    }
}

// modal eliminar
function mostrarModalEliminar() {
    const modalDelet = document.getElementById('delete-modal')
    if(modalDelet){
        modalDelet.style.display = 'block';
    }    
}



// para cerrar modales
function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productModal = document.getElementById('product-modal');
            const modifyModal = document.getElementById('modify-modal');
            const deleteModal = document.getElementById('delete-modal');
            const stockModal = document.getElementById('stock-modal');
            const precioModal = document.getElementById('precio-modal');

            if (precioModal) {
                precioModal.style.display = 'none'
            }

            if (productModal) {
                productModal.style.display = 'none';
            }
            if (modifyModal) {
                modifyModal.style.display = 'none';
            }
            if (deleteModal) {
                deleteModal.style.display = 'none';
            }
            if(stockModal){
                stockModal.style.display = 'none';
            }
        });
    });
}

closeModals();