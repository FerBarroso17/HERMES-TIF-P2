const url = 'http://127.0.0.1:3000/auth_bp/get_user/1';
document.getElementById("usuario").addEventListener("click", function() {
    fetch("/get_user/1", {
        method: "GET",  // Método de envío de la solicitud
        headers: {
          "Content-Type": "application/json",  // Tipo de contenido que se está enviando
        },
    })
    .then(function(response) {
        if (response.ok) {
            return response.json();
        }else{
        throw new Error("Error en la solicitud");
    }
    })
    .then(function(data) {
        // Manejar los datos del usuario recibidos del servidor
        if (data) {
          // Aquí puedes actualizar la vista con los datos del usuario
          const userDataDiv = document.getElementById("userData");
          userDataDiv.innerHTML = `<p>ID: ${data.usuario_id}</p>
                                    <p>Nombre: ${data.nombre_usuario}</p>
                                    <p>Correo Electrónico: ${data.correo_electronico}</p>`;
        } else {
          console.log("Usuario no encontrado");
        }
      })
      .catch(function(error) {
        // Manejar errores
        console.error(error);
      });
    });