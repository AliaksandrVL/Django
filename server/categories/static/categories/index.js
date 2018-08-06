const Image = href => (
    `<div class="item__image" style="background-image: url(${ href })"></div>`
)

const Article = ({ id, name, image, content, created }) => (
    `<tr>
        <td><h3><a href = "articles/${ id }">${ name }</a></h3></td>
    </tr>
    <tr class="list">
        <td>${ Image(`/media/${ image }`) }<p>${ content }</p></td>
    </tr>
    <tr class="created">
        <td><p>Добавлено ${ created }</p></td>
    </tr>`
)

const renderData = res => {
    art_htm = res.data.results.map(Article).join('')

    container = document.getElementById('articles-list')
    container.innerHTML = art_htm
}