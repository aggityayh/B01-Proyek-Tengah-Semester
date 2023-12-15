
document.getElementById('filterAlphabet').addEventListener('change', filterBooks);

async function filterBooks() {
    const selectedAlphabet = document.getElementById('filterAlphabet').value;
    const bookOptions = document.querySelectorAll('#buku option');
    
    bookOptions.forEach((option) => {
        const bookAlphabet = option.getAttribute('data-alphabet');
        if (!selectedAlphabet || bookAlphabet === selectedAlphabet) {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    });
}

async function getReviews() {
    return fetch("/review/get-ulasan/").then((res) => res.json())
}

async function refreshReviews() {
    document.getElementById("review_table").innerHTML = "";
    const reviews = await getReviews();
    let htmlString = `<tr>
        <th>Judul Buku</th>
        <th>Nama</th>
        <th>Deskripsi Ulasan</th>
        <th>Rating Buku</th>
        <th>Tanggal Ulasan</th>
        <th>Hapus Review</th>
    </tr>`;
    reviews.forEach((item) => {
        htmlString += `\n<tr>
        <td>${item.buku__title}</td>
        <td>${item.reviewer_name}</td>
        <td>${item.review_text}</td>
        <td>${item.rating}</td>
        <td>${item.review_date}</td>
        <td><input type="button" class="btn btn-primary" onclick="deleteItemAjax(${item.pk})" value="Delete"></td>
    </tr>` 
    })
    
    document.getElementById("review_table").innerHTML = htmlString;
    document.getElementById("button_add").onclick = addUlasan
}

refreshReviews();

function addUlasan() {
    fetch("/review/create-review-ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#review-form'))
    }).then(() => {
        refreshReviews();
    });

    document.getElementById("review-form").reset();
    return false;
}

function deleteItemAjax(id) {
    mydata = {pk:id}
    fetch("/review/delete-ajax/", {
        method: "DELETE",
        body: JSON.stringify(mydata)    
    }).then(refreshReviews)
}

