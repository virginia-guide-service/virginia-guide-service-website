<!-- <template> -->
  <!-- Main wrapper that contains the navbar and main content area (full screen height) -->
  <!-- <div class="flex h-screen"> -->

    <!-- Main content area (flexible, grows to fill available space) -->
    <!-- <div class="flex flex-col flex-grow h-full"> -->

      <!-- Main content (loads different pages based on the router and scrollable) -->
      <!-- <main class="w-full h-full"> -->
        <!-- Navbar component (full width, appears at the top and fixed at the top) -->
        <!-- <Navbar class="absolute top-0 left-0 w-full z-50" /> -->

        <!-- <router-view /> The router view renders different pages here -->
        <!-- <NuxtPage /> -->
      <!-- </main> -->
    <!-- </div>
  </div>
</template> -->

<template>
  <div class="flex min-h-screen flex-col">

    <!-- Navbar stays fixed at the top -->
    <Navbar class="fixed top-0 left-0 w-full z-50" />

    <!-- Main content area below navbar -->
    <main class="flex-grow w-full overflow-y-auto">
      <NuxtPage />
    </main>

  </div>
</template>

<script>
  // Importing the Sidebar and Navbar components to be used in this layout
  import Navbar from './components/Navbar.vue';

  export default {
    // Register the Navbar components for use in this template
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