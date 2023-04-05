<template>
    <Header />
    <div class="retangulo-estante-config">
        <div class="foto-obra">
            <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
        </div>
        <form class="retangulo-add-estante" @submit.prevent="adicionarEstante">
            <div class="enunciado">
                <h2> Você deseja adicionar "{{ titulo }}" à sua Estante</h2>
            </div>
            <div class="selecao-estado">
                <label class="label-estado">Estado: 
                    <select class="dropdown-estado" required v-model="estado_selecionado">
                        <option value="">Selecione o estado da obra</option>
                        <option v-for="estado in estados" v-bind:value="estado.id_estado">
                            {{ estado.nome }}
                        </option>
                    </select>
                </label>
            </div>
            <div class="botao-adicionar">
                <Botao texto="Adicionar à Estante" />
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

.selecao-estado{
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
            estado_selecionado: null,
            estante: [],
            estados: [
                { id_estado: 1, nome: "Lista de Desejos" },
                { id_estado: 2, nome: "Em Progresso" },
                { id_estado: 3, nome: "Finalizada" },
                { id_estado: 4, nome: "Abandonada" }
            ],
        };
    },
    created() {
        const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
        this.titulo = dados.title;
        this.idObra = dados.id;
        this.foto = dados.poster_path;
    },

    methods: {
        adicionarEstante() {
            const data = {
                "obra": {
                    "id": this.idObra,
                    "tipo": 1,
                },
                "estado": this.estado_selecionado
            }
            
            api.getEstanteID(localStorage.getItem('idUsuario')).then(estante => {
                this.estante = estante;
                let obraNaEstante = false;
                let i;
                for(i = 0; i < estante.length; i++){
                    if(estante[i].obra.id == this.idObra){
                        obraNaEstante = true;
                    }
                }
                if (!obraNaEstante){
                    api.adicionarObraEstante(localStorage.getItem('token'), data)
                }
                else{
                    api.alterarObraEstante(localStorage.getItem('token'), this.idObra, this.estado_selecionado)
                }

                this.$router.push({name:'obra', query: {dados: encodeURIComponent(this.$route.query.dados)}})
            });

        }
    }
};
</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue'
import Header from './Header.vue'
</script>