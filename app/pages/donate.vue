<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_Donate.jpeg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-8xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] text-center xl:text-right italic text-[clamp(2rem,9.5vw,5rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                VIRGINIA GUIDES
            </h1>
            <p class="font-Roboto text-center xl:text-right text-sm sm:text-lg md:text-md font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
        </div>
    </header> 

    <!-- Overlapping Section for Donatation Information-->
    <section class="relative z-20 -mt-20 px-4 mb-10">

        <div class="shadow-lg p-3 max-w-3xl mx-auto text-center bg-white border-4 border-royal-blue">

            <div class="flex flex-col justify-evenly items-center gap-4 bg-royal-blue px-10 py-12">
                <p class="text-white font-['Montserrat'] text-base sm:text-lg">
                    The Virginia Guides Service at UVA is an entirely student-run independent volunteer organization. All tours are given free of charge.
                </p>
                <p class="text-white font-['Montserrat'] text-base sm:text-lg pt-3 pb-5">
                    If you would like to provide additional support, please consider donating to our day-to-day operations. We appreciate your time and thank you for continuing to support our mission
                </p>
                <a href="https://www.givecampus.com/campaigns/21200/donations/new?designation=universityguides" class="px-10 py-2 border-1 border-white text-white text-lg rounded-full hover:bg-gray-200 hover:text-black hover:scale-105 transition-all duration-300 ease-in-out font-medium">
                    Donate
                </a>
            </div>
        </div>
    </section>
    
    <!-- Explore UVA History Section -->
    <ExploreUVAHistoryWhite />

    <!--Footer Section-->
    <Footer />

</template>

<script setup>
    import { onMounted } from "vue"
    import Footer from '~/components/Footer.vue'
    import ExploreUVAHistoryWhite from '~/components/ExploreUVAHistoryWhite.vue';

    onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show")
        } else {
            entry.target.classList.remove("show")
        }
        })
    })

    const scrollElements = document.querySelectorAll(".scrollElement")
    scrollElements.forEach((element) => observer.observe(element))
    })
</script>

<style>
    .scrollElement {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .scrollElement.show {
        opacity: 1;
        transform: translateY(0);
    }
    /* Carousel for Explore UVA History Section */
    .carousel-body {
        width: 100%;
        height: var(--height);
        display: grid;
        place-items: center;
    }
    .slider{
        height: 400px;
        margin: auto;
        position: relative;
        width: 100%;
        display: grid;
        place-items: center;
        overflow: hidden;
    }
    .slide-track{
        display: flex;
        width: calc(350px * 18);
        animation: scroll 15s linear infinite;
    }
    @keyframes scroll {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(calc(-350px * 5));
        }
    }
    .slide-track:hover{
        animation-play-state: paused;
    }
    .slide{
        height: 250px;
        width: 350px;
        display: flex;
        align-items: center;
        padding: 15px;
        perspective: 100px;
    }
    .carousel-img{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 1s;
    }
    .carousel-img:hover{
        transform: translateZ(12px);
        cursor: pointer;
    }
    .carousel-text {
        transition: opacity 0.3s ease;
    }
    .slide:hover .carousel-img + .carousel-text {
        opacity: 0;
        pointer-events: none;
    }
</style>