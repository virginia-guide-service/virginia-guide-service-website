<template>
  <div class="flex min-h-screen flex-col">
    <!-- Announcement Banner -->
    <WeatherAnnouncementBanner
      v-if="showBanner"
      @closed="showBanner = false"
    />

    <!-- Navbar -->
    <Navbar
      :class="[
        'fixed left-0 w-full z-50 transition-all duration-300',
        showBanner ? 'top-[130px]' : 'top-0'
      ]"
    />

    <main class="grow w-full overflow-y-auto">
      <NuxtPage />
    </main>
  </div>
</template>

<script>
import WeatherAnnouncementBanner from './components/WeatherAnnouncementBanner.vue'
import Navbar from './components/Navbar.vue'

export default {
  components: {
    WeatherAnnouncementBanner,
    Navbar
  },
  data() {
    return {
      showBanner: true
    }
  }
}
</script>
