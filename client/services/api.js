function buscarFilmes(nome) {
    return fetch(`https://api.themoviedb.org/3/search/movie?api_key=158133b16a544083e8506dccf5af2bd4&query=${nome}&language=pt-BR&page=1&include_adult=true`).then((res) => res.json());
}

function buscarUsuario(nick) {
    return fetch(`http://127.0.0.1:8000/user/search?nick=${nick}`).then((res) => res.json());
}

function criarUsuario(data) {
    return fetch('http://127.0.0.1:8000/user/signup', {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
        .then((res) => res.json());
}



function getProductsById(id) {
    return fetch(`http://localhost:3333/products/${id}`).then((res) => res.json());
}

function getProductsPetshop(id) {
    return fetch(`http://localhost:3333/products/petshop/${id}`).then((res) => res.json());
}

function createProducts(newProduct) {
    return fetch('http://localhost:3333/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newProduct),
    })
        .then((res) => res.json());
}

function removeProducts(id) {
    return fetch(`http://localhost:3333/products/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then((res) => res.json())
        .catch((err) => console.log(err));
}

function editProducts(products, id) {
    return fetch(`http://localhost:3333/products/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(products)
    })
        .then((res) => res.json());
}

export default {
    buscarFilmes, criarUsuario, buscarUsuario
};