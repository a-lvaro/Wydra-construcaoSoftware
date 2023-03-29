<template>
    <div class="retangulo-perfil">
        <div class="container-foto-perfil">
            <img src="https://thumbs.dreamstime.com/b/opte-pelo-avatar-placeholder-da-foto-%C3%ADcone-do-perfil-124557887.jpg">
        </div>
        <h1 class="nome-usuario">
            Nome do Usuário
        </h1>
        <RouterLink to="/estante" class="botao-estante">Estante de {{ nome }}</RouterLink>
    </div>
</template>

<style>
.retangulo-perfil {
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

.container-foto-perfil {
    height: 150px;
    width: 150px;
    margin: 10px;
    border-radius: 100%;
    border: 2px solid black;
    align-self:stretch;
}

.container-foto-perfil img{
    width: 100%;
    height: 100%;
    border-radius: 100%;
}

.nome-usuario{
    margin: 30px;
    align-self:stretch;
}

.botao-estante{
    text-decoration: none;
    font-size: 20px;
    color: #2c3e50;
}
</style>

<script>

</script>
  