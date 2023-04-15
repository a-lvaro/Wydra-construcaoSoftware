<template>
    <div>
        <Header />
        <form class="retangulo-resenha"  @submit.prevent="publicarResenha">
            <div class="foto-obra">
                <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster`">
            </div>
            <div >
                <div >
                    <RouterLink :to="`/obra?dados=${this.$route.query.dados}`" class="botao-voltar">{{'<'}} Voltar</RouterLink>
                    <br>
                    <label  for="resenha" style="font-size: large;">Digite sua resenha: (opcional)</label>
                        <br>
                            <textarea minlength="100" maxlength="1000" v-model="resenha" style="font-size: medium; padding: 5px;" class = "campo" id="resenha" name="resenha" rows="10" cols="60"></textarea>
                            <br>
                            <label style = "font-size: large;" for="nota">Digite sua nota (1 a 5):</label>
                            <br>
                            <div class = "container-nota">
                                <input required v-model="nota" type="number" id="nota" name="nota" min="1" max="5" step="1">
                                <Botao class = "botao-resenha" texto="Publicar resenha" />
                            </div>
                        <br>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    props: ['dados'],
    setup: (props) => {
        const { dados } = props
    },

    data(){
        return {
            foto: null,
            nota: null,
            idObra: null,
            resenha: ''
        };
    },

    created() {
        const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
        this.foto = dados.poster_path;
        this.idObra = dados.id;
    },

    methods: {
        async publicarResenha(){
            const avaliacao = {
                "nota": this.nota,
                "resenha": this.resenha,
                "obra": {
                    "id": this.idObra,
                    "tipo": 1,
                }
            }
           await api.publicarResenha(localStorage.getItem('token'), avaliacao) 
            this.$router.push({name:'obra', query: {dados: this.$route.query.dados}}) 
        }
    }
}
</script>

<style scoped>
.retangulo-resenha {
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
    overflow-x: auto;
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

#nota{
        width: 150px;
        align-items: center;
        border-radius: 10px; 
        padding: 10px;
        font-size: 18px; 
}

.container-nota{
    display: flex;
    flex-direction: row;
    align-items: center;
}

.botao-resenha{
    margin-left: 100px;
}

.foto-obra {
    margin: 30px;
    border: 2px solid;
    border-radius: 3px;
    display: flex;
}

.foto-obra img{
    max-height: 400px;
}

.campo {
    font-size: larger;
}

</style>

<script setup>
    import api from '../../services/api';
    import Header from './Header.vue';
    import Botao from './Botao.vue';
</script>