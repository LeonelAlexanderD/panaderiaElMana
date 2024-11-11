


// Función para mostrar el modal de registro de proveedor
function mostrarModalRegistro() {
    const modalRegistro = document.getElementById('register-modal');
    if (modalRegistro) {
        modalRegistro.style.display = 'block';
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
// document.querySelectorAll('.close').addEventListener('click', () => {
//     document.getElementById('register-modal').style.display = 'none';
//     document.getElementById('modify-modal').style.display = 'none';
//     document.getElementById('delete-modal').style.display = 'none'
// });


function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const registerModal = document.getElementById('register-modal');
            const modifyModal = document.getElementById('modify-modal');
            const deleteModal = document.getElementById('delete-modal');

            if (registerModal) {
                registerModal.style.display = 'none'
            }

            if (modifyModal) {
                modifyModal.style.display = 'none';
            }
            if (deleteModal) {
                deleteModal.style.display = 'none';
            }
        });
    });
}

closeModals();