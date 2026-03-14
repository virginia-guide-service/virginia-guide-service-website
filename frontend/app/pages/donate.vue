<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_Donate.jpeg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
    </header> 

    <!-- Overlapping Section for Donatation Information-->
    <section class="relative z-20 -mt-50 px-4 mb-10">

        <div class="shadow-lg p-3 max-w-3xl mx-auto text-center bg-white border-4 border-royal-blue">

            <div class="flex flex-col justify-evenly items-center gap-4 bg-royal-blue px-10 py-12">
                <p class="text-white font-['Montserrat'] text-base sm:text-lg">
                    The Virginia Guide Service at UVA is an entirely student-run independent volunteer organization. All tours are given free of charge.
                </p>
                <p class="text-white font-['Montserrat'] text-base sm:text-lg pt-3 pb-5">
                    If you would like to provide additional support, please consider donating to our day-to-day operations. We appreciate your time and thank you for continuing to support our mission.
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

    useHead({
        title: 'Donate | Virginia Guides Service',
        link: [
            { rel: 'preload', as: 'image', href: 'https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_Donate.jpeg', fetchpriority: 'high' }
        ]
    })

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
</style>
