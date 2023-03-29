<template>
    <div class="retangulo-obra">
        <div class="foto-obra">
            <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`">
        </div>
        <div class="container-infos-obra">
            <h1> {{ titulo }} </h1>
            <div class="descricao-obra">
                <h3>{{ descricao }}</h3>
            </div>
        </div>
        <form>

        </form>
    </div>
</template>

<style scoped>
.retangulo-obra {
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
      foto: null
    };
  },
  created() {
    const dados = JSON.parse(decodeURIComponent(this.$route.query.dados));
    this.titulo = dados.title;
    this.descricao = dados.overview;
    this.foto = dados.poster_path;
  }
};
</script>