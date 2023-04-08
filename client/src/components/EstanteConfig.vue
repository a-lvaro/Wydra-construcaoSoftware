<template>
    <div>
        <Header />
        <div class="retangulo-estante-config">
            <div class="foto-obra">
                <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
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
    props: ['dados', 'naEstante'],
    setup: (props) => {
        const { dados, naEstante } = props
    },
    data() {
        return {
            titulo: null,
            descricao: null,
            foto: null,
            estado_selecionado: null,
            naEstante: null,
            idObra: null,
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
            console.log(data)
            
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

        },

        removerDaEstante(){
            api.removerObraEstante(localStorage.getItem('token'), this.idObra).then(() => {
                this.$router.push({name:'obra', query: {dados: encodeURIComponent(this.$route.query.dados)}})
            })
        }
    }
};
</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue'
import Header from './Header.vue'
</script>