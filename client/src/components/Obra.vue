<template>
    <Header />
    <div class="retangulo-obra">
        <div class="foto-obra">
            <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
        </div>
        <div class="container-infos-obra">
            <h1> {{ titulo }} </h1>
            <!-- <div v-if="jaNaEstante" class="botao-estante">
                <RouterLink :to="`/estanteConfig?dados=${encodeURIComponent((this.$route.query.dados))}`" class="botao-estante">
                    Alterar Estado</RouterLink>
            </div>
            <div v-else class="botao-estante"> 
                <RouterLink :to="`/estanteConfig?dados=${encodeURIComponent((this.$route.query.dados))}`" class="botao-estante">
                    Adicionar à Estante</RouterLink>
            </div> -->
            <div class="descricao-obra">
                <h4>{{ descricao }}</h4>
            </div>
        </div>
    </div>
</template>

<style scoped>
.retangulo-obra {
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

.container-infos-obra {
    display: flex;
    flex-direction: column;
    text-align: justify;
}

.botao-estante {
    padding: 5px;
    margin: 10px;
    font-size: 18px;
    background-color: cornflowerblue;
    color: white;
    border: 2px solid black;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    box-sizing: border-box;
    min-width: 100px;
    max-width: 200px;
    justify-content: center;
}

.botao-estante:hover {
    background-color: rgb(40, 112, 245);
}

.descricao-obra {
    max-width: max-content;
    overflow: auto;
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
            idObra: null
        };
    },
    created() {
        const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
        this.titulo = dados.title;
        this.descricao = dados.overview;
        this.foto = dados.poster_path;
        this.idObra = dados.id;
        this.jaNaEstante()
    },
    methods: {
        jaNaEstante() {
            try {   
                api.getObraID(localStorage.getItem('idUsuario'), this.idObra);
            }
            catch(err) {
                console.log(err)
                return false
            }
        }
    }
};
</script>

<script setup>
import api from '../../services/api';
import Header from './Header.vue'
</script>