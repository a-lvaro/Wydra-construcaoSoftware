<template>
    <div>
        <Header />
        <div class="cadastro">
            <div class="container">
                <div class="form-image">
                    <img src="join.svg" alt="cadastro">
                </div>
                <div class="formulario">
                    <form @submit.prevent="fazerCadastro">
                        <div class="header-formulario">
                            <div class="titulo">
                                <h1>Cadastre-se</h1>
                            </div>
                            <div class="botao-entrar">
                                <button>
                                    <RouterLink v-on:click="login" to="/login">Fazer Login</RouterLink>
                                </button>
                            </div>
                        </div>
                        <div class="inputs">
                            <div class="input-box">
                                <label for="name">Nome </label>
                                <input placeholder=" Digite seu nome" type="text" id="name" name="name" required v-model="nome">
                            </div>
    
                            <div class="input-box">
                                <label for="name">Sobrenome </label>
                                <input placeholder=" Digite seu sobrenome" type="text" id="name" name="name" required v-model="sobrenome">
                            </div>
    
                            <div class="input-box">
                                <label for="nickname">Apelido </label>
                                <input placeholder=" Digite seu nickname" type="text" id="nickname" name="nickname" required
                                    v-model="nickname">
                            </div>
    
                            <div class="input-box">
                                <label for="emailCadastro">Email </label>
                                <input placeholder=" Digite seu melhor email" type="emailCadastro" id="email" name="email"
                                    required v-model="email">
                            </div>
    
                            <div class="input-box">
                                <label for="passwordCadastro">Senha </label>
                                <input placeholder=" Digite sua senha" type="password" id="passwordCadastro"
                                    name="passwordCadastro" required v-model="senha">
                            </div>
    
                            <div class="input-box">
                                <label for="confirmaSenha">Confirme sua Senha </label>
                                <input placeholder=" Digite sua senha novamente" type="password" id="confirmaSenha"
                                    name="confirmaSenha" required v-model="confirmaSenha">
                            </div>

                            <div class="input-box">
                                <label for="foto">Foto de Perfil </label>
                                 <input ref="foto de perfil" accept="image/jpeg" type="file" @change="pickFile">
                            </div>
                        </div>
    
                        <div class="continue-button">
                            <Botao texto="Continuar" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.cadastro {
    width: 100%;
    /* height: 100vh; */
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    width: 80%;
    height: 700px;
    display: flex;
    box-shadow: 10px 5px 10px rgba(0, 0, 0, .212);
}

.form-image {
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: cornflowerblue;
    padding: 1rem;
}

.form-image img {
    width: 31rem;
}

.formulario {
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: white;
    padding: 3rem;
}

.header-formulario {
    margin-bottom: 2rem;
    display: flex;
    justify-content: space-between;
}

.botao-entrar {
    display: flex;
    align-items: center;
}

.botao-entrar button {
    cursor: pointer;
    padding: 10px;
    font-size: 18px;
    background-color: cornflowerblue;
    color: white;
    border: 2px solid black;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    box-sizing: border-box;
    min-width: 100px;
    justify-content: center;
}

.botao-entrar button:hover {
    background-color: rgb(40, 112, 245);
}

.botao-entrar button a {
    text-decoration: none;
    font-weight: 500;
    color: white
}

.header-formulario h1::after {
    content: '';
    display: block;
    width: 5rem;
    height: 0.3rem;
    background-color: cornflowerblue;
    margin: 0 auto;
    position: absolute;
    border-radius: 10px;
}

.inputs {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    padding: 1rem 0;
}

.input-box {
    display: flex;
    flex-direction: column;
    margin-bottom: 1.1rem;
}

.input-box input {
    margin: 0.6rem 0;
    padding: 0.8rem 1.2rem;
    border: none;
    border-radius: 10px;
    box-shadow: 1px 1px 6px #0000001c;
}

.input-box input:hover {
    background-color: #eeeeee75;
}

.input-box input:focus-visible {
    outline: 1px solid #6c63ff;
}

.input-box label {
    font-size: 1rem;
    font-weight: 600;
    color: black;
}


.continue-button button {
    width: 100%;
    margin-top: 2.5rem;
    border: none;
    background-color: #6c63ff;
    padding: 0.62rem;
    border-radius: 5px;
    cursor: pointer;
}

.continue-button button:hover {
    background-color: #6b63fff1;
}

.continue-button button a {
    text-decoration: none;
    font-size: 0.93rem;
    font-weight: 500;
    color: white
}

@media screen and (max-width: 1300px) {
    .form-image {
        display: none;
    }

    .container {
        width: 50%;
    }

    .formulario {
        width: 100%;
    }
}

/* 19 */
</style>

<script>
export default {
    name: "Cadastro",
    data() {
        return {
            nome: "",
            sobrenome: "",
            nickname: "",
            email: "",
            senha: "",
            confirmaSenha: "",
            caminhoFoto: null
        }
    },

    methods: {
        fazerCadastro() {
            const data =
            {
                nome: this.nome,
                sobrenome: this.sobrenome,
                email: this.email,
                nick: this.nickname,
                senha: this.senha,
                senha_confirma: this.confirmaSenha,
                foto: this.caminhoFoto,
                foto_ext: "jpeg"
            }

            api.criarUsuario(data);
            this.$router.push('/login')
        },
        login(){
            this.$router.push({name:'login'})
        },
        pickFile(e){
            const image = e.target.files[0];
                const reader = new FileReader();
                reader.readAsDataURL(image);
                reader.onload = e =>{
                    this.previewImage = e.target.result;
                    const posicaoVirgula = this.previewImage.indexOf(",");
                    const novaStr = this.previewImage.slice(posicaoVirgula + 1);
                    this.caminhoFoto = novaStr;
                    console.log(this.previewImage)
                    console.log(this.caminhoFoto)
                };
            }
        }
    }

</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue'
import Header from './Header.vue'
</script>