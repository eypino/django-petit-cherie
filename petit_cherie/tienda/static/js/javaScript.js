
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
//CARRITO DE COMPRAS
// Evento de clic para añadir productos al carrito
var addToCartButtons = document.getElementsByClassName('addToCart');
for (var i = 0; i < addToCartButtons.length; i++) {
  addToCartButtons[i].addEventListener('click', function () {
    var productId = this.getAttribute('data-product-id');
    addToCart(productId);
  });
}

// Función para añadir un producto al carrito
function addToCart(productId) {
  // Obtener el carrito de compras actual almacenado en la cookie
  var cart = getCartFromCookie();

  // Verificar si el producto ya está en el carrito
  var existingItem = cart.find(function (item) {
    return item.productId === productId;
  });

  if (existingItem) {
    // Si el producto ya está en el carrito, incrementar la cantidad
    existingItem.quantity++;
  } else {
    // Si el producto no está en el carrito, agregarlo con cantidad 1
    cart.push({ productId: productId, quantity: 1 });
  }

  // Guardar el carrito actualizado en la cookie
  saveCartToCookie(cart);

  // Actualizar la visualización del carrito en el modal
  updateCartModal();
}

// Función para obtener el carrito de compras almacenado en la cookie
function getCartFromCookie() {
  var cartCookie = getCookie('cart');
  if (cartCookie) {
    return JSON.parse(cartCookie);
  } else {
    return [];
  }
}

// Función para guardar el carrito de compras en la cookie
function saveCartToCookie(cart) {
  var cartJson = JSON.stringify(cart);
  setCookie('cart', cartJson, 7); // Guardar la cookie durante 7 días (ajustar según sea necesario)
}

// Función para obtener el valor de una cookie
function getCookie(name) {
  var cookieName = name + '=';
  var cookieArray = document.cookie.split(';');
  for (var i = 0; i < cookieArray.length; i++) {
    var cookie = cookieArray[i];
    while (cookie.charAt(0) === ' ') {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(cookieName) === 0) {
      return cookie.substring(cookieName.length, cookie.length);
    }
  }
  return '';
}

// Función para establecer el valor de una cookie
function setCookie(name, value, days) {
  var expires = '';
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = '; expires=' + date.toUTCString();
  }
  document.cookie = name + '=' + value + expires + '; path=/';
}

// Función para actualizar la visualización del carrito en el modal
function updateCartModal() {
  var cart = getCartFromCookie();
  var tableBody = document.getElementById('carritoTabla').getElementsByTagName('tbody')[0];
  var totalElement = document.getElementById('carritoTotal');
  var total = 0;

  // Limpiar la tabla del carrito
  while (tableBody.firstChild) {
    tableBody.firstChild.remove();
  }

  // Agregar los elementos del carrito a la tabla
  for (var i = 0; i < cart.length; i++) {
    var item = cart[i];
    var row = tableBody.insertRow(i);
    var indexCell = row.insertCell(0);
    var nameCell = row.insertCell(1);
    var priceCell = row.insertCell(2);
    var quantityCell = row.insertCell(3);

    indexCell.textContent = i + 1;
    nameCell.textContent = 'Product ' + item.productId;
    priceCell.textContent = '$10'; // Reemplazar con el precio real del producto
    quantityCell.textContent = item.quantity;

    total += 10 * item.quantity; // Reemplazar con el precio real del producto multiplicado por la cantidad
  }

  // Actualizar el total del carrito
  totalElement.textContent = 'Total: $' + total;
}

// Evento de clic para el botón de pago
var payButton = document.getElementById('payButton');
payButton.addEventListener('click', function () {
  var cart = getCartFromCookie();
  // Realizar el proceso de pago con el carrito actual
  console.log('Proceso de pago:', cart);
});

// Actualizar la visualización del carrito en el modal al cargar la página
updateCartModal();