/*$('#todolistform').on('submit', function (e) {

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
        let link = item.pk.replace(" ", "-");
        htmlString += `\n
                  <div class="card mx-auto m-3" style="width: 18rem"> 
                      <div class="card-header">
                          <b>${item.pk}</b>
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