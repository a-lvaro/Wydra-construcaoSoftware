<template>
  <div>
    <Header />
    <div>
      <form class="retangulo-login" @submit.prevent="fazerLogin">
        <img src="../../wydra.png" class="lontra" alt="lontrinha">
        <div class="titulo">
          <h1>Login</h1>
        </div>
        <label for="nick">Nome de Usuário:</label>
        <input placeholder = "Digite seu apelido" type="nick" id="nick" name="nick" required v-model="nick" />
  
        <label for="password">Senha:</label>
        <input placeholder = "Digite sua senha" type="password" id="password" name="password" required v-model="senha" />
        <Botao texto="Entrar"/>
        <div class="criar-conta">
          <p>Ainda não tem conta?</p>
          <Botao v-on:click="irParaCadastro" texto="Criar conta"/>
        </div>
      </form>
    </div>
  </div>
</template>
  
<style scoped>
form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.titulo{
  margin: 10px;
}

.lontra {
  margin-top: 30px;
  align-content: center;
  padding: auto;
}

input[type="email"],
input[type="nick"],
input[type="password"] {
  padding: 12px;
  align-content: center;
  margin-bottom: 30px;
  border: 1px solid #0c0909;
  border-radius: 10px;
  width: 100%;
  max-width: 320px;
  box-sizing: border-box;
}

input:hover{
  background-color: #eeeeee75;
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
  min-height: 680px;
  border-radius: 20px;
  /* Define o raio da borda */
  border: 2px solid #000000ba;
  /* Define a cor e largura da borda */
}

.criar-conta {
  display: flex;
  align-items:center;
  flex-direction: column;
  margin-top: 20px;
  margin-bottom: 20px;
}

.criar-conta p{
  margin-bottom: 10px;
}

</style>

<script>
export default {
  name: "Login",
  data() {
    return {
      nick: "",
      senha: "",
      usuario: {}
    }
  },

  methods: {
    fazerLogin() {
      const data =
      {
        nick: this.nick,
        senha: this.senha,
      }
      api.fazerLogin(data)
          .then(res => {
            if(typeof res === "string"){
              localStorage.setItem('token', res)
              api.getUsuarioLogado(res).then(data => {
                this.usuario = data
                localStorage.setItem('usuario', JSON.stringify(data))
                localStorage.setItem('idUsuario', data.id)
                localStorage.setItem('mostrarItem', 'true')
                this.$router.push(`/perfil?dados=${encodeURIComponent(localStorage.getItem('usuario'))}`)
              }
              )
            }
            else{
              console.log('erro ao logar')
              }
            }
            )
          },

    irParaCadastro(){
      this.$router.push({name:'cadastro'})
    }
  },
}
</script>

<script setup>
  import Botao from './Botao.vue'
  import api from '../../services/api.js'
  import Header from './Header.vue'
</script>