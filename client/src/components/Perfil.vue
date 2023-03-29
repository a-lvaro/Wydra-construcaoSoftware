<template>
    <div class="retangulo-perfil">
        <div class="container-foto-perfil">
            <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`foto ${nick}`">
        </div>
        <div class="container-infos-perfil">
            <div class="nome-usuario">
                <h1> {{ nome }} </h1>
            </div>
            <div class="nick-usuario">
                <h2>{{ nick }}</h2>
            </div>
            <RouterLink to="/estante"  class="botao-estante"><h2>Estante de {{ nome }}</h2></RouterLink>
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
    align-items: center;
}

.container-foto-perfil {
    height: 150px;
    width: 150px;
    margin: 20px;
    margin-right: 20px;
    border-radius: 100%;
    border: 2px solid black;
    align-self:flex-start;
}

.container-foto-perfil img{
    width: 100%;
    height: 100%;
    border-radius: 100%;
}

.botao-estante{
    text-decoration: none;
    color: #2c3e50;
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
      nome: null,
      nick: null,
      foto: null,
      id: null
    };
  },
  created() {
    const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
    this.nome = dados.nome + dados.sobrenome;
    this.nick = dados.nick;
    this.foto = dados.foto_perfil;
    this.id = dados.id
  }
}
</script>
  