<template>
    <div class="retangulo-obra">
        <div class="foto-obra">
            <img src="https://m.media-amazon.com/images/I/817esPahlrL.jpg" alt="capa cem anos">
        </div>
        <div class="container-infos-obra">
            <h1>Cem Anos de Solidão</h1>
            <h2>Gabriel García Márquez</h2>
            <h3>Gênero: Realismo Mágico</h3>
        </div>
    </div>
</template>

<style scoped>
.retangulo-obra {
    margin: 50px auto;
    background-color: white;
    width: 900px;
    height: 420px;
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
}
</style>

<script setup>

</script>