<template>
    <li class="card">
        <h3 class="titulo">{{ razao_social }}</h3>
        <p class="cnpj"><b class="subtitle">CNPJ: </b>{{cnpj}}</p>
        <p class="cep"><b class="subtitle">CEP: </b>{{cep}}</p>
        <p class="telefone"><b class="subtitle">Telefone: </b>({{ddd}}) {{telefone}}</p>
        <p class="email"><b class="subtitle">E-mail: </b>{{endereco_eletronico}}</p>
    </li>

</template>

<script setup lang="ts">

const props = defineProps({
    cnpj: {
        type: String,
        required: true
    },
    razao_social: {
        type: String,
        required: true
    },
    cep: {
        type: String,
        required: true
    },
    ddd: {
        type: String,
        required: true
    },
    telefone: {
        type: String,
        required: true
    },
    endereco_eletronico: {
        type: String,
        required: true
    }
})

</script>

<style scoped>

.card{
    background-color: bisque;
    width: 90%;
    padding: 2vh 2vw;
    border-radius: 8px;
    display: block;
    margin: 2vh auto;
}

.titulo{
    font-size: 2rem;
    text-align: center;
}

.cnpj, .cep, .telefone, .email, .subtitle{
    font-size: 1.5rem;
    text-align: center;
    margin: 0.8vh 0;
}

</style>
