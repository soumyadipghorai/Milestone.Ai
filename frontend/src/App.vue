<template>
  <div>
    <header>
    </header>
    <div class="wrapper">
      
    </div>
    <RouterView></RouterView>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import login from './components/login.vue';
  import TheWelcome from './components/home.vue';
</script>

<style scoped>
  
</style>
