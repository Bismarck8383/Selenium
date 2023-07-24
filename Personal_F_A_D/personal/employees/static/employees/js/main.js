
let employee;
document.addEventListener("DOMContentLoaded", function() {
  let tarjetas = document.querySelectorAll('.tarjetas');
  let modalBody = document.querySelector('.modal-body');

  tarjetas.forEach(function(card) {
    card.addEventListener('click', function() {
     id_employee = card.getAttribute('id');
     console.log(`Clickeado en Id : ${id_employee}`);
     fetch(`/employees/id/${id_employee}`)
     .then(function(response) {
      return response.json();
    })
     .then(function(response) {
       employee = response;

          // Construir los detalles del empleado
       let details = `
       <ul>
       <li><b>Cargo:</b> ${employee.cargo}</li>
       <li><b>Name:</b> ${employee.name}</li>
       <li><b>Edad:</b> ${employee.edad}</li>
       <li><b>Telefono:</b> ${employee.telefono}</li>
       <li><b>Dirección:</b> ${employee.direccion}</li>
       <li><b>Ciudad:</b> ${employee.ciudad}</li>
       <li><b>Email:</b> ${employee.email}</li>
       <li><b>Salario:</b> ${employee.salario}</li>
       <li><b>Fecha Contratación:</b> ${employee.fecha_contratacion}</li>
       <li><b>Genero:</b> ${employee.genero}</li>
       </ul>
       `;

          // Asignar los detalles al cuerpo del modal
       modalBody.innerHTML = details;

          // Mostrar el modal
       $('#subsidyModal').modal('show');
     });
   });
  });
});


/*Delete Usuario*/
const swalWithBootstrapButtons = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
});


// Obtén una referencia al botón de "Eliminar"
let deleteButton = document.querySelector('#subsidyModal .btn-danger');

// Agrega el evento click al botón de "Eliminar"
deleteButton.addEventListener('click', function() {
  // Muestra la confirmación SweetAlert
  swalWithBootstrapButtons.fire({
    title: `¿Estás seguro que deseas Eliminar el registro de ${employee.name}?`,
    text: 'No podrás revertir esto.',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminarlo',
    cancelButtonText: 'No, cancelar',
    reverseButtons: true
  }).then(function(result) {
    // Si el usuario confirma la eliminación
    if (result.isConfirmed) {
      // Obtén el ID del empleado
      let idEmployee = employee.id; // Utiliza el ID almacenado previamente
      console.log(`id eliminado ${idEmployee}`);
      // Realiza la eliminación del registro utilizando fetch
      fetch(`/employees/delete/${idEmployee}`)
      .then(function(response) {
        if (response.status === 200) {
          return response.json();
          data = true;
        } else {
          throw new Error('Error al eliminar el registro');
        }
      })
      .then(function(data) {
        swalWithBootstrapButtons.fire(
          '¡Eliminado!',
          'El registro ha sido eliminado correctamente.',
          'success'
          );
        setTimeout(function(){
                window.location.href = 'http://127.0.0.1:8000/employees/list/';
            }, 3000);
      })
      .catch(function(error) {
        swalWithBootstrapButtons.fire(
          'Error',
          'Ha ocurrido un error al eliminar el registro.',
          'error'
          );
      });
    } else if (result.dismiss === Swal.DismissReason.cancel) {
      // Si el usuario cancela la eliminación
      // Muestra un mensaje de cancelación
      swalWithBootstrapButtons.fire(
        'Cancelado',
        'La eliminación ha sido cancelada.',
        'error'
        );
    }
  });
});





/*Editar usuario*/

// Agrega el evento click al botón de "Editar usuario"
document.getElementById('editUserButton').addEventListener('click', async function() {
  const { value: formValues, isConfirmed } = await Swal.fire({
   title: `Editar usuario ${employee.name}`,
   html: `
   <div class="contenedor_edit">
   <div class="fila" style="width:100%">
   <label for="swal-input1">Nombre</label>
   <input type="text" id="swal-input1" class="swal2-input" value="${employee.name}">
   </div>
   <div class="fila">
   <label for="swal-input2">Edad</label>
   <input type="text" id="swal-input2" class="swal2-input" value="${employee.edad}">
   </div>
   <div class="fila">
   <label for="swal-input3">Cargo</label>
   <input type="text" id="swal-input3" class="swal2-input" value="${employee.cargo}">
   </div>
   <div class="fila">
   <label for="swal-input4">Género</label>
   <input type="text" id="swal-input4" class="swal2-input" value="${employee.genero}">
   </div>
   <div class="fila">
   <label for="swal-input5">Salario</label>
   <input type="text" id="swal-input5" class="swal2-input" value="${employee.salario}">
   </div>
   <div class="fila">
   <label for="swal-input6">Correo</label>
   <input type="text" id="swal-input6" class="swal2-input" value="${employee.email}">
   </div>
   <div class="fila">
   <label for="swal-input7">Dirección</label>
   <input type="text" id="swal-input7" class="swal2-input" value="${employee.direccion}">
   </div>
   <div class="fila">
   <label for="swal-input8">Fecha Alta</label>
   <input type="text" id="swal-input8" class="swal2-input" value="${employee.fecha_contratacion}">
   </div>
   <div class="fila">
   <label for="swal-input9">Teléfono</label>
   <input type="text" id="swal-input9" class="swal2-input" value="${employee.telefono}">
   </div>
   <div class="fila">
   <label for="swal-input10">Teléfono</label>
   <input type="text" id="swal-input10" class="swal2-input" value="${employee.ciudad}">
   </div>
   </div>
   `,
   showCancelButton: true,
   confirmButtonText: 'Guardar',
   cancelButtonText: 'Cerrar',
   focusConfirm: false,
   width: '50%',
   position: 'center',
   preConfirm: () => {
    return [
      document.getElementById('swal-input1').value,
      document.getElementById('swal-input2').value,
      document.getElementById('swal-input3').value,
      document.getElementById('swal-input4').value,
      document.getElementById('swal-input5').value,
      document.getElementById('swal-input6').value,
      document.getElementById('swal-input7').value,
      document.getElementById('swal-input8').value,
      document.getElementById('swal-input9').value,
      document.getElementById('swal-input10').value,
      ];
  }
});

  if (isConfirmed) {
    if (formValues) {
      const name = formValues[0];
      const edad = parseInt(formValues[1]);  // convertir a int
      const cargo = formValues[2];
      const genero = formValues[3];
      const salario = parseFloat(formValues[4]);   // convertir a float
      const email = formValues[5];
      const direccion = formValues[6];
      const fecha_contratacion = formValues[7];
      const telefono = formValues[8];
      const ciudad = formValues[9];

      const idUsuario = parseInt(employee.id);

      const data = {
        name: name, // Debe ser "name" en lugar de "nombre"
        edad: edad,
        cargo: cargo,
        genero: genero,
        salario: salario,
        email: email,
        direccion: direccion,
        fecha_contratacion: fecha_contratacion,
        telefono: telefono,
        ciudad:ciudad
      };
      const replacer = (key, value) => {
        if (typeof value === 'number' && !Number.isInteger(value)) {
          return Number(value.toFixed(2));
        }
        return value;
      };

      const jsonData = JSON.stringify(data, replacer);
      console.log(`Id enviado ${idUsuario}`);
      
      
      fetch('/employees/update/'+ idUsuario, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: jsonData
      })
      .then(response => {
        if (response.status !== 200) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        Swal.fire('¡Editado!', 'Los datos del usuario han sido actualizados correctamente.', 'success');
        setTimeout(function(){
                window.location.href = 'http://127.0.0.1:8000/employees/list/';
            }, 3000);
      })

      .catch(error => {
        Swal.fire('Error', 'Ha ocurrido un error al editar el usuario.', 'error');
        console.log(error);
      });
    }
  }
});
