<template>
    <Header />
    <div class="retangulo-estante">
        <RouterLink :to="`/perfil?dados=${this.$route.query.dados}`" class="botao-perfil">
            <h2>Estante de {{ usuario.nome + ' ' + usuario.sobrenome }}</h2>
        </RouterLink>
        <div class="container-obras">
            <div v-for="(item, index) in obrasEstante" :key="index" class="container-resultado">
                <ObraEstante :json="item" :imagem="'https://image.tmdb.org/t/p/w500/' + item.poster_path" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.retangulo-estante {
    margin: 50px auto;
    padding-right: 20px;
    background-color: white;
    width: 900px;
    min-height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    flex-direction: column;
    display: flex;
    align-items: center;
}

.botao-perfil {
    margin: 10px 30px;
    align-self: self-start;
    text-decoration: none;
    color: rgb(34, 84, 176);
}

.container-obras {
    display: inline-grid;
    grid-template-columns: auto auto auto auto auto auto;
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
            usuario: {
                nome: '',
                sobrenome: ''
            },
            estanteID: [],
            obrasEstante: []
        };
    },
    mounted() {
        this.usuario = JSON.parse(decodeURIComponent(this.$route.query.dados));

        api.getEstanteID(this.usuario.id).then((res) => 
        {
                res.forEach(obraID => {
                    this.estanteID.push(obraID.obra.id)
            });
        }).then(() => 
        {
            this.estanteID.forEach(obraID => {
                api.getFilmeID(obraID).then((res) => {
                    if(res.success === undefined){
                        this.obrasEstante.push(res)
                    }
                })
            })
        });
        window.scrollTo(0, this.top);
    },
};
</script>

<script setup>
import api from '../../services/api';
import Header from './Header.vue'
import ObraEstante from './ObraEstante.vue'
</script>