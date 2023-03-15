<template>
    <header>
        <p class="nomePagina">Wydra</p>
        <nav>
            <ul class="menu">
                <li>
                    <RouterLink to="/cadastro">Cadastro</RouterLink>
                </li>
                <li>
                    <RouterLink to="/login">Login</RouterLink>
                </li>
                <li>
                    <RouterLink to="/estante">Estante</RouterLink>
                </li>
                <li>
                    <RouterLink to="/perfil">Perfil</RouterLink>
                </li>
                <li>
                    <RouterLink to="/busca">Busca</RouterLink>
                </li>
                <li>
                    <RouterLink to="/Logout">Logout</RouterLink>
                </li>
            </ul>
        </nav>
    </header>
</template>

<script>
</script>

<style scoped>
.nomePagina {
    font-size: 35px;
    /* Altere o tamanho do texto para o desejado */
    font-family: 'Segoe UI';
    color: rgb(229, 228, 228);
}

header {
    background-color: rgba(0, 0, 0, 0.834);
    display: flex;
    justify-content: space-around;
    padding: 5px;
    align-items: center;
    /* border-top: 1px solid cornflowerblue; */
    border-bottom: 1px solid cornflowerblue;
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
    font-family: 'Segoe UI';
    text-decoration: none;
}
</style>