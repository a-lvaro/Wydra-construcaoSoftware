<template>
    <div>
        <form class="retangulo-busca" @submit.prevent="fazerBusca">
            <div class="titulo">
                <h1>Busca</h1>
            </div>
            <div class="fitro-categoria">
                <label class="nome-filtro">Categoria
                    <select class="dropdown-categoria" required v-model="categoria_selecionada">
                        <option value="">Selecione o que deseja buscar</option>
                        <option v-for="categoria in categorias" v-bind:value="categoria.id_categoria">
                            {{ categoria.nome }}
                        </option>
                    </select>
                </label>
            </div>
            <div class="campo-busca">
                <label class="nome-campo-busca">Nome
                    <input placeholder="Digite o nome" type="search" id="busca" name="busca" required v-model="string_busca" />
                </label>
            </div>
            <div class="botao-buscar">
                <Botao texto="Buscar" />
            </div>
        </form>
    </div>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.titulo{
    padding: 30px;
}

.retangulo-busca {
    margin: 50px auto;
    background-color: white;
    width: 420px;
    height: 410px;
    border-radius: 20px;
    border: 2px solid #000000ba;
}

.nome-filtro,
.nome-campo-busca{
    font-size:large;
    display: flex;
    flex-direction: column;
}

.dropdown-categoria{
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

.botao-buscar{
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
                { id_categoria: 5, nome: "Álbum" }
            ],
            string_busca: '',
            categoria_selecionada: '',
        }
    },

    methods: {
        fazerBusca() {
            const data = {
                categoria_selecionada: this.categoria_selecionada,
                string_busca: this.string_busca
            }
            console.log(data)
        },
    }
}
</script>

<script setup>
import Botao from './Botao.vue'
</script>