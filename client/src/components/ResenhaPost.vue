<template>
    <div>
        <div class="container-resenha">
            <RouterLink :to="pathObra" class="container-infos-obra">
                <div class="foto-obra">
                    <img :src="'https://image.tmdb.org/t/p/w500/' + poster" :alt="`poster ${titulo}`">
                </div>
                <h4> {{ titulo }} </h4>
            </RouterLink>
            <div class="container-infos-post">
                <RouterLink :to="retornaPerfil()" class="container-infos-usuario">
                    <div class="container-foto-perfil">
                        <img :src="foto" :alt="`foto ${nick}`">
                    </div>
                    <div class="container-nome-nick">
                        <div class="nome-usuario">
                            <h3> {{ nome }} </h3>
                        </div>
                        <div class="nick-usuario">
                            <h5>{{ nick }}</h5>
                        </div>
                    </div>
                </RouterLink>
                <div class="container-resenha-nota">
                    <div class="nota">
                        <img v-for="n in nota" src="https://cdn-icons-png.flaticon.com/512/148/148839.png">
                    </div>
                    <div class="resenha">
                        <p> {{ resenha??"" }} </p>
                    </div>
                </div>
                <a class="container-like" @click="darLike">
                    <p>{{ likes }}</p>
                    <img v-if="likado" class="botao-like" src="..\assets\heart_filled.png">
                    <img v-else class="botao-like" src="..\assets\heart_empty.png">
                </a>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container-resenha {
    margin: 10px 0px;
    padding-right: 20px;
    padding-bottom: 10px;
    background-color: white;
    width: 600px;
    min-height: 200px;
    border-radius: 10px;
    border: 1px solid #000000ba;
    flex-direction: row;
    display: flex;
}

.container-infos-obra {
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: #2C3E50;
    max-width: min-content;
    text-align: center;
}

.foto-obra img {
    border: 1px solid;
    border-radius: 3px;
    max-height: 150px;
}

.container-infos-post {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.container-infos-usuario {
    display: flex;
    flex-direction: row;
    align-items: center;
    text-decoration: none;
    color: #2C3E50;
}

.container-foto-perfil {
    height: 50px;
    width: 50px;
    margin: 10px;
    margin-right: 20px;
    border-radius: 100%;
    border: 1px solid black;
}

.container-like{
    align-self: flex-end;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: flex-end;
}

.botao-like{
    height: 20px;
    width: 20px;
    margin: 0px 5px;
}

.container-resenha-nota{
    margin-left: 10px;
    margin-bottom: 10px;
}

.nota img{
    height: 20px;
}

.resenha {
    text-align: justify;
    max-width: 450px;
    overflow: hidden;
    text-overflow: ellipsis;
}

</style>

<script>
export default {
    props: ['dadosUsuario', 'dadosObra', 'dadosResenha'],
    setup: (props) => {
        const { dadosUsuario, dadosObra, dadosResenha } = props
    },
    data() {
        return {
            titulo: '',
            poster: '',
            nome: '',
            nick: '',
            foto: '',
            resenha: '',
            pathObra: '',
            nota: null,
            likado: false,
            idObra: null,
            idUsuario: null
        };
    },
    created() {
        const infosResenha = this.dadosResenha;
        this.resenha = infosResenha.resenha;
        this.nota = infosResenha.nota;
        this.likes = infosResenha.curtidas;
        
        if (this.dadosObra === undefined){
            this.getObraAPI();
        } 
        else {
            this.titulo = this.dadosObra.title;
            this.poster = this.dadosObra.poster_path;
            this.idObra = this.dadosObra.id;
        }

        if (this.dadosUsuario === undefined){
            this.nome = this.dadosResenha.usuario.nome + ' ' + this.dadosResenha.usuario.sobrenome;
            this.nick = this.dadosResenha.usuario.nick;
            this.foto = 'http://127.0.0.1:8000/' + this.dadosResenha.usuario.caminho_foto;
            this.idUsuario = this.dadosResenha.usuario.id;
        } 
        else {
            this.nome = this.dadosUsuario.nome + ' ' + this.dadosUsuario.sobrenome;
            this.nick = this.dadosUsuario.nick;
            this.foto = 'http://127.0.0.1:8000/' + this.dadosUsuario.caminho_foto;
            this.idUsuario = this.dadosResenha.usuario.id;
        }

        this.retornaObra();
    },

    methods: {
        getObraAPI() {
            api.getFilmeID(this.dadosResenha.obra.id).then((res) => {
                this.titulo = res.title;
                this.poster = res.poster_path;
                this.idObra = res.id;
            });
        },
        retornaPerfil(){
            if (this.dadosUsuario === undefined){
                return `/perfil?dados=${encodeURIComponent(JSON.stringify(this.dadosResenha.usuario))}`
            }
            else{
                return `/perfil?dados=${encodeURIComponent(JSON.stringify(this.dadosUsuario))}`
            }
        },
        retornaObra(){
            if (this.dadosObra === undefined){
                api.getFilmeID(this.dadosResenha.obra.id).then((res) => {
                this.pathObra = `/obra?dados=${encodeURIComponent(JSON.stringify(res))}`
            });
            }
            else{
                this.pathObra = `/obra?dados=${encodeURIComponent(JSON.stringify(this.dadosObra))}`
            }
        },
        darLike(){
            if (!this.likado){
                api.darLikeResenha(localStorage.getItem('token'), this.idUsuario, this.idObra).then(() => {
                    this.likado = true;
                    this.likes = this.likes + 1;
                });
            }
        }
    }
};
</script>

<script setup>
import api from '../../services/api';
</script>