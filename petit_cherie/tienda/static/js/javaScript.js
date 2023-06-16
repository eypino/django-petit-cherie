
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

