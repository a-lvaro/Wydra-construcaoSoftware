<template>
    <RouterLink to="/obra" class="container-resultado">
        <img :src="imagem" alt="imagem de capa ou perfil">
        <div class="textos-resultado">
            <h2>{{ nomePrincipal }}</h2>
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
    border: 1px solid;
}
</style>

<script>
export default {
    props: ['nomePrincipal', 'imagem'],
    setup: (props) => {
        const { nomePrincipal, imagem} = props
    }

}

</script>