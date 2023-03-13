<template >
    <div>
        <body >
            <form class="retangulo-cadastro">
                <img src="../../wydra.png" class="lontra" alt="lontrinha">
                <!-- <label for="nickname">Nome de Usuário:</label>
          <input type="nickname" id="nickname" name="nickname" required v-model="nickname"/>
          
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" required v-model="email"/>
          
          <label for="password">Senha:</label>
          <input type="password" id="password" name="password" required v-model="senha"/>
          
          <label for="confirmarSenha">Confirme sua senha:</label>
          <input type="confirmarSenha" id="confirmarSenha" name="confirmarSenha" required v-model="confirmarSenha"/> -->

                <label for="estado">Estado:</label>
                <select id="estado" name="estado">
                    <option value="">Selecione um estado</option>
                    <option value="AC">Acre</option>
                    <option value="AL">Alagoas</option>
                    <option value="AP">Amapá</option>
                    <option value="AM">Amazonas</option>
                    <option value="BA">Bahia</option>
                    <option value="CE">Ceará</option>
                    <option value="DF">Distrito Federal</option>
                    <option value="ES">Espírito Santo</option>
                    <option value="GO">Goiás</option>
                    <option value="MA">Maranhão</option>
                    <option value="MT">Mato Grosso</option>
                    <option value="MS">Mato Grosso do Sul</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="PA">Pará</option>
                    <option value="PB">Paraíba</option>
                    <option value="PR">Paraná</option>
                    <option value="PE">Pernambuco</option>
                    <option value="PI">Piauí</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="RN">Rio Grande do Norte</option>
                    <option value="RS">Rio Grande do Sul</option>
                    <option value="RO">Rondônia</option>
                    <option value="RR">Roraima</option>
                    <option value="SC">Santa Catarina</option>
                    <option value="SP">São Paulo</option>
                    <option value="SE">Sergipe</option>
                    <option value="TO">Tocantins</option>
                </select>

                <!-- <button type="submit" >Cadastrar</button> -->
            </form>
        </body>
    </div>
</template>

<script>
export default {
    name: "Cadastro",
    data() {
        return {
            Nickname: '',
            email: '',
            senha: '',
            confirmarSenha: '',
            telefone: '',
            estado: '',
        }
    }
}
</script>

<style>
body {
    background-color: rgba(0, 0, 0, 0.442);
}

.retangulo-cadastro {
    margin: 50px auto;
    background-color: white;
    width: 520px;
    height: 800px;
    border-radius: 20px;
    /* Define o raio da borda */
    border: 2px solid #000000ba;
    /* Define a cor e largura da borda */
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

input[type="email"],
input[type="password"],
input[type="nickname"],
input[type="confirmarSenha"] {
    padding: 12px;
    align-content: center;
    margin-bottom: 30px;
    border: 3px solid #0c0909;
    border-radius: 10px;
    width: 100%;
    max-width: 320px;
    box-sizing: border-box;
}</style>