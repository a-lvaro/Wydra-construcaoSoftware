<template>
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
                                <RouterLink to="/login">Entrar</RouterLink>
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
                            <input placeholder=" Digite seu sobrenome" type="text" id="name" name="name" required
                                v-model="sobrenome">
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

                        <!-- <div class="input-box">
                            <label for="name">Telefone </label>
                            <input placeholder=" (xx) xxxxx-xxxx" type="tel" id="telefone" name="telefone" required
                                v-model="telefone">
                        </div> -->

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
                    </div>

                    <!-- <div class="gender-inputs">
                        <div class="genero-titulo">
                            <h6>Gênero</h6>
                        </div>
                        <div class="gender-group">
                            <div class="gender-input">
                                <input type="radio" id="female" name="gender">
                                <label for="female">Feminino</label>
                            </div>

                            <div class="gender-input">
                                <input type="radio" id="male" name="gender">
                                <label for="male">Masculino</label>
                            </div>

                            <div class="gender-input">
                                <input type="radio" id="others" name="gender">
                                <label for="others">Outros</label>
                            </div>

                            <div class="gender-input">
                                <input type="radio" id="none" name="gender">
                                <label for="none">Prefiro não dizer</label>
                            </div>
                        </div>
                    </div> -->
                    <div class="continue-button">
                        <!-- <button><a href="#">Continuar</a></button> -->
                        <Botao texto="Continuar" />
                    </div>
                </form>
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

.botao-entrar {
    display: flex;
    align-items: center;
}

.botao-entrar button {
    border: none;
    background-color: #6c63ff;
    padding: 0.5rem 5rem;
    border-radius: 5px;
    cursor: pointer;
}

.botao-entrar button:hover {
    background-color: #6c63ff;
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
    background-color: #6c63ff;
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

.input-box label,
.gender-inputs h6 {
    font-size: 1rem;
    font-weight: 600;
    color: black;
}

.gender-group {
    display: flex;
    justify-content: space-between;
    margin-top: 0.62rem;
    padding: 0 0.5rem
}

.gender-input {
    display: flex;
    align-items: center;
}

.gender-input input {
    margin-right: 0.35rem;
}

.gender-input label {
    margin-right: 2rem;
    font-size: 0.81rem;
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
            confirmaSenha: ""
        }
    },

    methods: {
        fazerCadastro() {
            const data =
            {
                nome: this.nome,
                sobrenome: this.sobrenome,
                nick: this.nickname,
                email: this.email,
                senha: this.senha,
                senha_confirma: this.confirmaSenha
            }
            
            console.log(data)

            return fetch('http://127.0.0.1:8000/user/signup', {
                method: 'POST',
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data),
            })
                .then((res) => res.json());
        },
    },
}
</script>

<script setup>
import Botao from './Botao.vue'
</script>