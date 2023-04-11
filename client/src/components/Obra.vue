<template>
    <div>
        <Header />
        <div class="retangulo-obra">
            <div class="foto-obra">
                <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
                <div v-if="estado === 1" class="estado-lista-desejos" />
                <div v-else-if="estado === 2" class="estado-em-progresso" />
                <div v-else-if="estado === 3" class="estado-finalizado" />
                <div v-else-if="estado === 4" class="estado-abandonado" />
            </div>
            <div class="container-infos-obra">
                <h1> {{ titulo }} </h1>
                <div v-if="naEstante" class="container-botoes">
                    <RouterLink :to="`/estanteConfig?dados=${encodeURIComponent((this.$route.query.dados))}&naEstante=true&estado=${estado}`" class="botao-estante">
                        Alterar Estado</RouterLink>
                        <RouterLink v-if="estado === 3" :to ="`/resenha?dados=${encodeURIComponent((this.$route.query.dados))}`" class="botao-estante" > 
                            Avaliar Obra</RouterLink>     
                    </div>
                    <div v-else class="container-botoes"> 
                        <RouterLink :to="`/estanteConfig?dados=${encodeURIComponent((this.$route.query.dados))}&naEstante=false`" class="botao-estante">
                            Adicionar à Estante</RouterLink>
                </div>
                <div class="descricao-obra">
                    <h4>{{ descricao }}</h4>
                </div>
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
    display: flex;
    flex-direction: column;
}

.foto-obra img {
    border: 1px solid;
    border-radius: 3px;
    max-height: 350px;
}

.estado-lista-desejos, .estado-em-progresso, .estado-finalizado, .estado-abandonado {
    height: 10px;
    margin-top: 3px;
    border-radius: 3px;
}

.estado-lista-desejos{
    background-color: rgb(245, 245, 65);
}

.estado-em-progresso{
    background-color: rgb(90, 83, 228);
}

.estado-finalizado{
    background-color: rgb(49, 157, 49);
}

.estado-abandonado{
    background-color: rgb(248, 59, 59);
}
.container-botoes{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.botao-estante {
    padding: 5px 10px;
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

.container-infos-obra {
    display: flex;
    flex-direction: column;
    text-align: justify;
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
            idObra: null,
            naEstante: false,
            estado: null
        };
    },
    created() {
        const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
        this.titulo = dados.title;
        this.descricao = dados.overview;
        this.foto = dados.poster_path;
        this.idObra = dados.id;
        this.jaNaEstante();
    },
    methods: {
        jaNaEstante() {
            api.getObraID(localStorage.getItem('idUsuario'), this.idObra).then((res) => {
                if(res.detail === undefined){
                    this.naEstante = true;
                    this.estado = res.estado;
                }
                else{
                    this.naEstante = false;   
                }
            });
        }
    }
};
</script>

<script setup>
import api from '../../services/api';
import Header from './Header.vue';
</script>