<template>
    <div class="retangulo-estante-config">
        <div class="foto-obra">
            <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
        </div>
        <form class="retangulo-add-estante" @submit.prevent="adicionarEstante">
            <div class="enunciado">
                <h2> Você deseja adicionar "{{ titulo }}" à sua Estante</h2>
            </div>
            <div class="selecao-status">
                <label class="label-status">Status: 
                    <select class="dropdown-status" required v-model="status_selecionado">
                        <option value="">Selecione o status da obra</option>
                        <option v-for="categoria in status" v-bind:value="categoria.id_categoria">
                            {{ categoria.nome }}
                        </option>
                    </select>
                </label>
            </div>
            <div class="botao-adicionar">
                <Botao v-on:click="adicionarEstante" texto="Adicionar à Estante" />
            </div>
        </form>
    </div>
</template>

<style scoped>
.retangulo-estante-config {
    margin: 50px auto;
    padding-right: 20px;
    background-color: white;
    width: 900px;
    min-height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    flex-direction: row;
    display: flex;
    align-items: center;
}

.foto-obra {
    margin: 30px;
    border: 1px solid;
    border-radius: 3px;
    display: flex;
}

.foto-obra img {
    max-height: 350px;
}

.retangulo-add-estante {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;

}

.enunciado{
    margin-bottom: 30px;
}

.selecao-status{
    margin-bottom: 20px;
}


</style>

<script>
export default {
    props: ['dados'],
    setup: (props) => {
        const { dados } = props
    },
    data() {
        return {
            titulo: null,
            descricao: null,
            foto: null,
            status_selecionado: null,
            status: [
                { id_status: "Lista de Desejos", nome: "Lista de Desejos" },
                { id_status: "Em Progresso", nome: "Em Progresso" },
                { id_status: "Finalizada", nome: "Finalizada" },
                { id_status: "Abandonada", nome: "Abandonada" }
            ],
        };
    },
    created() {
        const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
        this.titulo = dados.title;
        this.id = dados.id;
        this.foto = dados.poster_path;
    },

    methods: {
        adicionarEstante() {
            this.$router.push({name:'resenha'})
        }
    }
};
</script>

<script setup>
import Botao from './Botao.vue'
</script>