<template>
    <RouterLink :to="`/obra?dados=${encodeURIComponent(JSON.stringify(json))}`" class="container-obra">
        <img :src="imagem" alt="imagem de capa ou perfil">
        <div v-if="estado == 1" class="estado-lista-desejos" />
        <div v-else-if="estado == 2" class="estado-em-progresso" />
        <div v-else-if="estado == 3" class="estado-finalizado" />
        <div v-else-if="estado == 4" class="estado-abandonado" />
    </RouterLink>
</template>

<style scooped>
.container-obra {
    margin: 8px;    
    display: flex;
    flex-direction: column;
}

.container-resultado img {
    height: 150px;
    border: 1px solid black;
}

.estado-lista-desejos, .estado-em-progresso, .estado-finalizado, .estado-abandonado {
    height: 5px;
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
</style>

<script>
export default {
    props: ['json', 'imagem', 'estado'],
    setup: (props) => {
        const {json, imagem, estado} = props
    }
}

</script>