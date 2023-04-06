<template>
    <header>
        <a v-on:click="login" class="nomePagina">Wydra</a>
        <nav>
            <ul class="menu">
                <li v-if="mostrarItem">
                    <RouterLink :to="`/estante?dados=${encodeURIComponent(JSON.stringify(usuario))}`">Estante</RouterLink>
                </li>
                <li v-if="mostrarItem">
                    <RouterLink :to="`/perfil?dados=${encodeURIComponent(JSON.stringify(usuario))}`">Perfil</RouterLink>
                </li>
                <li v-if="mostrarItem">
                    <RouterLink to="/busca">Busca</RouterLink>
                </li>
                <li v-if="mostrarItem">
                    <a v-on:click="logout" href="#">Logout</a>
                </li>
            </ul>
        </nav>
    </header>
</template>

<script>
export default{
    data() {
        return {
            mostrarItem: localStorage.getItem('mostrarItem') === 'true',
            usuario: JSON.parse(localStorage.getItem('usuario'))
        };
    },
    methods: {
        login(){
            this.$router.push({name:'login'})
        },
        logout()
        {
            localStorage.clear()
            localStorage.setItem('token', null)
            localStorage.setItem('usuario', null)
            localStorage.setItem('mostrarItem', 'false')
            this.$router.push({name:'login'})
        }
    },
}
</script>

<style scoped>
.nomePagina {
    font-size: 35px;
    color: rgb(229, 228, 228);
    text-decoration: none;
}

header {
    background-color: rgba(0, 0, 0, 0.834);
    display: flex;
    justify-content: space-around;
    padding: 5px;
    align-items: center;
    /* border-top: 2px solid cornflowerblue; */
    border-bottom: 2px solid cornflowerblue;
    width: 100%;
    height: 90px;
    bottom: 0px;
}

.menu {
    display: flex;
    list-style: none;
}

.menu li {
    margin-right: 20px;
}

.menu li a {
    color: white;
    font-size: 20px;
    text-decoration: none;
}
</style>