<template>
  <div class="flex min-h-screen flex-col">

    <!-- Navbar stays fixed at the top -->
    <Navbar class="fixed top-0 left-0 w-full z-50" />

    <!-- Main content area below navbar -->
    <main class="grow w-full overflow-y-auto">
      <NuxtPage />
    </main>

  </div>
</template>

<script>
  // Importing the Navbar component
  import Navbar from './components/Navbar.vue';

  export default {
    // Register the Navbar component for use in this template
    components: {
      Navbar
    }
  };
</script>

<style scoped>
  /* Ensures the body and app container take up the full screen height */
  html, body, #app {
    height: 100%; /* Full height */
    margin: 0;    /* Remove default margin */
  }
</style>