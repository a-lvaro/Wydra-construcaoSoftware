<template>
    <div class="retangulo-resenha">
        <div class="foto-obra">
            <img :src="'https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg'">
        </div>
        <div >
            <div >
                <label  for="resenha" style="font-size: large;">Digite sua resenha: (opcional)</label>
                    <br>
                        <textarea  style="font-size: medium;" class = "campo" id="resenha" name="resenha" rows="14" cols="60"></textarea>
                        <!-- A tag <textarea> cria um campo de entrada de texto multilinha -->
                            <br>
                            <label style = "font-size: large;" for="nota">Digite sua nota (0 a 10):</label>
                            <br>
                            <input type="number" id="nota" name="nota" min="0" max="10" step="1">
                    <br>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.retangulo-resenha {
    margin: 50px auto;
    padding-right: 20px;
    background-color: white;
    width: 900px;
    min-height: 420px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    flex-direction: row;
    display: flex;
    align-items: center;
    overflow-x: auto;
}

#nota{
        height: 40px; /* Altura do campo de entrada */
        width: 150px;
        align-items: center;
        border-radius: 10px; /* Raio das bordas do campo de entrada */
        padding: 5px; /* Espaçamento interno do campo de entrada */
        font-size: 16px; /* Tamanho da fonte do campo de entrada */
}

.foto-obra {
    margin: 30px;
    border: 2px solid;
    border-radius: 3px;
    display: flex;
}

.foto-obra img{
    max-height: 400px;
}

.campo {
    font-size: larger;
}

</style>