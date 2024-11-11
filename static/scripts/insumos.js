function modalCargarInsumo() {
    const altaModal = document.getElementById('register-modal');
    if (altaModal) {
        altaModal.style.display = 'block';
    }
}

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

function modalAgregarStock(){
    const stockModal = document.getElementById('stock-modal');
    if(stockModal){
        stockModal.style.display = 'block'
    }
}

function closeModals() {
    const closeButtons = document.querySelectorAll('.close');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const altaModal = document.getElementById('register-modal');
            const modifyModal = document.getElementById('modify-modal');
            const deleteModal = document.getElementById('delete-modal');
            const stockModal = document.getElementById('stock-modal');

            if (altaModal) {
                altaModal.style.display = 'none';
            }
            if (modifyModal) {
                modifyModal.style.display = 'none';
            }
            if (deleteModal) {
                deleteModal.style.display = 'none';
            }
            if (stockModal) {
                stockModal.style.display = 'none';
            }
        });
    });
}

closeModals();

document.addEventListener('DOMContentLoaded', function () {
    const jsonText = document.getElementById('choices').textContent;

    const unidadesChoices = JSON.parse(jsonText);

    const selectMedida = document.getElementById('medida');

    selectMedida.innerHTML = '';

    for (let key in unidadesChoices) {
        if (unidadesChoices.hasOwnProperty(key)) {
            let option = document.createElement('option');
            option.value = key;
            option.textContent = unidadesChoices[key];
            selectMedida.appendChild(option);
        }
    }
});