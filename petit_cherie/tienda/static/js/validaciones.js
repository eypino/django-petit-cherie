/* JS LOGIN*/
function checkBlankLogin(){
  if (document.getElementById('email').value =="") {
    alert('Por favor ingrese su correo');
    return false;
  }
}
/* JS LOGIN CONTRASEÑA/EMAIL ERRONEO  */
function checkBlankRegistro(){
  if (document.getElementById('email').value =="ejemplo@mail.com" && document.getElementById('password').value=="12345" ) {
    alert('Sesión iniciada exitosamente');
    return false;
  }else if (document.getElementById('email').value ==""){
 
  }
  else{
    alert('Email o contraseña errónea')
  }
}
/* JS Cambiar contraseña  */
function checkPass(){
  var contr1=document.getElementById('password1').value;
  var contr2=document.getElementById('password2').value;
  if (contr1==contr2 ) {
    alert('Contraseña modificada');
    return false;
  }
  else{
    alert('Contraseñas no coinciden')
  }
}

function checkEmail(){
  var email1=document.getElementById('email12').value;
  var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

  if (validEmail.test(email1)) {
    alert('Te enviamos un código revisa tu correo');
    return false;
  }else if (document.getElementById('email12').value ==""){
    alert('Por favor ingrese su correo');
    
  }
  else{
    alert('Correo no registrado')
  }
}

// 


///VALIDACION DE RUT
function validarRut(rut) {
  rut = rut.replace(/[^\dkK]/g, "").toUpperCase();
  if (rut.length < 8 || rut.length > 9) {
    return false;
  }
  var dv = rut.charAt(rut.length - 1);
  var rut_sin_dv = rut.substring(0, rut.length - 1);
  var suma = 0;
  var multiplo = 2;
  for (var i = rut_sin_dv.length - 1; i >= 0; i--) {
    suma += rut_sin_dv.charAt(i) * multiplo;
    multiplo++;
    if (multiplo == 8) {
      multiplo = 2;
    }
  }
  var resultado = suma % 11;
  var dv_calculado = 11 - resultado;
  if (dv_calculado == 11) {
    dv_calculado = "0";
  } else if (dv_calculado == 10) {
    dv_calculado = "K";
  } else {
    dv_calculado = dv_calculado.toString();
  }
  return dv_calculado === dv;
}
//VALIDACION DE CORREO
function validarCorreo(correo) {
  let valido = true;
  let mensaje = '';
  let expresion = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!expresion.test(correo)) {
    valido = false;
    mensaje = 'Por favor, ingrese un correo electrónico válido';
  }
  return {
    valido: valido,
    mensaje: mensaje
  };
}


///VALIDACION DE FORMULARIO DE REGISTRO



$('#botonCompletarReg').click(function() {
  
  let nombres = $('#nombreReg').val().trim();
  let apellidos = $('#apellidoReg').val().trim();
  let rut = $('#rutReg').val().trim();
  let correo = $('#correoReg').val().trim();
  let fechaNac = $('#fechaNac').val().trim();
  let fono = $('#fonoReg').val().trim();
  let direccion = $('#direccion').val().trim();
  let contrasena1 = $('#contrasena1').val().trim();
  let contrasena2 = $('#contrasena2').val().trim();
  let genero = $('#genero').val();
  let terminos = $('#terminos').is(':checked');

  let errores = [];

//NOMBRES
if (!nombres || nombres.length < 2) {
  errores.push({campo: '#nombreReg', mensaje: 'Por favor, ingrese un mínimo de dos caracteres'});
} else {
  $( '#nombreReg' ).removeClass('error');
}

$('#nombreReg').on('input', function() {
  let nombres = $(this).val().trim();
  if (!nombres) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error error">Por favor, ingrese su nombre</span>');
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});


// APELLIDOS
if (!apellidos || apellidos.length < 2) {
  errores.push({ campo: '#apellidoReg', mensaje: 'Por favor, ingrese un mínimo de dos caracteres para el apellido' });
} else {
  $('#apellidoReg').removeClass('error');
}

$('#apellidoReg').on('input', function() {
  let apellidos = $(this).val().trim();
  if (!apellidos) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">Por favor, ingrese su apellido</span>');
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});


//RUT

if (!rut) {
  errores.push({campo: '#rutReg', mensaje: 'Por favor, ingrese su RUT'});
} else if (!validarRut(rut)) {
  errores.push({campo: '#rutReg', mensaje: 'El RUT ingresado no es válido'});
} else {
  $( '#rutReg' ).removeClass('error');
}

$('#rutReg').on('input', function() {
  let rut = $(this).val().trim();
  if (!rut) {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
    return;
  }
  if (validarRut(rut)) {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  } else {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">El RUT ingresado no es válido</span>');
  }
});
//CORREO

if (!correo) {
  errores.push({campo: '#correoReg', mensaje: 'Por favor, ingrese su correo electrónico'});
} else {
  $( '#correoReg' ).removeClass('error');
}

$('#correoReg').keyup(function() {
  let correo = $(this).val().trim();
  let validacion = validarCorreo(correo);
  if (validacion.valido) {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  } else {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">' + validacion.mensaje + '</span>');
  }
});


//NACIMIENTO

if (!fechaNac) {
  errores.push({campo: '#fechaNac', mensaje: 'Por favor, ingrese su fecha de nacimiento'});
} else {
  $( '#fechaNac' ).removeClass('error');
}

$('#fechaNac').on('input', function() {
  let fecha = $(this).val();
  
  // Obtiene la fecha actual
  let fechaActual = new Date();
  
  // Crea una fecha con la fecha de nacimiento
  let fechaNacimiento = new Date(fecha);
  
  // Obtiene la diferencia en milisegundos entre la fecha actual y la fecha de nacimiento
  let diferenciaFechas = fechaActual - fechaNacimiento;
    
  // Convierte la diferencia en milisegundos a años
  let edad = Math.floor(diferenciaFechas / (1000 * 60 * 60 * 24 * 365));
  
  if (edad < 18) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error"style="color: red;">Debe ser mayor de 18 años para registrarse</span>');
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});


///FONO
function validarTelefonoChile(telefono) {
  // Eliminar espacios en blanco y guiones
  telefono = telefono.replace(/\s/g, '').replace(/-/g, '');

  // Verificar si está vacío
  if (telefono.length === 0) {
    return false;
  }

  // Verificar longitud y caracteres numéricos
  if (telefono.length !== 9 || isNaN(telefono)) {
    return false;
  }

  // Verificar prefijo
  var prefijo = telefono.substring(0, 2);
  if (prefijo !== '56') {
    return false;
  }

  // Verificar primer dígito del número
  var primerDigito = telefono.substring(2, 3);
  if (primerDigito !== '9') {
    return false;
  }

  return true;
}

var telefono = $('#fonoReg').val().trim();
if (telefono.length === 0) {
  errores.push({ campo: '#fonoReg', mensaje: 'Por favor, ingrese su número de teléfono' });
} else if (!validarTelefonoChile(telefono)) {
  errores.push({ campo: '#fonoReg', mensaje: 'Por favor, ingrese un número de teléfono válido de Chile' });
} else {
  $('#fonoReg').removeClass('error');
}

$('.mensaje-error').remove(); // Eliminar mensajes de error previos
errores.forEach(function(error) {
  $(error.campo).after('<span class="mensaje-error" style="color: red;">' + error.mensaje + '</span>');
});

if (errores.length === 0) {
  alert('Todos los campos están completos y correctos');
  window.location.href = '../index.html'; // redirigir a la página de inicio
}

if (errores.length > 0) {
  // Recorrer la lista de errores y aplicar estilos
  errores.forEach(function(error) {
    $(error.campo).addClass('error');
    $(error.campo).next('.mensaje-error').css('color', 'red');
  });
} else {
  // Si no hay errores, eliminar todos los estilos de error
  $('input').removeClass('error');
}

$('#fonoReg').on('input', function() {
  let fono = $(this).val().trim();

  if (!fono) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error" style="color: red;">Por favor, ingrese su número de teléfono</span>');
  } else if (fono.length < 8 || fono.length > 9) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error" style="color: red;">El número de teléfono debe tener 8 o 9 dígitos</span>');
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});


///DIRECCION
if (!direccion) {
  errores.push({campo: '#direccion', mensaje: 'Por favor, ingrese su dirección'});
} else {
  $( '#direccion' ).removeClass('error');
}

$('#direccion').on('input', function() {
  let direccion = $(this).val().trim();
  let longitudMinima = 5;
  let longitudMaxima = 100;

  if (direccion.length < longitudMinima) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after(`<span class="mensaje-error" style="color: red;">La dirección debe tener al menos ${longitudMinima} caracteres</span>`);
  } else if (direccion.length > longitudMaxima) {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after(`<span class="mensaje-error" style="color: red;">La dirección no debe tener más de ${longitudMaxima} caracteres</span>`);
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});



//CONTRASEÑAS
if (!contrasena1) {
  errores.push({campo: '#contrasena1', mensaje: 'Por favor, ingrese su contraseña'});
} else {
  $( '#contrasena1' ).removeClass('error');
}

if (!contrasena2) {
  errores.push({campo: '#contrasena2', mensaje: 'Por favor, ingrese su contraseña nuevamente'});
} else {
  $( '#contrasena2' ).removeClass('error');
}

if (contrasena1 !== contrasena2) {
  errores.push({campo: '#contrasena2', mensaje: 'Las contraseñas no coinciden'});
} else {
  $( '#contrasena2' ).removeClass('error');
}

// Validación de Contraseña 1
$('#contrasena1').on('input', function() {
  let contrasena1 = $(this).val().trim();
  
  // Verificar si la contraseña cumple con los requisitos
  if (contrasena1.length >= 8) {
    // La contraseña es válida, quitar el mensaje de error
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  } else {
    // La contraseña no cumple con los requisitos, agregar el mensaje de error
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">La contraseña debe tener al menos 8 caracteres</span>');
  }
});

// Validación de Contraseña 2
$('#contrasena2').on('input', function() {
  let contrasena1 = $('#contrasena1').val().trim();
  let contrasena2 = $(this).val().trim();
  
  // Verificar si la contraseña 2 es igual a la contraseña 1
  if (contrasena2 === contrasena1) {
    // Las contraseñas coinciden, quitar el mensaje de error
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  } else {
    // Las contraseñas no coinciden, agregar el mensaje de error
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">Las contraseñas no coinciden</span>');
  }
});

//GENERO

if (genero === 'Elija su género') {
  errores.push({campo: '#genero', mensaje: 'Por favor, seleccione su género'});
} else {
  $( '#genero' ).removeClass('error');
}

$('#genero').on('change', function() {
  let genero = $(this).val();
  
  if (genero == 'Elija su género') {
    $(this).addClass('error');
    $(this).next('.mensaje-error').remove();
    $(this).after('<span class="mensaje-error">Por favor, seleccione su género</span>');
  } else {
    $(this).removeClass('error');
    $(this).next('.mensaje-error').remove();
  }
});
//TERMINOS

if (!terminos) {
  errores.push({campo: '#terminos', mensaje: 'Por favor, acepte los términos y condiciones'});
} else {
  $( '#terminos' ).removeClass('error');
}

// Mostrar errores
$('.mensaje-error').remove(); // Eliminar mensajes de error previos
errores.forEach(function(error) {
  $(error.campo).after('<span class="mensaje-error" style="color: red; text-align: center;">' + error.mensaje + '</span>');
});

if (errores.length === 0) {
  alert('Todos los campos están completos y correctos');
  window.location.href = '../index.html'; // redirigir a la página de inicio
}

if (errores.length > 0) {
  // Recorrer la lista de errores y aplicar estilos
  errores.forEach(function(error) {
    $(error.campo).addClass('error');
    $(error.campo).next('.mensaje-error').css('color', 'red', 'text-align', 'center');
    $(error.campo).next('.error').css('color', 'red', 'text-align', 'center');
  });
} else {
  // Si no hay errores, eliminar todos los estilos de error
  $('input').removeClass('error');
}
});

///LIMPIAR CAMPOS
$('#botonBorrarReg').on('click', function() {
  $('input[type="text"]').val('');
  $('input[type="password"]').val('');
  $('input[type="email"]').val('');
  $('input[type="tel"]').val('');
  $('input[type="date"]').val('');
  $('select').prop('selectedIndex', 0);
  $('.mensaje-error').remove();
  $('.error').removeClass('error');
});
//TERMINOS Y CONDICIONES
$('#terminosTexto').click(function() {
  $('#modalTerminos').modal('show');
});
$(document).ready(function() {
  $('#botonIniciarSesion').click(function() {
    var email = $('#emailLogin').val();
    var password = $('#passwordLogin').val();
    var errores = [];

    // Verificar si el campo de correo electrónico está vacío o no es válido
    if (!email) {
      $('#emailError').text('Por favor ingrese su correo electrónico').css('color', 'red', 'text-align', 'center');
      $('#emailLogin').addClass('error');
      errores.push('email');
    } else if (!validarEmail(email)) {
      $('#emailError').text('Por favor ingrese un correo electrónico válido').css('color', 'red', 'text-align', 'center');
      $('#emailLogin').addClass('error');
      errores.push('email');
    } else {
      $('#emailError').text('');
      $('#emailLogin').removeClass('error');
    }
    
    // Verificar si el campo de contraseña está vacío o es menor a 8 caracteres
    if (!password) {
      $('#passwordError').text('Por favor ingrese su contraseña').css('color', 'red', 'text-align', 'center');
      $('#passwordLogin').addClass('error');
      errores.push('password');
    } else if (password.length < 8) {
      $('#passwordError').text('La contraseña debe tener al menos 8 caracteres').css('color', 'red', 'text-align', 'center');
      $('#passwordLogin').addClass('error');
      errores.push('password');
    } else {
      $('#passwordError').text('');
      $('#passwordLogin').removeClass('error');
    }
    
    // Si hay errores, prevenir el envío del formulario
    if (errores.length > 0) {
      return false;
    }
  });
});

// Función para validar un correo electrónico
function validarEmail(email) {
  var re = /\S+@\S+\.\S+/;
  return re.test(email);
}




