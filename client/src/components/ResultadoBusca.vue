<template>
    <RouterLink to="/obra" class="container-resultado">
        <img src={{ imagem }} alt="imagem de capa ou perfil">
        <div class="textos-resultado">
            <h2>{{ nomePrincipal }}</h2>
            <h3>{{ nomeSecundario }}</h3>
        </div>
    </RouterLink>
</template>

<style scooped>
.container-resultado {
    margin: 8px;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.textos-resultado {
    margin-left: 8px;
}
</style>

<script>
export default {
    props: ['id', 'tipo', 'nomePrincipal', 'nomeSecundario', 'imagem']
}

</script>