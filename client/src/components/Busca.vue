<template>
    <div>
        <form class="retangulo-busca" @submit.prevent="fazerBusca">
            <input type="search" id="busca" name="busca">
            <Botao texto="Buscar" />
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
                tipo_busca: this.tipo_busca,
                string_busca: this.string_busca
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

<script setup>
import Botao from './Botao.vue'
</script>