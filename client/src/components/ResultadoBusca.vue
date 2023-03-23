<template>
    <RouterLink :to="`${tipo}?dados=${encodeURIComponent(JSON.stringify(json))}`" class="container-resultado">
        <img :src="imagem" alt="imagem de capa ou perfil">
        <div class="textos-resultado">
            <h2>{{ nomePrincipal }}</h2>
            <h3>{{ nick??"" }}</h3>
        </div>
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

.textos-resultado {
    margin-left: 30px;
    color: #2C3E50;
}

.container-resultado img {
    height: 150px;
    border: 1px solid black;
}
</style>

<script>
export default {
    props: ['json', 'tipo', 'nomePrincipal', 'imagem', 'nick'],
    setup: (props) => {
        const { json, tipo, nomePrincipal, imagem, nick} = props
    },
}

</script>