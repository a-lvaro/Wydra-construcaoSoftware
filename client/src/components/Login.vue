
<template>
  <div>
    <form class="retangulo-login" @submit.prevent="fazerLogin">
      <img src="../../wydra.png" class="lontra" alt="lontrinha">
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required v-model="email" />

      <label for="password">Senha:</label>
      <input type="password" id="password" name="password" required v-model="senha" />
      <Botao />
    </form>
  </div>
</template>
  
<style scoped>
form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.lontra {
  margin-top: 30px;
  align-content: center;
  padding: auto;
  ;
}

input[type="email"],
input[type="password"] {
  padding: 12px;
  align-content: center;
  margin-bottom: 30px;
  border: 3px solid #0c0909;
  border-radius: 10px;
  width: 100%;
  max-width: 320px;
  box-sizing: border-box;
}

input[type="password"] {
  -webkit-text-security: disc;
  -moz-text-security: disc;
  -ms-text-security: disc;
  -o-text-security: disc;
}



label {
  font-size: 20px;
}

.retangulo-login {
  margin: 50px auto;
  background-color: white;
  width: 420px;
  height: 700px;
  border-radius: 20px;
  /* Define o raio da borda */
  border: 2px solid #000000ba;
  /* Define a cor e largura da borda */
}
</style>



<script>
import Botao from './Botao.vue'

export default {
  name: "Login",
  data() {
    return {
      email: "",
      senha: ""
    }
  },

  methods: {
    fazerLogin() {
      const data = {
        email: this.email,
        senha: this.senha
      }
      console.log(data)
    },
  },
}
</script>