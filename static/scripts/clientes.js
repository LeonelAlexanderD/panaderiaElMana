


// Función para mostrar el modal de registro de proveedor
function mostrarModalRegistro() {
    const modalRegistro = document.getElementById('register-modal');
    if (modalRegistro) {
        modalRegistro.style.display = 'block';
    }
}






function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const registerModal = document.getElementById('register-modal');
            

            if (registerModal) {
                registerModal.style.display = 'none'
            }
            
        });
    });
}

closeModals();