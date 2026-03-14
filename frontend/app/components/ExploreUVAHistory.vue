<template>
  <section :class="['py-16 sm:py-20 md:py-24', blue ? 'bg-royal-blue' : 'bg-white']">
    <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">

      <h1 class="scrollElement font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
        Explore UVA History
      </h1>

      <p :class="['scrollElement font-[\'Montserrat\'] text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto', blue ? 'text-white' : 'text-black']">
        In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
        which focus on a specific aspect of UVA's extensive 200 year history.
      </p>

      <a href="/about-tours" class="scrollElement">
        <button :class="['inline-flex items-center space-x-3 rounded-full border-1 font-[\'Montserrat\'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-royal-blue hover:bg-gray-100 hover:scale-105 transition-all duration-300 ease-in-out hover:cursor-pointer', blue ? 'text-white border-white' : 'text-black border-gray-300']">
          <span>HISTORY TOURS</span>
          <svg class="flex-shrink-0" height="25px" width="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6 12H18M18 12L13 7M18 12L13 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </a>
    </div>

    <div class="scrollElement history-carousel-wrapper mt-12">
      <div class="history-slider">
        <div class="history-track">

          <div v-for="n in 2" :key="n" class="history-group">

            <a v-for="(tour, index) in specialtyTours"
               :key="index"
               :href="tour.link"
               class="history-slide">

              <div class="image-container">
                <img :src="tour.image" :alt="tour.title" loading="lazy" class="tour-img">
              </div>

              <p :class="['tour-label', blue ? 'text-white' : 'text-black']">{{ tour.title }}</p>
            </a>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  blue: {
    type: Boolean,
    default: false
  }
});

/**
 * ADD/EDIT TOURS HERE
 */
const specialtyTours = [
  {
    title: "History of Women at UVA",
    link: "/about-tours/#history-of-women-at-uva-tour",
    image: "https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg"
  },
  {
    title: "History of African-Americans at UVA",
    link: "/about-tours/#history-of-african-americans-tour",
    image: "https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg"
  },
  {
    title: "Garden Tours",
    link: "/about-tours/#garden-tours",
    image: "https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg"
  },
  {
    title: "Memorial to Enslaved Laborers",
    link: "/about-tours/#MEL-tour",
    image: "https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg"
  },
  {
    title: "Children's Tour",
    link: "/about-tours/#childrens-tours",
    image: "https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg"
  }
];
</script>

<style scoped>
    .history-carousel-wrapper {
        width: 100%;
        overflow: hidden;
        padding: 20px 0;
    }
    .history-slider {
        display: flex;
        width: 100%;
    }
    .history-track {
        display: flex;
        width: max-content;
        animation: scroll-history 25s linear infinite;
    }
    .history-track:hover {
        animation-play-state: paused;
    }
    .history-group {
        display: flex;
        gap: 1.5rem;
        padding-right: 1.5rem;
    }
    .history-slide {
        width: 350px;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        gap: 12px;
        transition: transform 0.3s ease;
    }
    .image-container {
        width: 100%;
        height: 250px;
        overflow: hidden;
        position: relative;
    }
    .tour-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .tour-label {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        text-align: left;
        transition: color 0.3s ease;
    }
    .history-slide:hover .tour-img {
        transform: scale(1.1);
    }
    .history-slide:hover .tour-label {
        color: #E57200;
    }
    @media (max-width: 1023px) {
        .history-slide { width: 280px; }
        .image-container { height: 220px; }
    }
    @media (max-width: 639px) {
        .history-slide { width: 220px; }
        .image-container { height: 180px; }
        .tour-label { font-size: 0.85rem; }
    }
    @keyframes scroll-history {
        0%   { transform: translateX(-50%); }
        100% { transform: translateX(0%); }
    }
</style>
