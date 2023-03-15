<template>
    <div>
        <form class="retangulo-busca" @submit.prevent="fazerBusca">
            <div class="titulo">
                <h1>Buscar</h1>
            </div>
            <div class="campo-busca">
                <input type="search" id="busca" name="busca">
            </div>
            <div class="botao-buscar">
                <Botao texto="Buscar" />
            </div>
        </form>
    </div>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.retangulo-busca {
  margin: 50px auto;
  background-color: white;
  width: 420px;
  height: 600px;
  border-radius: 20px;
  border: 2px solid #000000ba;
}

input[type="search"] {
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

<script setup>
import Botao from './Botao.vue'
</script>