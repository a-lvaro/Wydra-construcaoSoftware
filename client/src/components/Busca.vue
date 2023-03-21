<template>
    <div class="container-busca">
        <form class="retangulo-busca" @submit.prevent="fazerBusca">
            <div class="titulo">
                <h1>Busca</h1>
            </div>
            <div class="fitro-categoria">
                <label class="nome-filtro">Categoria
                    <select class="dropdown-categoria" required v-model="categoria_selecionada">
                        <option value="">Selecione o que deseja buscar</option>
                        <!-- <option v-for="categoria in categorias" v-bind:value="categoria.id_categoria">
                            {{ categoria.nome }}
                        </option> -->
                    </select>
                </label>
            </div>
            <div class="campo-busca">
                <label class="nome-campo-busca">Nome
                    <input placeholder="Digite o nome" type="search" id="busca" name="busca" required
                        v-model="string_busca" />
                </label>
            </div>
            <div class="botao-buscar">
                <Botao texto="Buscar" />
            </div>
        </form>
        <div class="retangulo-resultado">
            <RouterLink to="/obra" class="container-resultado">
                <img src="https://m.media-amazon.com/images/I/817esPahlrL.jpg" alt="capa cem anos">
                <div class="textos-resultado">
                    <h2>Cem anos de solidão</h2>
                    <h3>Gabriel García Márquez </h3>
                </div>
            </RouterLink>
            <div class="container-resultado">
                <img src="https://m.media-amazon.com/images/I/817esPahlrL.jpg" alt="capa cem anos">
                <div class="textos-resultado">
                    <h2>Cem anos de solidão</h2>
                    <h3>Gabriel García Márquez</h3>
                </div>
            </div>

        </div>
    </div>
</template>

<style scoped>
/* AQUI A IMAGEM */
img {
    height: 100px;
}

.container-busca {
    flex-direction: row;
    display: flex;
    align-items: center;
    margin: auto;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.titulo {
    padding: 30px;
    align-self: flex-start;
}

.retangulo-busca {
    margin: 50px auto;
    /* margin-right: 2px; */
    background-color: white;
    width: 500px;
    height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
}

.retangulo-resultado {
    margin: 50px auto;
    background-color: white;
    width: 650px;
    height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: auto;
    padding: 10px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background-color: cornflowerblue;
    border: 4px solid transparent;
    border-radius: 10px;
    background-clip: padding-box;
}

::-webkit-scrollbar {
    width: 16px;
    border-radius: 8px;
    border-bottom-left-radius: 0px;
    border-top-left-radius: 0px;
    background-color: #b6b5b5ba;
}

.nome-filtro,
.nome-campo-busca {
    font-size: large;
    display: flex;
    flex-direction: column;
}

.dropdown-categoria {
    padding: 12px;
    align-content: center;
    margin-bottom: 30px;
    border: 2px solid #0c0909;
    border-radius: 10px;
    width: 270px;
    box-sizing: border-box;
}

input[type="search"] {
    padding: 12px;
    align-content: center;
    margin-bottom: 30px;
    border: 2px solid #0c0909;
    border-radius: 10px;
    width: 270px;
    box-sizing: border-box;
}

.container-resultado {
    margin: 8px;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.textos-resultado {
    margin-left: 8px;
}

.botao-buscar {
    padding-bottom: 30px;
}
</style>

<script>

export default {
    name: "Busca",
    data() {
        return {
            categorias: [
                { id_categoria: 0, nome: "Usuário" },
                { id_categoria: 1, nome: "Livro" },
                { id_categoria: 2, nome: "Filme" },
                { id_categoria: 3, nome: "Série" },
                { id_categoria: 4, nome: "Jogo" },
                { id_categoria: 5, nome: "Álbum Musical" }
            ],
            string_busca: '',
            categoria_selecionada: '',
        }
    },

    methods: {
        fazerBusca() {
            const USUARIO = 0;

            const data = {
                string_busca: this.string_busca
            }

            if (this.categoria_selecionada == USUARIO) {
                api.buscarUsuario(this.string_busca).then((res) => console.log(res))
            }
            else {
                api.buscarFilmes(this.string_busca)
                    .then((res) => console.log(res))
            }
        },
    }
}
</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue' 
</script>