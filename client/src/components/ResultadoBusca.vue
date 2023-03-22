<template>
    <RouterLink :to="tipo" class="container-resultado">
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

img {
    height: 150px;
    border: 1px solid black;
}
</style>

<script>
export default {
    props: ['tipo', 'nomePrincipal', 'imagem', 'nick'],
    setup: (props) => {
        const { tipo, nomePrincipal, imagem, nick} = props
    }

}

</script>