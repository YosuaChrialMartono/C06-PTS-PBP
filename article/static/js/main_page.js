/*$('.btn-get-data').on('click', function () {
    $.ajax({
        url: $('.content-data').data('url'),
        type: 'GET',
        dataType: 'json',
        success: function (resp) {
            var html = '';
            //loop through json array
            $(resp).each(function (index, value) {
                html += `<div class="col-lg-3 col-md-5 col-sm-6 col-11">`
                html += `<div class="card mx-auto m-3" style="width: 18rem"> <div class="card-header"><b>`;
                html += value.fields.title;
                html += `</b></div><div class="card-body"><h6 class="card-subtitle mb-2 text-muted">`;
                html += value.fields.date;
                html += `</h6><p class="card-text">`
                html += value.fields.description
                html += "</p>"
                if (value.fields.is_finished == true) {
                    html += `<p class="card-text">Status : Finished</p>`
                }
                else {
                    html += `<p class="card-text">Status : Not Finished</p>`
                }
                html += `<button><a href="{}">Change Status</a></button></div></div></div>`
            })
            $(".content-data").empty()
            $(".content-data").html(html)
        },
        error: function (resp) {
            console.log('something went wrong');
        }
    });
});
$('#todolistform').on('submit', function (e) {

    $.ajax({
        method: 'POST',
        url: $('#todolistform').data('url'),
        data: {
            titlevalue: $('#tasktitle').val(),
            descriptionvalue: $('#description').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {

        },
    });
    $("#createTaskModal").modal('hide');
    refreshTodolist();
    return false
});
*/
async function getArticle() {
    return fetch("json/").then((res) => res.json())
}

async function refreshArticle() {
    document.getElementById("article_card").innerHTML = ""
    const article = await getArticle()
    let htmlString = ""
    article.forEach((item) => {
        let content = item.fields.content.slice(0, 300);
        let link = item.fields.title.replace(" ", "-");
        htmlString += `\n
                  <div class="card mx-auto m-3" style="width: 18rem"> 
                      <div class="card-header">
                          <b>${item.fields.title}</b>
                        </div>
                    <div class="card-body">
                        <p class="card-text">${content}</p> 
                    <a href="/article/json-by-page/${link}">Read more</a>
                    </div>
                    <div class="card-footer text-muted">
                    <h6 class="card-subtitle mb-2 text-muted">published at : ${item.fields.date}</h6>
                    </div>
                    </div>`
    })
    document.getElementById("article_card").innerHTML = htmlString
}
refreshArticle()