
    

    // evento boton mas detalles
    document.querySelectorAll('.details-btn').forEach(button => {
        button.addEventListener('click', function() {
            const id = parseInt(this.getAttribute('data-id'));
            openDetailsModal(id);
        });
    });




function openDetailsModal(id) {
    
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

