<template>
        <!--Header Section-->
        <header class="relative overflow-visible h-[110vh] w-full bg-[url('/home-header-not-cropped.png')] bg-cover bg-center md:bg-left sm:bg-center" aria-label="Virginia Guides Hero Section">
        <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
            <h1 class="font-['Playfair_Display'] italic whitespace-nowrap text-[clamp(2.5rem,9vw,5rem)] leading-tight">
                VIRGINIA GUIDES
            </h1>
            <p class="font-['Roboto'] text-base sm:text-lg md:text-xl font-semibold leading-snug">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
            <button class="font-['Roboto'] mt-15 px-6 py-2 text-lg text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 border hover:border-neutral-300 rounded-full cursor-pointer transition duration-300"
            aria-label="Explore Virginia Guides">
                Plan Your Visit
            </button>
        </div>
    </header>

    <!-- Carousel -->
    <div class="w-full overflow-hidden mt-10">
        <div class="slider" style="
            --width: 350px;
            --height: 250px;
            --quantity: 5;
        ">
            <div class="list text-white font-light font-['Roboto']">
                <div class="item" style="--position: 1">
                    <img src="/UVAhistoryCarousel_womenatuva.jpg" alt="">
                    <p>History of Women</p>
                </div>
                <div class="item" style="--position: 2">
                    <img src="/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                    <p>History of African-Americans</p>
                </div>
                <div class="item" style="--position: 3">
                    <img src="/UVAhistoryCarousel_GardenTours.jpg" alt="">
                    <p>Garden Tours</p>
                </div>
                <div class="item" style="--position: 4">
                    <img src="/UVAhistoryCarousel_MEL.jpeg" alt="">
                    <p>Memorial to Enslaved Laborers</p>
                </div>
                <div class="item" style="--position: 5">
                    <img src="/UVAhistoryCarousel_childrenstour.jpg" alt="">
                    <p>Children's Tours</p>
                </div>
            </div>
        </div>
    </div>

    <!-- More Tour Info Section -->
    <section class="bg-white">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
            <div class="flex flex-col md:flex-row items-start md:items-center gap-10">
            
                <!-- Left: Text -->
                <div class="w-full md:w-3/5">
                    <p class="font-['Playfair_Display'] italic font-bold text-dark-green text-4xl sm:text-5xl leading-tight mb-6">
                        Where The Past Stands<br />
                        And More Is Told.
                    </p>
                    <p class="font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                        The American promise rests on the idea that all are created equal, and every story has a place in that legacy. 
                        Many who have shaped this University had long gone unrecognized. As we learn more, 
                        <span class="text-dark-green font-semibold italic">our tours evolve — not to change the past, but to share more of it.</span>
                        <br /><br />
                        Jefferson's Academical Village is more than its founding. From the history of enslavement to 
                        liberation, desegregation to coeducation, it shapes and reflects the American story, recognized by UNESCO for this role, 
                        and is made richer as we share more.
                        <br /><br />
                        <span class="font-medium italic">With this mission, </span>
                        <span class="italic underline">all tours are offered free of charge.</span>
                    </p>
                </div>

                <!-- Right: Image with Text Overlay -->
                <div class="w-full md:w-2/5 flex justify-center md:justify-end">
                    <div class="relative w-full max-w-sm sm:max-w-md h-[573px] overflow-hidden rounded-[35px] shadow-lg">

                        <!-- Background Image -->
                        <img
                        src="/1800UVA1.jpg"
                        alt="Tour illustration"
                        class="absolute inset-0 w-full h-full object-cover rounded-[35px]"
                        loading="lazy"
                        />

                        <!-- Overlay: Tour Times with Clock Icon -->
                        <div class="absolute top-[116px] left-6 w-52 h-16 flex items-center gap-2 text-left">
                            <!-- Clock Icon -->
                            <svg viewBox="0 0 24 24" fill="none" class="w-6 h-6" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 7V12L14.5 13.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>

                            <!-- Tour Times Text -->
                            <p class="text-stone-800 text-2xl font-bold font-['Montserrat']">TOUR TIMES*</p>
                        </div>

                        <!-- Overlay: Days and Times -->
                        <div class="absolute top-[179px] left-12 w-36 text-left">
                            <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">FRIDAY</p>
                            <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                        </div>
                        <div class="absolute top-[234px] left-12 w-36 text-left">
                            <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SATURDAY</p>
                            <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                        </div>
                        <div class="absolute top-[289px] left-12 w-36 text-left">
                            <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SUNDAY</p>
                            <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                        </div>

                        <!-- Footer Note -->
                        <div class="absolute bottom-4 left-1/2 -translate-x-1/2 w-full px-4 text-center text-stone-900 text-xs font-semibold italic font-['Roboto']">
                            *Tour dates are subject to the Student Calendar. Some days may not have tours due to student breaks or finals. Click <span class="underline">here</span> for details.
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Swiper -->
    <section>
        <swiper
      :slides-per-view="4"
      :slides-per-group="4"
      :space-between="30"
      :pagination="{ clickable: true }"
      :navigation="true"
      :grabCursor="true"
      :loop="true"
      :speed="800"
      :modules="modules"
      class="mySwiper"
      style="
        width: 100%;
        padding: 20px 40px;"
      :breakpoints="{
        320: { slidesPerView: 2, spaceBetween: 10 },
        640: { slidesPerView: 2, spaceBetween: 20 },
        1024: { slidesPerView: 3, spaceBetween: 25 },
        1280: { slidesPerView: 4, spaceBetween: 30 }
      }"
    >
      <!-- Card 1 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_Tours.jpg"
            alt="Columns at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Tours
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 2 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_YourVisit.jpg"
            alt="Panels of a Pavillion at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Your Visit
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 3 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_ForEducators.jpg"
            alt="Close up of bottom of the columns at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            For Educators (K-12+)
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 4 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_ContactUs.jpg"
            alt="Image of a tree and an arch made of brick"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Contact Us
          </p>
        </div>
      </swiper-slide>
      
      <!-- Card 5 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_Tours.jpg"
            alt="Columns at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            About Our Guides
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 6 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_YourVisit.jpg"
            alt="Panels of a Pavillion at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Feedback
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 7 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_ForEducators.jpg"
            alt="Close up of bottom of the columns at the Academical Village"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Become a Guide
          </p>
        </div>
      </swiper-slide>
  
      <!-- Card 8 -->
      <swiper-slide>
        <div class="relative w-full p-4 group">
          <NuxtImg
            src="/Carousel_ContactUs.jpg"
            alt="Image of a tree and an arch made of brick"
            class="w-full rounded-lg transition duration-250 group-hover:brightness-75"
          />
          <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
            Donate
          </p>
        </div>
      </swiper-slide>
    </swiper>
    </section>
  </template>
  
  <script>
  import { Swiper, SwiperSlide } from "swiper/vue";
  import "swiper/css";
  import "swiper/css/pagination";
  import "swiper/css/navigation";
  import { Pagination, Navigation } from "swiper/modules";
  
  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [Pagination, Navigation],
      };
    },
  };
  </script>
  
  <style>
    .swiper-pagination {
        position: absolute;
    }
    .swiper-pagination-bullet {
        height: 7px;
        width: 26px;
        border-radius: 25px;
        background: royalblue;
    }

    .swiper-button-next,
    .swiper-button-prev {
        color: royalblue;
    }
    /* History Carousel Styling and Functionality */
    .slider{
        width: 100%;
        height: var(--height);
        overflow: hidden;
        /* mask-image: linear-gradient(
            to right,
            transparent,
            #000 10% 90%,
            transparent
        ); */
    }
    .slider .list{
        display: flex;
        width: 100%;
        min-width: calc(var(--width) * var(--quantity));
        position: relative;
    }
    .slider .list .item{
        width: var(--width);
        height: var(--height);
        position: absolute;
        left: 100%;
        animation: autoRun 10s linear infinite;
        animation-delay: calc((10s / var(--quantity)) * (var(--position) - 1));
        transition: filter 0.5s;
    }
    .slider .list .item img{
        width: 100%;
        height: 225px;
    }
    .slider .list .item img:hover{
        width: 100%;
        height: 225px;
        transition: transform 0.5s ease, filter 0.5s ease;
    }
    @keyframes autoRun{
        from{
            left: 100%;
        }to{
            left: calc(var(--width) * -1);
        }
    }
    .slider:hover .item {
        animation-play-state: paused!important;
        /* filter: grayscale(1); */
    }
    .slider .item:hover {
        /* filter: grayscale(0);  */
        cursor: pointer;
    }
  </style>
  
