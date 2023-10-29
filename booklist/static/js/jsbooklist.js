async function getBooks() {
    return fetch(getBookJsonUrl).then((res) => res.json());
}
async function getBuku() {
    return fetch(getBukuJsonUrl).then((res) => res.json());
}
async function refreshBook() {
    document.getElementById("book_table").innerHTML = "";
    const products = await getBooks();
    let htmlString = `<thead>
        <th>Title</th>
        <th>Language</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Year</th>
        <th>Subject</th>
        <th>Bookshelves</th>
        <th></th>
    </thead>`;

    for (const item of products) {
        htmlString += `\n<tbody>
        <td>${item.fields.title}</td>
        <td>${item.fields.language}</td>
        <td>${item.fields.first_name}</td>
        <td>${item.fields.last_name}</td>
        <td>${item.fields.year}</td>
        <td>${item.fields.subjects}</td>
        <td>${item.fields.bookshelves}</td>
        <td><input type="button" onclick="deleteBook(${item.pk})" value="Delete"></td>
        </tbody>`;
    };
    document.getElementById("book_table").innerHTML = htmlString;
    document.getElementById("button_add").onclick = addBook;
}
async function refreshBuku() {
    const products = await getBuku();
    let htmlString = ``;
    for (const item of products) {
        htmlString += `
        <option value="${item.pk}">${item.fields.title}</option>
        `
    };
    document.getElementById("buku").innerHTML = htmlString;
}
refreshBook();
refreshBuku();
function addBook() {
    fetch(addBookJsonUrl, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(response => {
        if (response.status === 201) {
            return response.text()
        } else if (response.status === 404) {
            return "Resource Not Found."
        } else {
            return "Request failed with status code " + response.status
        }
    }).then(data => {
        alert(data)
        refreshBook()
        refreshBuku()
    }).catch(error => {
        console.error("Request failed", error)
    });
    document.getElementById("form").reset()
    return false
    };
function deleteBook(id) {
    if (confirm("You want delete this book from booklist?") == true) {
    mydata = {pk:id}
        fetch(deleteBookJsonUrl, {
            method: "DELETE",
            body: JSON.stringify(mydata)    
        }).then(response => {
            if (response.status === 201) {
                return response.text()
            } else if (response.status === 404) {
                return "Resource Not Found."
            } else {
                return "Request failed with status code " + response.status
            }
        }).then(data => {
            refreshBook()
            refreshBuku()
        }).catch(error => {
            console.error("Request failed", error)
        }) ;
    } else {
        refreshBook()
        refreshBuku()
    };
}