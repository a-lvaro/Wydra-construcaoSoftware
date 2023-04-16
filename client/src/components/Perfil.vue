<template>
    <div>
        <Header />
        <div class="retangulo-perfil">
            <div class="container-foto-perfil">
                <img :src="foto" :alt="`foto ${nick}`">
            </div>
            <div class="container-infos-perfil">
                <div class="nome-usuario">
                    <h1> {{ nome }} </h1>
                    <div v-if= "usuarioLogado">
                        <RouterLink class="botao-alterar" to="/editarCadastro"> editar informações </RouterLink>
                    </div>
                </div>
                <div class="nick-usuario">
                    <h2>{{ nick }}</h2>
                </div>
                <RouterLink :to="`/estante?dados=${this.$route.query.dados}`"  class="botao-estante"><h2>Estante de {{ nome }}</h2></RouterLink>
                <div v-for="(item, index) in resenhas" :key="index" class="container-resenha">
                    <ResenhaPost :dados-usuario="usuario" :dados-resenha="item"/>
                </div>
            </div>
    </div>
    </div>
</template>

<style>
.retangulo-perfil {
    margin: 50px auto;
    padding-right:20px;
    background-color: white;
    width: 900px;
    min-height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    flex-direction: row;
    display: flex;
    align-items: flex-start;
}

.container-infos-perfil {
    display: flex;
    flex-direction: column;
    margin: 30px 10px;
}

.container-foto-perfil {
    height: 150px;
    width: 150px;
    margin: 20px;
    margin-right: 20px;
    border-radius: 100%;
    border: 2px solid black;
}

.container-foto-perfil img{
    width: 100%;
    height: 100%;
    border-radius: 100%;
}

.botao-estante{
    text-decoration: none;
    color: rgb(34, 84, 176);
}

.botao-alterar {
    padding: 5px 10px;
    margin: 10px 0px;
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
    text-decoration: none;
}

.botao-alterar:hover {
    background-color: rgb(40, 112, 245);
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
      usuario: {},
      nome: null,
      nick: null,
      foto: null,
      idUsuario: null,
      usuarioLogado: false,
      resenhas: []
    };
  },
  created() {
    const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
    this.usuario = dados;
    this.nome = dados.nome + ' ' + dados.sobrenome;
    this.nick = dados.nick;
    this.foto = dados.caminho_foto;
    this.idUsuario = dados.id
    this.getResenhas()
    this.checarUsuarioLogado();
    window.scrollTo(0, this.top);
  },

  methods: {
    getResenhas(){
        api.getResenhasUsuario(this.idUsuario).then(res => {
            this.resenhas = res
        })
    },
    checarUsuarioLogado(){
        if (localStorage.getItem("idUsuario") == this.idUsuario){
            this.usuarioLogado = true;
        }
    }
  }
}
</script>

<script setup>
import api from '../../services/api';
import Header from './Header.vue'
import ResenhaPost from './ResenhaPost.vue';
</script>
  