<template>
    <!-- Explore UVA History Section -->
    <section class="bg-royal-blue py-16 sm:py-20 md:py-24">
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">

            <!-- Header -->
            <h1 class="scrollElement font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                Explore UVA History
            </h1>

            <!-- Description -->
            <p class="scrollElement font-['Montserrat'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                which focus on a specific aspect of UVA's extensive 200 year history.
            </p>

            <!-- Button -->
            <a href="/about-tours" class="scrollElement">
                <button class="inline-flex items-center space-x-3 rounded-full border-1 border-gray-300 text-white font-['Montserrat'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-royal-blue hover:bg-gray-100 hover:scale-105 transition-all duration-300 ease-in-out hover:cursor-pointer">
                    <p>HISTORY TOURS</p>
                    <svg class="flex-shrink-0" height="25px" width="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 12H18M18 12L13 7M18 12L13 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </a>
        </div>

        <!-- Carousel: Our Tours-->
        <div class="scrollElement carousel-body">
            <div class="slider">
                <div class="slide-track">
                    <a href="/about-tours/#history-of-women-at-uva-tour">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of Women at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white  font-['Roboto']">History of African-Americans at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white  font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                    <!--Same 5 slides (doubled)-->
                    <a href="/about-tours/#history-of-women-at-uva-tour">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of Women at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of African-Americans at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>