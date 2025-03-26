<template>
    <h1 class="title">Intuitive Care Test</h1>
    <div class="container__search">
        <input 
        v-model="buscaOperadora" 
        @keydown.enter="handleSearch"
        type="text" 
        class="input__search" 
        placeholder="Razão social da operadora">
        <button 
        @click="handleSearch" 
        class="btn__search">Pesquisar</button>
    </div>
    <ul class="list__cards" v-if="isOperadoraFound && operadoras.length > 0">
        <OperadoraCard  v-for="(operadora, index) of operadoras"
        :key="index"
        :cnpj="operadora.cnpj"
        :razao_social="operadora.razao_social"
        :cep="operadora.cep"
        :ddd="operadora.ddd"
        :telefone="operadora.telefone"
        :endereco_eletronico="operadora.endereco_eletronico"
        ></OperadoraCard>
    </ul>
    <p class="not__found" v-if="!isOperadoraFound">Operadora não encontrada!</p>
</template>

<script setup lang="ts">

import { getOperadora } from '../services/getOperadora';
import OperadoraCard from './OperadoraCard.vue';
import { ref } from 'vue';
import type { Operadora } from '../services/getOperadora';

const operadoras = ref<Operadora[]>([]);
const buscaOperadora = ref('');
const isOperadoraFound = ref(true)

const handleSearch = async () => {
    if (buscaOperadora.value.length <= 0) return;
    try {
        operadoras.value = await getOperadora(buscaOperadora.value);
        isOperadoraFound.value = operadoras.value.length > 0;
    } catch (e){
        alert(e);
    }
}

</script>

<style scoped>
.title{
    font-size: 4rem;
    text-align: center;
    margin: 4vh 0;
}
.container__search{
    display: flex;
    justify-content: center;
    margin: 5vh 2vw;
}

.input__search{
    font-size: 2rem;
    border-radius: 8px;
    border: 3px solid #ccc;
    padding: 1vw 1vh;
    width: 70vw;
    margin-right: 3vw;
    -webkit-transition: 0.5s;
    transition: 0.5s;
    outline: none;
}

.input__search:focus {
  border: 3px solid #555;
}

.btn__search{
    font-size: 2rem;
    border-radius: 8px;
    background-color: #fff;
    border: 1px solid #fff;
    padding: 1vw 1vh;
    -webkit-transition: 0.5s;
    transition: 0.5s;
}

.btn__search:hover{
    cursor: pointer;
    border-color: #555;
}

.not__found{
    font-size: 3rem;
    text-align: center;
    font-weight: 600;
}

@media (min-width: 768px) {
    .list__cards{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        padding: 0 5vw;
    }

    .input__search{
        margin-right: 2vw;
    }

    .btn__search{
        width: 10vw;
    }
}

</style>
