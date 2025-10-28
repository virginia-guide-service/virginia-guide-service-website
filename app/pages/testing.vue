<script setup>
  const { data, error } = await useFetch('http://127.0.0.1:8000/api/hello/')
  import NavbarTest from '~/components/NavbarTest.vue';
  import ExploreUVAHistoryBlue from '~/components/ExploreUVAHistoryBlue.vue';
</script>

<template>
  <ExploreUVAHistoryBlue />
  <NavbarTest />
  <div>
    <p v-if="error">Error: {{ error.message }}</p>
    <p v-else>{{ data?.message }}</p>
  </div>
</template>