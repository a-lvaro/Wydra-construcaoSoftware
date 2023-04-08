<template>
    <div>
        <Header />
        <form class="retangulo-resenha"  @submit.prevent="publicarResenha">
            <div class="foto-obra">
                <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster`">
            </div>
            <div >
                <div >
                    <label  for="resenha" style="font-size: large;">Digite sua resenha: (opcional)</label>
                        <br>
                            <textarea minlength="100" maxlength="1000" v-model="resenha" style="font-size: medium;" class = "campo" id="resenha" name="resenha" rows="14" cols="60"></textarea>
                            <!-- A tag <textarea> cria um campo de entrada de texto multilinha -->
                            <br>
                            <label style = "font-size: large;" for="nota">Digite sua nota (0 a 5):</label>
                            <br>
                            <div class = "container-nota">
                                <input required v-model="nota" type="number" id="nota" name="nota" min="0" max="10" step="1">
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
        publicarResenha(){
            const info ={
                        "nota": this.nota,
                        "resenha": this.resenha,
                        "obra": {
                            "id": this.idObra,
                            "tipo": 1
                        }
                        }
                console.log(info)
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
    import Header from './Header.vue';
    import Botao from './Botao.vue';
</script>