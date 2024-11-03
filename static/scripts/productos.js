
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

// Función para mostrar el modal de registro de proveedor
function modalCargarProducto() {
    const productModal = document.getElementById('product-modal');
    if (productModal) {
        productModal.style.display = 'block';
    }
}

function mostrarModalModificar() {
    const modalEdit = document.getElementById("modify-modal");
    if(modalEdit){
        modalEdit.style.display = 'block';
    }
}


function mostrarModalEliminar() {
    const modalDelet = document.getElementById('delete-modal')
    if(modalDelet){
        modalDelet.style.display = 'block'
    }    
}

// para cerrar modales
function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            document.getElementById('product-modal').style.display = 'none';
            document.getElementById('modify-modal').style.display = 'none';
            document.getElementById('delete-modal').style.display = 'none';
        });
    });
}

closeModals();