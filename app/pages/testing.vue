<script setup>
const { data, error } = await useFetch('http://127.0.0.1:8000/api/hello/')
</script>

<template>
  <div>
    <p v-if="error">Error: {{ error.message }}</p>
    <p v-else>{{ data?.message }}</p>
  </div>
</template>