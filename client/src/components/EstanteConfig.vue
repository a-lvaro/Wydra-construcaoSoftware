<template>
    <div>
        <Header />
        <div class="retangulo-estante-config">
            <div class="foto-obra">
                <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
                <div v-if="estadoAnterior === 1" class="estado-lista-desejos" />
                <div v-else-if="estadoAnterior === 2" class="estado-em-progresso" />
                <div v-else-if="estadoAnterior === 3" class="estado-finalizado" />
                <div v-else-if="estadoAnterior === 4" class="estado-abandonado" />
            </div>
            <form class="retangulo-add-estante" @submit.prevent="adicionarEstante">
                <RouterLink :to="`/obra?dados=${this.$route.query.dados}`" class="botao-voltar">{{'<'}} Voltar</RouterLink>
                <div class="enunciado">
                    <h2 v-if="naEstante"> Você deseja alterar o estado de "{{ titulo }}"</h2>
                    <h2 v-else> Você deseja adicionar "{{ titulo }}" à sua Estante</h2>
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
                    <Botao v-if="naEstante" texto="Alterar Estado" />
                    <Botao v-else texto="Adicionar à Estante" />
                </div>
                <a v-if="naEstante" class="botao-remover" v-on:click="removerDaEstante" href="#">Remover da Estante</a>
            </form>
        </div>
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

.foto-obra img {
    max-height: 350px;
}

.retangulo-add-estante {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    
}

.botao-voltar{
    margin-bottom: 20px;
    width: 90px;
    padding: 5px;
    text-decoration: none;
    color: rgb(34, 84, 176);
    font-size: large;
}

.botao-voltar:hover{
    color: rgb(40, 112, 245);
}

.enunciado{
    margin-bottom: 30px;
}

.selecao-estado{
    margin-bottom: 20px;
}
.botao-adicionar{
    width: 200px;
}
.botao-remover {
    margin-top: 20px;
    padding: 10px;
    font-size: 18px;
    background-color: cornflowerblue;
    color: white;
    border: 2px solid black;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    box-sizing: border-box;
    width: 135px;
    justify-content: center;
    text-decoration: none;
    text-align: center;
}
.botao-remover:hover {
    background-color: rgb(40, 112, 245);
}

</style>

<script>
export default {
    props: ['dados', 'naEstante', 'estado'],
    setup: (props) => {
        const { dados, naEstante, estado } = props
    },
    data() {
        return {
            titulo: null,
            descricao: null,
            foto: null,
            estado_selecionado: null,
            naEstante: null,
            idObra: null,
            estadoAnterior: null,
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
        this.naEstante = JSON.parse(decodeURIComponent(this.$route.query.naEstante));
        if (this.naEstante){
            this.estadoAnterior = JSON.parse(decodeURIComponent(this.$route.query.estado));
        }
    },

    methods: {
        async adicionarEstante() {
            const data = {
                "obra": {
                    "id": this.idObra,
                    "tipo": 1,
                    "nota": 0
                },
                "estado": this.estado_selecionado
            }
            
            api.getEstanteID(localStorage.getItem('idUsuario')).then(async estante => {
                this.estante = estante;
                let obraNaEstante = false;
                let i;
                for(i = 0; i < estante.length; i++){
                    if(estante[i].obra.id == this.idObra){
                        obraNaEstante = true;
                    }
                }
                if (!obraNaEstante){
                    await api.adicionarObraEstante(localStorage.getItem('token'), data)
                }
                else{
                    await api.alterarObraEstante(localStorage.getItem('token'), this.idObra, this.estado_selecionado)
                }
            }).then(() => {
                this.$router.push({name:'obra', query: {dados: this.$route.query.dados}})
            });

        },

        async removerDaEstante(){
            await api.removerObraEstante(localStorage.getItem('token'), this.idObra)
            this.$router.push({name:'obra', query: {dados: this.$route.query.dados}})
        }
    }
};
</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue'
import Header from './Header.vue'
</script>