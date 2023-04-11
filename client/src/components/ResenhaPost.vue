<template>
    <div>
        <div class="container-resenha">
            <div class="container-infos-obra">
                <div class="foto-obra">
                    <img :src="foto" :alt="`poster ${titulo}`">
                    <!-- <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`poster ${titulo}`"> -->
                </div>
                <h3> {{ titulo }} </h3>
            </div>
            <div class="container-infos-post">
                <div class="container-infos-usuario">
                    <div class="container-foto-perfil">
                        <!-- <img :src="'https://image.tmdb.org/t/p/w500/' + foto" :alt="`foto ${nick}`"> -->
                    </div>
                    <div class="container-nome-nick">
                        <div class="nome-usuario">
                            <h3> {{ nome }} </h3>
                        </div>
                        <div class="nick-usuario">
                            <h5>{{ nick }}</h5>
                        </div>
                    </div>
                </div>
                <div class="container-resenha-nota">
                    <div class="nota">
                        <img v-for="n in nota" src="https://cdn-icons-png.flaticon.com/512/148/148839.png">
                    </div>
                    <div class="resenha">
                        <p> {{ resenha??"" }} </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container-resenha {
    margin-top: 10px;
    padding-right: 20px;
    background-color: white;
    width: 600px;
    min-height: 300px;
    border-radius: 20px;
    border: 2px solid #000000ba;
    flex-direction: row;
    display: flex;
    /* align-items: center; */
}

.container-infos-obra {
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
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
}

.container-foto-perfil {
    height: 50px;
    width: 50px;
    margin: 10px;
    margin-right: 20px;
    border-radius: 100%;
    border: 1px solid black;
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
            titulo: 'shrek',
            foto: 'https://a-static.mlcdn.com.br/1500x1500/poster-cartaz-shrek-terceiro-pop-arte-poster/poparteskins2/15938523793/11b7dfef967c3668a49c679cd55c8dd7.jpeg',
            nome: 'joao',
            nick: 'jj',
            resenha: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N',
            nota: 5
        };
    },
    // created() {
    //     const infosResenha = this.dadosResenha;
    //     this.resenha = infosResenha.resenha;
    //     this.nota = infosResenha.nota;
    //     const infosObra = this.dadosObra??this.getObraAPI();
    //     const infosUsuario = this.dadosUsuario??this.getUsuarioAPI();
    // },
    // methods: {
    //     setObra() {
    //         const infosObra = this.dadosObra;
    //         this.titulo = infosObra.titulo;
    //         this.foto = infosObra.foto;
    //     },
    //     setUsuario() {
    //         const infosUsuario = this.dadosUsuario;
    //         this.nome = infosUsuario.nome;
    //         this.nick = infosUsuario.nick;
    //     },
    //     // getObraAPI() {
    //     //     const infosObra = 0;
    //     //     api.getFilmeID(this.dadosResenha.obra.id).then((res) => {
    //     //         infosObra = res.data;
    //     //     });
    //     // },
    //     // getUsuarioAPI() {
    //     //     const infosUsuario =0;
    //     // }
    // }
};
</script>

<script setup>
import api from '../../services/api';
</script>