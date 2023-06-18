$(function() {

  const token = 'IGQVJYNHRlb2dlRTd2OFl0blZAFcE15aWhSVzBOWlNxOEQzelJKaGs4ZA1ZAUZAEpYUVBycnphanhoelp2VVN2a0U3MVpDTVMyWE9YNmxNbk54LVFGUFBFZAGhXdWs1YmYzeXdLRW45WXFoUDk5YlNOTmhjNAZDZD';
  const url = `https://graph.instagram.com/me/media?fields=media_url,media_type,caption,permalink&refresh_access_token?grant_type=ig_refresh_token&&access_token=${token}`;

  $.get(url).then(function(response) {
    let datosJson = response.data;
    let contenido = '<div class="row" style="padding/left:5px">';
    let currentIndex = 0;

    for (let p = 0; p < 3; p++) {
      let feed = datosJson[p];
      let titulo = feed.caption !== null ? feed.caption : '';
      let tipo = feed.media_type;

      if (tipo === 'VIDEO') {
        contenido += '<div class="col-12 col-sm-6 col-md-4" style: "align-items: center;"><video style="width: 26rem;height: 28rem; transition: 2s;" controls><source src="' + feed.media_url + '" type="video/mp4"><center><p style="position: absolute; color:white; align-self: center; width:30%; padding-left: 0.5rem;">' + titulo + '</p></center></video></div>';
      } else if (tipo === 'IMAGE') {
        contenido += '<div class="col-12 col-sm-6 col-md-4" style: "align-items: center;"><img style="width: 26rem;height: 28rem; transition: 2s;" title="' + titulo + '" src="' + feed.media_url + '" onclick="window.open(\'' + feed.permalink + '\');"><center><p style="position: absolute; color:white; align-self: center; width:30%; padding-left: 0.5rem;">' + titulo + '</p></center></div>';
      }

      if (p === currentIndex) {
        currentIndex = p;
      }
    }

    contenido += '</div>';
    $('#insta').html(contenido);

    //chevron next
    $('#next').click(function() {
      if (currentIndex < datosJson.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      actualizarFeed();
    });

    //chevron prev
    $('#prev').click(function() {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = datosJson.length - 1;
      }
      actualizarFeed();
    });

    function actualizarFeed() {

        let contenido = '<div class="row" style="padding/left:5px">';
        for (let p = currentIndex; p < currentIndex + 3; p++) {
          let feed = datosJson[p % datosJson.length];
          let titulo = feed.caption !== undefined ? feed.caption : '';
          let tipo = feed.media_type;
  
          if (tipo === 'VIDEO') {
            contenido += '<div class="col-12 col-sm-6 col-md-4" style: "align-items: center;"><video style="width: 26rem;height: 28rem; transition: 2s;" controls><source src="' + feed.media_url + '" type="video/mp4"><center><p style="position: absolute; color:white; align-self: center; width:30%;; padding-left: 0.5rem;">' + titulo + '</p></center></video></div>';
          } else if (tipo === 'IMAGE') {
            contenido += '<div class="col-12 col-sm-6 col-md-4" style: "align-items: center;"><img style="width: 26rem;height: 28rem; transition: 2s;" title="' + titulo + '" src="' + feed.media_url + '" onclick="window.open(\'' + feed.permalink + '\');"><center><p style="position: absolute; color:white; align-self: center; width:30%;; padding-left: 0.5rem;">' + titulo + '</p></center></div>';
          }
        }
        contenido += '</div>';
        $('#insta').html(contenido);
      }
    });
  });


/*$(function(){
    const token = 'IGQVJXa2xyeWlWa1pUQm9OQjdtMVVDMFEtUFgxeGNQOHRZAekNyaVJsQVJDdUZANYWx6Ym5KN0E0Y1ZATNWZAOSVVvRnJvbVRaNDBfMWllTnBLQW8xSTliU09GNHJTNWxvaHpuNi1OM1JmVXFMM0pXRDRnWAZDZD';
    const url = `https://graph.instagram.com/me/media?fields=media_url,media_type,caption,permalink&refresh_access_token?grant_type=ig_refresh_token&&access_token=${token}`; 

    $.get(url).then(function(response){
        //console.log('retorno: ', response.data);
        let datosJson=response.data
        let contenido= '<div class="row" style="padding/left:5px">';

      for (let p=0; p<3;p++){
          let feed=datosJson[p];
          let titulo=feed.caption !== null ? feed.caption : '';
          let tipo = feed.media_type;
          if (tipo === 'VIDEO'){
              contenido+='<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4 image-overflow"><video style="width: 26rem;height: 28rem;" controls><source src="'+feed.media_url+'" type="video/mp4"><div class="opacity-hover"></div></video></div>';  
          }
          else if (tipo === 'IMAGE'){
              contenido+='<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4 image-overflow"><img style="width: 26rem;height: 28rem;" title="'+titulo+'" src="'+feed.media_url+'" onclick="window.open(\''+feed.permalink+'\');"><div class="opacity-hover"></div></div>';
          }
      }
      contenido+='</div>';
      $('#insta').html(contenido);
  })

    const token = 'IGQVJXa2xyeWlWa1pUQm9OQjdtMVVDMFEtUFgxeGNQOHRZAekNyaVJsQVJDdUZANYWx6Ym5KN0E0Y1ZATNWZAOSVVvRnJvbVRaNDBfMWllTnBLQW8xSTliU09GNHJTNWxvaHpuNi1OM1JmVXFMM0pXRDRnWAZDZD';
    const url = `https://graph.instagram.com/me/media?fields=media_url,media_type,caption,permalink&refresh_access_token?grant_type=ig_refresh_token&&access_token=${token}`;
  
    $.get(url).then(function(response) {
      let datosJson = response.data;
      let contenido = '<div class="row" style="padding/left:5px">';
      let currentIndex = 0;
  
      for (let p = 0; p < 3; p++) {
        let feed = datosJson[p];
        let titulo = feed.caption !== null ? feed.caption : '';
        let tipo = feed.media_type;
  
        if (tipo === 'VIDEO') {
          contenido += '<div class="col-12 col-sm-6 col-md-4"><video style="width: 26rem;height: 28rem; transition: 2s;" controls><source src="' + feed.media_url + '" type="video/mp4"><p style="position: absolute; color:white; align-self: center; width:26rem;">' + titulo + '</p></video></div>';
        } else if (tipo === 'IMAGE') {
          contenido += '<div class="col-12 col-sm-6 col-md-4"><img style="width: 26rem;height: 28rem; transition: 2s;" title="' + titulo + '" src="' + feed.media_url + '" onclick="window.open(\'' + feed.permalink + '\');"><p style="position: absolute; color:white; align-self: center; width:26rem;">' + titulo + '</p></div>';
        }
  
        if (p === currentIndex) {
          currentIndex = p;
        }
      }
  
      contenido += '</div>';
      $('#insta').html(contenido);
  
      //chevron next
      $('#next').click(function() {
        if (currentIndex < datosJson.length - 1) {
          currentIndex++;
        } else {
          currentIndex = 0;
        }
        actualizarFeed();
      });
  
      //chevron prev
      $('#prev').click(function() {
        if (currentIndex > 0) {
          currentIndex--;
        } else {
          currentIndex = datosJson.length - 1;
        }
        actualizarFeed();
      });
  
      function actualizarFeed() {

        let contenido = '<div class="row" style="padding/left:5px">';
        for (let p = currentIndex; p < currentIndex + 3; p++) {
          let feed = datosJson[p % datosJson.length];
          let titulo = feed.caption !== undefined ? feed.caption : '';
          let tipo = feed.media_type;
  
          if (tipo === 'VIDEO') {
            contenido += '<div class="col-12 col-sm-6 col-md-4"><video style="width: 26rem;height: 28rem;" controls><source src="' + feed.media_url + '" type="video/mp4"><p style="position: absolute; color:white; align-self: center; width:26rem;">' + titulo + '</p></video></div>';
          } else if (tipo === 'IMAGE') {
            contenido += '<div class="col-12 col-sm-6 col-md-4"><img style="width: 26rem;height: 28rem;" title="' + titulo + '" src="' + feed.media_url + '" onclick="window.open(\'' + feed.permalink + '\'); loading="lazy"><p style="position: absolute; color:white; align-self: center; width:26rem;">' + titulo + '</p></div>';
          }
        }
        contenido += '</div>';
        $('#insta').html(contenido);
      }
    });
  });


/*$(function(){
    const token = 'IGQVJXa2xyeWlWa1pUQm9OQjdtMVVDMFEtUFgxeGNQOHRZAekNyaVJsQVJDdUZANYWx6Ym5KN0E0Y1ZATNWZAOSVVvRnJvbVRaNDBfMWllTnBLQW8xSTliU09GNHJTNWxvaHpuNi1OM1JmVXFMM0pXRDRnWAZDZD';
    const url = `https://graph.instagram.com/me/media?fields=media_url,media_type,caption,permalink&refresh_access_token?grant_type=ig_refresh_token&&access_token=${token}`; 

    $.get(url).then(function(response){
        //console.log('retorno: ', response.data);
        let datosJson=response.data
        let contenido= '<div class="row" style="padding/left:5px">';

        for (let p=0; p<3;p++){
            let feed=datosJson[p];
            let titulo=feed.caption !== null ? feed.caption : '';
            let tipo = feed.media_type;
            if (tipo === 'VIDEO'){
                contenido+='<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4 image-overflow"><video style="width: 26rem;height: 28rem;" controls><source src="'+feed.media_url+'" type="video/mp4"><div class="opacity-hover"></div></video></div>';  
            }
            else if (tipo === 'IMAGE'){
                contenido+='<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4 image-overflow"><img style="width: 26rem;height: 28rem;" title="'+titulo+'" src="'+feed.media_url+'" onclick="window.open(\''+feed.permalink+'\');"><div class="opacity-hover"></div></div>';
            }
        }
        contenido+='</div>';
        $('#insta').html(contenido);
    })

})*/





/*const gallery = document.querySelector('.galeria');
const feed = document.querySelector('.contenedor-galeria');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');

const token = 'IGQVJWNE1jNnJ1WjIxWms5aVExeTlnR2M3eDkwVUpjUUZAheWQ4V1FCZAk1uWXZAVVVQ3dGZAVRHpuXzB3QnRybFcydHYzOEYxb1laUFo2NEZALdEhLNF81ME51NG5rNVlacHNvVVpPRlptbC1HWFRHbmVLQgZDZD';
const url = "https://graph.instagram.com/me/media?access_token"+token+"&fields=media_url,media_type,caption,permalink";

fetch(url)

  .then(res => res.json())
  .then(data => createHtml(data.data));

function createHtml(data) {
for (const img of data) {
  gallery.innerHTML += `
    <div class="image overflow">
      <img loading="lazy" src="${img.media_url}" alt="galeria">
      <div class="opacity-hover">
        <a href="${img.permalink}" class="caption">
          <p>
            ${img.caption.slice(0, 100)}
          </p>
        </a>
      </div>
    </div>`;
}

  .then(res => res.json())
  .then(data => createHtml(data.data));

function createHtml(data) {
  for (const img of data) {
    gallery.innerHTML += `
      <div class="image overflow">
        <img loading="lazy" src="${img.media_url}" alt="galeria">
        <div class="opacity-hover">
          <a href="${img.permalink}" class="caption">
            <p>
              ${img.caption.slice(0, 100)}
            </p>
          </a>
        </div>
      </div>`;
  }

}

next.addEventListener('click', moveGallery);
prev.addEventListener('click', moveGallery);

function moveGallery(e) {

if (e.target.id === 'next' || e.target.parentElement.id === 'next') {
  feed.scrollLeft += feed.offsetWidth;
} else {
  feed.scrollLeft -= feed.offsetWidth;
}
}*/


