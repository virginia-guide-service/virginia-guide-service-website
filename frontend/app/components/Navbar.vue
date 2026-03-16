<template>
  <div>
    <!-- Mobile Navbar -->
    <div
      :class="[
        'xl:hidden flex items-center justify-between w-full px-4 py-2 transition-all duration-500 ease-in-out bg-white/30 backdrop-blur-lg text-black',
        navOpen ? 'opacity-0 pointer-events-none translate-y-[-10px]' : 'opacity-100 translate-y-0'
      ]"
    >
      <!-- Logo (Left) -->
      <a href="/" class="flex items-center space-x-2">
        <img class="h-12 w-12" width="48" height="48" src="https://virginia-guides-website-images.s3.amazonaws.com/public/guides-logo.png" alt="Virginia Guides Logo" fetchpriority="high" />
      </a>

      <!-- Hamburger Button (Right) -->
      <div class="flex items-center gap-x-3">
        <p @click="navOpen = !navOpen" v-if="!navOpen" class="font-['Montserrat']  font-medium transition-all duration-300 cursor-pointer">MENU</p>
        <button @click="navOpen = !navOpen" class="focus:outline-none">
          <svg
            v-if="!navOpen"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="text-black size-7"
          >
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    <transition name="fade-slide" appear>
      <nav
        v-if="navOpen"
        class="fixed inset-0 z-50 xl:hidden bg-white/80 backdrop-blur-lg text-black flex flex-col justify-center items-center space-y-6 transition-all duration-500 ease-in-out"
      >
        <!-- Close Button (Top Right) -->
        <div class="absolute top-6 right-6">
          <button @click="navOpen = false" class="focus:outline-none">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-8 h-8 text-black hover:text-orange-500 transition-colors duration-200"
            >
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Navigation Links -->
        <div class="flex flex-col justify-center items-center h-full text-center space-y-6">
          <a href="/about-tours" class="font-['Montserrat'] uppercase text-2xl font-medium hover:text-orange-500 transition-colors duration-200" @click="navOpen = false">About Tours</a>
          <a href="/join-guides" class="font-['Montserrat'] uppercase text-2xl font-medium hover:text-orange-500 transition-colors duration-200" @click="navOpen = false">Join Guides</a>
          <a href="/for-educators" class="font-['Montserrat'] uppercase text-2xl font-medium hover:text-orange-500 transition-colors duration-200" @click="navOpen = false">For Educators</a>
          <a href="/feedback" class="font-['Montserrat'] uppercase text-2xl font-medium hover:text-orange-500 transition-colors duration-200" @click="navOpen = false">Feedback</a>
          <a href="/donate" class="font-['Montserrat'] uppercase text-2xl font-medium hover:text-orange-500 transition-colors duration-200" @click="navOpen = false">Donate</a>
          <a href="/your-visit" class="font-['Montserrat'] uppercase text-2xl font-semibold text-orange-500 hover:text-orange-700 transition-colors duration-200 pt-4 border-t border-orange-500 active:scale-95" @click="navOpen = false">Take a Tour</a>
        </div>
      </nav>
    </transition>

    <!-- Desktop Navbar (with scroll effect) -->
    <header
      :class="[
        'hidden xl:flex w-full z-50 transition duration-350 items-center justify-between px-4 py-2',
        isScrolled
          ? 'bg-white/30 shadow-md backdrop-blur-md text-black'
          : 'bg-transparent text-white'
      ]"
    >
      <!-- Logo (Left Side) -->
      <a href="/" class="flex items-center space-x-2">
        <img class="h-12 w-12" width="48" height="48" src="https://virginia-guides-website-images.s3.amazonaws.com/public/guides-logo.png" alt="Virginia Guides Logo" fetchpriority="high" />
      </a>

      <!-- Navigation Links (Right Side) -->
      <div class="flex items-center gap-x-6">
        <a href="/about-tours" class="nav-link font-['Montserrat'] font-medium px-5 py-2 cursor-pointer">ABOUT TOURS</a>
        <a href="/join-guides" class="nav-link font-['Montserrat'] font-medium px-5 py-2 cursor-pointer">JOIN GUIDES</a>
        <a href="/for-educators" class="nav-link font-['Montserrat'] font-medium px-5 py-2 cursor-pointer">FOR EDUCATORS</a>
        <a href="/feedback" class="nav-link font-['Montserrat'] font-medium px-5 py-2 cursor-pointer">FEEDBACK</a>
        <a href="/donate" class="nav-link font-['Montserrat'] font-medium px-5 py-2 cursor-pointer">DONATE</a>
        <a href="/your-visit">
          <button class="font-['Montserrat'] font-medium text-white bg-UVA-orange hover:bg-orange-800 hover:scale-105 rounded-full px-5 py-2 cursor-pointer transition duration-250 active:scale-95">
            TAKE A TOUR
          </button>
        </a>
      </div>
    </header>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const navOpen = ref(false)
const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 200
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style>
  .fade-slide-enter-active,
  .fade-slide-leave-active {
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .fade-slide-enter-from,
  .fade-slide-leave-to {
    opacity: 0;
    transform: translateY(-20px);
  }
  .fade-slide-enter-to,
  .fade-slide-leave-from {
    opacity: 1;
    transform: translateY(0);
  }

  .nav-link {
    position: relative;
    padding-bottom: 4px;
  }
  .nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 1.25rem;
    width: 0;
    height: 2px;
    background-color: currentColor;
    transition: width 0.3s ease;
  }
  .nav-link:hover::after {
    width: calc(100% - 2.5rem);
  }
</style>
