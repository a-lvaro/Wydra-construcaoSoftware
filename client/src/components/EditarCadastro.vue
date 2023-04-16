<template>
    <div>
        <Header />
        <div class="cadastro">
            <div class="container">
                <div class="formulario">
                    <form @submit.prevent="editarInformacoes">
                        <div class="header-formulario">
                            <div class="titulo">
                                <h1>Editar Cadastro</h1>
                                <div style="margin-top: 20px;" class="input-box">
                                <label for="emailCadastro">Email </label>
                                <input placeholder=" Digite seu melhor email" type="emailCadastro" id="email" name="email"
                                    required v-model="email">
                            </div>
                            </div>
                            
                        </div>
                        <div class="inputs">
                            <div class="input-box">
                                <label for="name">Nome </label>
                                <input placeholder=" Digite seu nome" type="text" id="name" name="name"  v-model="nome">
                            </div>
    
                            <div class="input-box">
                                <label for="name">Sobrenome </label>
                                <input placeholder=" Digite seu sobrenome" type="text" id="name" name="name"  v-model="sobrenome">
                            </div>
            
                            <div class="input-box">
                                <label for="nickname">Apelido </label>
                                <input placeholder=" Digite seu nickname" type="text" id="nickname" name="nickname" 
                                    v-model="nick">
                            </div>
                            
                            <div class="input-box">
                                <label for="passwordCadastro">Senha </label>
                                <input placeholder=" Digite sua senha" type="password" id="passwordCadastro"
                                    name="passwordCadastro"  v-model="senha">
                            </div>
    
                            <div class="input-box">
                                <label for="confirmaSenha">Confirme sua Senha </label>
                                <input placeholder=" Digite sua senha novamente" type="password" id="confirmaSenha"
                                    name="confirmaSenha"  v-model="confirmaSenha">
                            </div>
                        </div>
    
                        <div class="continue-button">
                            <Botao texto="Continuar" />
                        </div>
                    </form>
                </div>
                <div class="form-image">
                    <img src="team_up.svg" alt="cadastro">
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.cadastro {
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    width: 80%;
    height: 80vh;
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
    display: inline-grid;
    grid-template-columns: auto auto auto;
    flex-wrap: wrap;
    justify-content: space-between;
    padding: 1rem 0;
}

.input-box {
    display: flex;
    margin-right: 10px;
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
    name: "EditarCadastro",
    data() {     
        return {
                nome: null,
                sobrenome:null,
                nick: null,
                caminhoFoto: "",
                senha: null,
                confirmaSenha: "",
                usuario: null,
            }
        },
        
    created(){
        api.getUsuarioLogado(localStorage.getItem('token'))
        .then((res)=> {
            const dados = res;
            this.nome = dados.nome,
            this.sobrenome= dados.sobrenome,
            this.nick = dados.nick,
            this.caminhoFoto = dados.caminho_foto,
            // this.senha = dados.senha,
            // this.confirmaSenha =  dados.senha_confirma,
            this.usuario = res
        })
    },

    methods: {
        editarInformacoes(){
            const data = {
                nome: this.nome,
                sobrenome: this.sobrenome,
                nick: this.nick,
                caminho_foto: "",
                email: this.email,
                senha: this.senha,
                senha_confirma: this.confirmaSenha
            }
            api.editarCadastro(data, localStorage.getItem('token'));
            this.$router.push(`/perfil?dados=${encodeURIComponent(JSON.stringify(this.usuario))}`);
        },
        
    },
}
</script>

<script setup>
import api from '../../services/api.js'
import Botao from './Botao.vue'
import Header from './Header.vue'
</script>