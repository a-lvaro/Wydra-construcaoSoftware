function buscarFilmes(nome) {
    return fetch(`https://api.themoviedb.org/3/search/movie?api_key=158133b16a544083e8506dccf5af2bd4&query=${nome}&language=pt-BR&page=1&include_adult=false`).then(res => res.json());
}

function getFilmeID(id) {
    return fetch(`https://api.themoviedb.org/3/movie/${id}?api_key=158133b16a544083e8506dccf5af2bd4&language=pt-BR`).then(res => res.json());
}

function buscarUsuarios(nick) {
    return fetch(`http://127.0.0.1:8000/user/search?nick=${nick}`).then((res) => res.json());
}

function getUsuarioLogado(token) {
    return fetch(`http://127.0.0.1:8000/user/me?access_token=${token}`).then((res) => res.json());
}

function getObraID(idUsuario, idObra) {
    return fetch(`http://127.0.0.1:8000/estante/${idUsuario}/${idObra}`).then((res) => res.json());
}

function getEstanteID(id) {
    return fetch(`http://127.0.0.1:8000/estante/${id}`).then((res) => res.json());
}

function getResenhasUsuario(id) {
    return fetch(`http://127.0.0.1:8000/avaliacao/user/${id}`).then((res) => res.json());
}

function getResenhasObra(id) {
    return fetch(`http://127.0.0.1:8000/avaliacao/obra/${id}`).then((res) => res.json());
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

function fazerLogin(data){
    return fetch('http://127.0.0.1:8000/user/login',{
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
        .then((res) => res.json());
}

function adicionarObraEstante(token, data) {
    return fetch(`http://127.0.0.1:8000/estante/add?access_token=${token}`, {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
        .then((res) => res.json());
}

function alterarObraEstante(token, idObra, estado) {
    return fetch(`http://127.0.0.1:8000/estante/alterar?access_token=${token}&idObra=${idObra}&estado=${estado}`, {
        method: 'PUT',
        headers: {
            'accept': 'application/json'
        }
    })
        .then((res) => res.json());
}

function removerObraEstante(token, idObra) {
    return fetch(`http://127.0.0.1:8000/estante/remover?token=${token}&idObra=${idObra}`, {
        method: 'DELETE',
        headers: {
            'accept': 'application/json'
        }
    })
        .then((res) => res.json());
}

function publicarResenha(token, data) {
    return fetch(`http://localhost:8000/avaliacao/add?token=${token}`, {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
        .then((res) => res.json());
}

function darLikeResenha(token, idUsuario, idObra) {
    return fetch(`http://127.0.0.1:8000/avaliacao/curtir?token=${token}&idUsuario=${idUsuario}&idObra=${idObra}&curtir=true`, {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: JSON.stringify(''),
    })
        .then((res) => res.json());
}

export default {
    buscarFilmes, getFilmeID, criarUsuario, buscarUsuarios, fazerLogin, getUsuarioLogado, getEstanteID, 
    adicionarObraEstante, alterarObraEstante, getObraID, removerObraEstante, publicarResenha,
    getResenhasUsuario, getResenhasObra, darLikeResenha 
};