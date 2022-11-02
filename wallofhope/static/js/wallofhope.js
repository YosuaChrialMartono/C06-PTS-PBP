function show(){
  $('#data').empty()
  $.ajax({
  url: "json/"
  }).done(data => {
  data.forEach(value => {
      let kartu = `<div class="cards" >
        
            <div class="card" >
              <h2 class="card-title"> ${value.fields.judul}</h2>
              <img src = "${value.fields.image}" id = "img_id" alt = "img"> </img>
              <p class="card-desc">${value.fields.deskripsi}</p>
              <br>
            </div>
            <a class="btn login_btn bg-primary text-white" style="color:blue;" href="delete/${value.pk}">Delete</a>
          </div>`
          
      $('#data').append(kartu)
  })
  })
}


$(document).ready(function ()  {
  myModal = new bootstrap.Modal('#exampleModal', {
  keyboard: false
  })

  $('#formm').submit(event => {
    event.preventDefault()
    
    $.ajax({
      url: "add/", 
      method: "POST", 
      data: {
        judul: $('#input_title').val(),
        deskripsi: $('#input_desc').val(),
        image: $('#input_image').val()
      },
      headers: {
        "X-CSRFToken": window.CSRF_TOKEN
      },

      success: function (json) {
        myModal.hide()
        show()

        document.getElementById("formm").reset();
      },

      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText); 
      }
    });
  })
})
show()