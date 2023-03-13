<template>
<body class="cadastro">
    
    <div class="container">
        <div class="form-image">
            <img src="join.svg" alt="cadastro">
        </div>
        <div class="formulario">
            <form action="#">
                <div class="header-formulario">
                    <div class="titulo">
                        <h1>Cadastre-se</h1>
                    </div>
                    <div class="botao-cadastro">
                        <button><a href="#">Cadastrar</a></button>
                    </div>
                </div>
                <div class="inputs">
                    <div class="input-box">
                        <label for="firstname">Primeiro Nome </label>
                        <input placeholder=" Digite seu primeiro nome" type="text" id="firstname" name="firstname" required v-model="primeiroNome">
                    </div>

                    <div class="input-box">
                        <label for="lastname">Sobrenome </label>
                        <input placeholder=" Digite seu sobrenome" type="text" id="lastname" name="lastname" required v-model="sobrenome">
                    </div>

                    <div class="input-box">
                        <label for="emailCadastro">Email </label>
                        <input placeholder=" Digite seu melhor email" type="emailCadastro" id="email" name="email" required v-model="email">
                    </div>

                    <div class="input-box">
                        <label for="telefone">Telefone </label>
                        <input placeholder=" (xx) xxxxx-xxxx" type="tel" id="telefone" name="telefone" required v-model="telefone">
                    </div>

                    <div class="input-box">
                        <label for="passwordCadastro">Senha </label>
                        <input placeholder=" Digite sua senha" type="passwordCadastro" id="passwordCadastro" name="passwordCadastro" required v-model="senha">
                    </div>

                    <div class="input-box">
                        <label for="confirmaSenha">Confirme sua Senha </label>
                        <input placeholder=" Digite sua senha novamente" type="confirmaSenha" id="confirmaSenha" name="confirmaSenha" required v-model="confirmaSenha">
                    </div> 
                </div>

                <div class="genero-inputs">
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
                </div>
                <div class="continue-button">
                    <button><a href="#">Continuar</a></button>
                </div>
            </form>
        </div>
    </div>
</body>
</template>

<script>
export default {
    name:"Cadastro",
    data() {
        return{
            
        }
    }
}
</script>

<style>
   * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
   } 

   .cadastro{
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    /* background: #0c0ce94d; */
    background: white;
   }

   .container{
    width: 80%;
    height: 80vh;
    display: flex;
    box-shadow: 10px 5px 10px rgba(0,0,0, .212);
   }

</style>