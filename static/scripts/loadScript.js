function contentLoader() {
    fetch('/static/header-footer/header.html')
        .then(response => response.text()  )
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
            console.log('Cargando el header desde: /static/header-footer/header.html');
        })
        .catch(error => console.error('Error al cargar el header:', error));
        console.log('no cargo el header desde: /static/header-footer/header.html');


    // fetch('/static/header-footer/footer.html')
    //     .then(response => response.text())
    //     .then(data => {
    //         document.getElementById('footer-container').innerHTML = data;
    //         console.log('no el header desde: /static/header-footer/header.html');

    //     })
    //     .catch(error => console.log('Error al cargar el footer', error));
}

document.addEventListener('DOMContentLoaded', contentLoader);
