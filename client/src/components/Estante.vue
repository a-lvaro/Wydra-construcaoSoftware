<template>
    <div class="estante">
        <div class="usuario">
            <h1>Estante de {{nick}}</h1>
        </div>
    
        <div class="retangulo-estante">
            <div v-for="(item, index) in resultados_obra" :key="index" class="container-obra">
                <ResultadoBusca :json="item" tipo="/obra" 
                    :imagem="'https://image.tmdb.org/t/p/w500/' + item.poster_path" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.retangulo-estante {
    /* margin: 0px 50px 50px 50px auto; */
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

.estante{
    margin-bottom: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}
.usuario {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: white;
    padding: 1rem;
}

</style>

<script>
export default {
    // props: ['dados'],
    // setup: () => {
    //     this.resultados_obra = []
    // },

    data() {
        return {
            nick: null,
            resultados_obra: []
        };
    },
    created() {
        
    }
};
</script>