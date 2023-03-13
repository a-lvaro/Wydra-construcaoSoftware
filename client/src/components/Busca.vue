<template>
    <div>
        <form class="retangulo-login" @submit.prevent="fazerBusca">
            <button type="submit">Entrar</button>
        </form>
    </div>
</template>

<script>
export default {
    name: "Busca",
    data() {
        return {
            string_busca: ''
        }
    },

    methods: {
        fazerBusca() {
            const data = {
                email: this.email,
                senha: this.senha
            }
            console.log(data)
        },
    },
}
</script>

<style scoped>

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