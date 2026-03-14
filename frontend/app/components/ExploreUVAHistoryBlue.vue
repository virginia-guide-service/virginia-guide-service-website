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
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of Women at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of African-Americans at UVA</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>

<style>
/* === Explore UVA History Carousel === */
.carousel-body {
    width: 100%;
    height: var(--height);
    display: grid;
    place-items: center;
}
.slider {
    height: 400px;
    margin: auto;
    position: relative;
    width: 100%;
    display: grid;
    place-items: center;
    overflow: hidden;
}
/* Track that continuously scrolls */
.slide-track {
    display: flex;
    /* 10 slides × 350px */
    width: calc(350px * 10);
    animation: scroll 15s linear infinite;
    will-change: transform;
}
/* Left-to-right scrolling animation */
@keyframes scroll {
    0%   { transform: translateX(0); }
    100% { transform: translateX(calc(-350px * 5)); }
}
/* Pause scrolling on hover */
.slide-track:hover {
    animation-play-state: paused;
}
/* Individual slide */
.slide {
    height: 250px;
    width: 350px;
    display: flex;
    align-items: center;
    padding: 15px;
    perspective: 100px;
}
/* Carousel image styling */
.carousel-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 1s;
}
/* Slight pop-out effect on hover */
.carousel-img:hover {
    transform: translateZ(12px);
    cursor: pointer;
}
/* Text overlay */
.carousel-text {
    transition: opacity 0.3s ease;
}
/* Hide text when image is hovered */
.slide:hover .carousel-img + .carousel-text {
    opacity: 0;
    pointer-events: none;
}
 
/* === Responsive overrides === */
 
/* Tablet (640px – 1023px) */
@media (max-width: 1023px) {
    .slide {
        width: 280px;
        height: 220px;
        padding: 12px;
    }
    .slide-track {
        width: calc(280px * 10);
    }
    @keyframes scroll {
        0%   { transform: translateX(0); }
        100% { transform: translateX(calc(-280px * 5)); }
    }
}
 
/* Mobile (< 640px) */
@media (max-width: 639px) {
    .slider {
        height: 260px;
    }
    .slide {
        width: 200px;
        height: 180px;
        padding: 8px;
    }
    .slide-track {
        width: calc(200px * 10);
    }
    @keyframes scroll {
        0%   { transform: translateX(0); }
        100% { transform: translateX(calc(-200px * 5)); }
    }
    .carousel-text {
        font-size: 0.75rem;
    }
}
</style>
