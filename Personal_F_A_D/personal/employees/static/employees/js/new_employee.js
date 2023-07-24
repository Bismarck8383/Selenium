
document.getElementById('createEmployeeForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let data = {
        'name': document.getElementById('name').value,
        'email': document.getElementById('email').value,
        'edad': document.getElementById('edad').value,
        'cargo': document.getElementById('cargo').value,
        'genero': document.getElementById('genero').value,
        'salario': document.getElementById('salario').value,
        'direccion': document.getElementById('direccion').value,
        'fecha_contratacion': document.getElementById('fecha_contratacion').value,
        'telefono': document.getElementById('telefono').value,
        'ciudad': document.getElementById('ciudad').value
    }

    fetch('http://127.0.0.1:8000/employees/add_employee/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if(data.id) {
            Swal.fire(
                'Creado correctamente!',
                'El empleado ha sido creado con éxito.',
                'success'
            )
            setTimeout(function(){
                window.location.href = 'http://127.0.0.1:8000/employees/list/';
            }, 3000);
        }
        else {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Ha ocurrido un error al crear el empleado.',
            })
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ha ocurrido un error al crear el empleado.',
        })
    });
});


/* Uso de promises */
const aplicarDescuento = new Promise((resolve, reject) => {
    const descuento = false;

    if (descuento) {
        resolve('Descuento aplicado');
    } else {
        reject('Descuento no aplicado'); // Corregido "Descuendo" a "Descuento"
    }
});

aplicarDescuento
        .then(respuesta => {
            console.log(respuesta);
        })
        .catch(error => {
            console.log(error);
        })




