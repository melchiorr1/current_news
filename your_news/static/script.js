function add(button) {
    // get data and create FormData object
    let data = new FormData();

    let article = button.parentElement;
    data.append("title", article.children[0].innerText);
    data.append("url", article.children[0].children[0].href);
    data.append("author", article.children[1].innerText);
    data.append("img", article.children[2].src);

    // POST data
    fetch("/add", {
        method: 'POST',
        body: data,
    }).then(function (response) {
        window.location.href = `/`
    });
};

function remove(article_id){
    fetch('/delete' , {
        method: 'POST',
        body: JSON.stringify({ 'articleId': article_id })
    }).then(res => {
        window.location.href = '/readlater'
    })
}