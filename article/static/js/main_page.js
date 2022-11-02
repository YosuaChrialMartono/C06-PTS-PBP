function prev_page() {
    let current_page = document.getElementById("page").innerHTML.trim()
    let prev_page = parseInt(current_page) - 1
    let myurl = `?page=${prev_page}`
    return window.location.href = myurl
}

function next_page(){
    let current_page = document.getElementById("page").innerHTML.trim()
    let next_page = parseInt(current_page) + 1
    let myurl = `?page=${next_page}`
    return window.location.href = myurl
}


async function getArticle(page_num) {
    return fetch(`json/${page_num}`).then((res) => res.json())
}

async function refreshArticle() {
    let page = document.getElementById("page").innerHTML.trim()
    document.getElementById("article_card").innerHTML = ""
    const article = await getArticle(page)
    let htmlString = ""
    article.forEach((item) => {
        let content = item.fields.content.slice(0, 300);
        let link = item.pk.replace(" ", "-");
        htmlString += `\n
                  <div class="card col-3 m-3" style="width: 18rem"> 
                      <div class="card-header">
                          <b>${item.pk}</b>
                        </div>
                    <div class="card-body">
                        <p class="card-text">${content}</p> 
                    <a href="/article/articles/${link}">Read more</a>
                    </div>
                    <div class="card-footer text-muted">
                    <h6 class="card-subtitle mb-2 text-muted">published at : ${item.fields.date}</h6>
                    </div>
                    </div>`
    })
    document.getElementById("article_card").innerHTML = htmlString
}
refreshArticle()