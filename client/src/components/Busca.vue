<template>
    <div>

        <body>
            <form class="retangulo-login" @submit.prevent="fazerLogin">
                <img src="../../wydra.png" class="lontra" alt="lontrinha">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required v-model="email" />

                <label for="password">Senha:</label>
                <input type="password" id="password" name="password" required v-model="senha" />

                <button type="submit">Entrar</button>
            </form>
        </body>
    </div>
</template>

<script>
export default {
    name: "Busca",
    data() {
        return {
            string_busca: ''
        }
    }
}
</script>

<style>
body {
    background-color: rgba(0, 0, 0, 0.442);
}

.retangulo-login {
    margin: 50px auto;
    background-color: white;
    width: 520px;
    height: 800px;
    border-radius: 20px;
    border: 2px solid #000000ba;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

input[type="email"] {
    padding: 12px;
    align-content: center;
    margin-bottom: 30px;
    border: 3px solid #0c0909;
    border-radius: 10px;
    width: 100%;
    max-width: 320px;
    box-sizing: border-box;
}
</style>