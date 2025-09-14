<template>
    <!-- Header container with padding and flexbox for layout -->
    <header
      :class="[
        'fixed top-0 left-0 w-full z-50 transition-all',
        isScrolled ? 'bg-white/30 shadow-md backdrop-blur-md text-black' : 'bg-transparent text-white'
      ]"
      class="flex items-center justify-between px-4 py-2"
    >  
      <!-- Logo (Right side) -->
      <div class="flex items-center space-x-2">
        <a href="/">
          <img class="h-15 w-15" src="/guides-logo.png" alt="Virginia Guides Logo">
        </a>
        <!-- <button class="font-['Montserrat']font-medium bg-transparent hover:bg-royal-blue hover:text-white hover:border-none cursor-pointer rounded-sm px-3 py-1 transition duration-300">
          HOME
        </button> -->
      </div>
  
      <!-- Navigation Link Container (Left Side) -->
      <div class="flex items-center space-x-6">
  
        <a href="/about-tours">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer rounded-sm px-3 py-3 transition duration-500">
            ABOUT TOURS
          </button>
        </a>
  
        <a href="/join-guides">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer rounded-sm px-3 py-3 transition duration-500">
            JOIN GUIDES
          </button>
        </a>

        <a href="/for-educators">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer rounded-sm px-3 py-3 transition duration-500">
            FOR EDUCATORS
          </button>
        </a>
  
        <a href="/feedback">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer rounded-sm px-3 py-3 transition duration-500">
            FEEDBACK
          </button>
        </a>

        <a href="/donate">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer rounded-sm px-3 py-3 transition duration-500">
            DONATE
          </button>
        </a>
  
        <a href="/your-visit">
          <button class="font-['Montserrat'] font-medium bg-transparent hover:bg-royal-blue hover:text-white cursor-pointer border hover:border-royal-blue rounded-full px-4 py-2 transition duration-500">
            TAKE A TOUR
          </button>
      </a>
      </div>
  
    </header>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  
  const isScrolled = ref(false)
  
  const handleScroll = () => {
    isScrolled.value = window.scrollY > 200 // adjust threshold as needed
  }
  
  onMounted(() => {
    window.addEventListener('scroll', handleScroll)
  })
  
  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
  })
  </script>
  