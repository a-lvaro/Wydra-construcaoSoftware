<template>
    <RouterLink :to="`/obra?dados=${encodeURIComponent(JSON.stringify(json))}`" class="container-resultado">
        <img :src="imagem" alt="imagem de capa ou perfil">
    </RouterLink>
</template>

<style scooped>
.container-resultado {
    margin: 8px;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-decoration: none;
    
}
.container-resultado img {
    height: 150px;
    border: 1px solid black;
}
</style>

<script>
export default {
    props: ['json', 'imagem'],
    setup: (props) => {
        const { json, imagem} = props
    },
}

</script>