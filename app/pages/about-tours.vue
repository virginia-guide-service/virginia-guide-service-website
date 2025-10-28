<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_Tours.jpg')] w-full bg-cover bg-right bg-no-repeat h-[60vh] sm:h-[75vh]">
        <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-left whitespace-nowrap text-[clamp(3rem,9.5vw,5.5rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                SHED LIGHT
            </h1>
            <p class="font-Roboto text-center xl:max-w-lg xl:text-right text-xl sm:text-2xl md:text-3xl font-extralight leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                ON HISTORY
            </p>
        </div>
    </header>

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative z-20 -mt-10 px-4 mb-5">
        <!-- Blue Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-royal-blue -z-10 hidden sm:block"></div>

        <div class="shadow-lg p-6 max-w-2xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4 text-white">
                <a href="#specialty-tours" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Specialty Tours
                </a>
                <a href="/your-visit" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Take a Tour
                </a>
                <a href="/for-educators" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    For Educators
                </a>
            </div>
        </div>
    </section>

    <!-- Historical Tour Info Section -->
    <section id="about-tours">
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="flex flex-col lg:flex-row justify-center items-center gap-10">
                <!-- Right: Image -->
                <div class="scrollElement w-full lg:w-1/2 flex justify-center items-center">
                    <img src="/about-tours-page/TourTaking1.jpg" alt="Historical Tour Image" loading="lazy" class="w-full max-w-lg h-auto rounded-md shadow-md">
                </div>

                <!-- Left: Text -->
                <div class="w-full lg:w-1/2 px-5 lg:px-0 justify-between items-center">
                    <p class="scrollElement font-['Playfair_Display'] italic text-center font-medium text-dark-green text-4xl sm:text-5xl leading-tight mb-6">
                        HISTORICAL TOURS
                    </p>
                    <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                        Founded in 1819 by Thomas Jefferson to promote education as a defense against tyranny, 
                        UVA's history is more than its founding ideals. It is also shaped by the labor, activism, 
                        and voices of those once excluded. Built and maintained by an estimated 4,000 enslaved 
                        laborers between 1817 and 1865, the University's grounds hold stories long overlooked.
                    </p>
                    <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 pt-2">
                        From its founding to construction, from the Civil War to Civil Rights, our student-led tours 
                        explore 200+ years of change, resistance, and community that shape the present. Tours navigate 
                        the outdoor grounds of the UNESCO World Heritage Site and are written by students after a 
                        semester of intensive training, research, and critical reflection.
                    </p>
                    <div class="scrollElement flex flex-col justify-center items-center pt-5">
                        <div class="flex flex-col justify-center items-center border-3 border-dark-green p-4">
                            <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-xl px-4">
                                <li>
                                Standard History Tours last around <span class="font-bold">1 hour</span>.
                                </li>
                                <li>
                                All tours are <span class="font-bold">free of charge</span>, regardless of group size.
                                </li>
                                <li>
                                Donations to support work are welcome at this link
                                <a href="https://www.givecampus.com/campaigns/21200/donations/new?designation=universityguides">
                                    <span class="underline cursor-pointer">here</span>.
                                </a>
                                </li>
                            </ul>
                            <!--Button-->
                            <NuxtLink to="/your-visit#times-and-registration" class="justify-center items-center pt-3">
                                <button class="rounded-full bg-dark-green px-6 py-2 shadow-md hover:shadow-lg hover:bg-green-700 hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-white text-base font-medium">
                                        Register Here
                                    </p>
                                </button>
                            </NuxtLink>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Carousel of pictures-->
    <section>
        <div class="scrollElement about-carousel-body">
            <div class="about-slider">
                <div class="about-slide-track">
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="/about-tours-page/carousel-history/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                    </div>
                    <!--Same 5 slides (doubled)-->
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="/about-tours-page/carousel-history/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--Specialty Tours Section-->
    <section id="specialty-tours" class="pt-6 pb-12">
        <div class="flex flex-col justify-center items-center">
            <!--Heading-->
            <div class="flex flex-col justify-center items-center pb-10">
                <h1 class="scrollElement font-['Playfair_Display'] italic text-center font-medium text-dark-green text-5xl sm:text-6xl leading-tight mb-2">
                    SPECIALTY TOURS
                </h1>
                <p class="scrollElement font-['Montserrat'] w-full sm:w-[70%] text-center font-light text-black text-base sm:text-xl px-10">
                    In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                    which focus on a specific aspect of UVA's extensive 200 year history.
                </p>
            </div>

            <!--Banner-->
            <div class="scrollElement bg-dark-green py-6 px-10">
                <div class="flex flex-col md:flex-row w-full items-center justify-between gap-8">

                    <!-- Description -->
                    <div class="font-Montserrat text-white text-left text-base lg:text-lg">
                        <p class="italic">
                            To ensure guide availability for special topic or large tour groups, all tour requests should be submitted at least 
                            <span class="underline font-semibold">two to three weeks in advance</span>.
                            Standard Historical Tours occur regularly throughout the school year and 
                            <span class="underline font-semibold">do not</span> require a special request.
                        </p>
                    </div>

                    <!-- Button -->
                    <div class="text-center text-nowrap">
                        <a href="/request-specialty-tours"
                        class="inline-block font-['Montserrat'] bg-white text-dark-green font-semibold rounded-full 
                                px-6 py-2 text-sm 
                                sm:px-8 sm:py-3 sm:text-base 
                                md:px-10 md:py-4 md:text-lg 
                                shadow-md hover:shadow-lg hover:scale-105 transition-all duration-300 ease-in-out">
                        Specialty Tour Request Form
                        </a>
                    </div>

                </div>
            </div>

            <!--Specialty Tours List-->
            <div class="flex flex-col justify-center items-center gap-10 md:gap-5 py-6 m-5 lg:m-10">
                <!--History of African-Americans at UVA-->
                <div id="history-of-african-americans-tour" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/HAA.jpg" loading="lazy" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-2 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            History of African-Americans at UVA
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            History of African-American tours run approximately an hour and grapple with our University's complicated racial legacies of slavery and discrimination. 
                            Topics covered will include slavery, integration, and even a discussion of the modern racial climate at UVA.
                        </p>
                        <!--Request Tour Button-->
                        <div class="w-full flex justify-start">
                            <a href="/request-specialty-tours">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                        Request Tour
                                    </p>
                                    <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                        <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>
                </div>

                <!--Memorial to Enslaved Laborers-->
                <div id="MEL-tour" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/MEL.jpeg" loading="lazy" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-3 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            Memorial to Enslaved Laborers
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            MEL tours discuss the history of enslaved laborers' resistance and resilience at the University 
                            and the advocacy by community members and students to fully acknowledge and memorialize their labor. 
                            MEL tours were designed by the Descendants of Enslaved Communities (DEC-UVA).
                        </p>
                        <!--Request Tour Button-->
                        <div class="w-full flex justify-start">
                            <a href="/request-specialty-tours">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                        Request Tour
                                    </p>
                                    <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                        <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>
                </div>

                <!--History of Women at UVA-->
                <div id="history-of-women-at-uva-tour" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/HistoryofWomen.jpg" loading="lazy" class="w-full h-full object-cover object-top" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-3 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            History of Women at UVA
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            History of Women tours run approximately an hour and focus on the process of gradual integration of women at the University of Virginia. 
                            Tourists learn about the lives of the first women on Grounds in the 1820s and the gradual acceptance of women into the student community.
                        </p>
                        <!--Request Tour Button-->
                        <div class="w-full flex justify-start">
                            <a href="/request-specialty-tours">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                        Request Tour
                                    </p>
                                    <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                        <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>
                </div>

                <!--Children's Tours-->
                <div id="childrens-tours" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/ChildrensTour.jpg" loading="lazy" class="w-full h-full object-cover object-bottom" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-3 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            Children's Tours
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            Children's tours run approximately an hour and introduce various exciting stories about the University. 
                            Children will learn about the founder of the University, Thomas Jefferson, early life at the University, 
                            and the burning of the Rotunda in 1895. The content of these tours is geared toward young children from Pre-K to Fifth grade.
                        </p>
                        <!--Button-->
                        <div class="w-full flex justify-start">
                            <a href="/for-educators">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out hover:cursor-pointer">
                                <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                    For Educators
                                </p>
                                <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                                </button>
                            </a>
                        </div>
                    </div>
                </div>

                <!--Private Admissions Tours-->
                <div id="private-admissions-tour" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/PrivateTour.jpg" loading="lazy" class="w-full h-full object-cover object-bottom" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-3 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            Private Admissions Tours
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            Admissions tours are 75-90 minutes long and centered around the student experience at UVA. 
                            None of our Guides have an identical script. While all tours cover a shared basic information, 
                            our goal is to present the University with candor, personal experienceand enthusiasm. 
                            The tour covers a brief history of the University, as well as academics, extracurricular activities, 
                            athletics, dining, traditions, and much more.                      </p>
                        <!--Request Tour Button-->
                        <div class="w-full flex justify-start">
                            <a href="/request-specialty-tours">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                        Request Tour
                                    </p>
                                    <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                        <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>

                </div>

                <!--Garden Tours-->
                <div id="garden-tours" class="scrollElement flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/GardenTour.jpg" loading="lazy" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
                    </div>
                    <!--Text-->
                    <div class="md:w-1/2 flex flex-col justify-start space-y-3 md:space-y-6 px-2 sm:px-6 md:px-4">
                        <h1 class="font-['Montserrat'] text-left font-medium text-black text-2xl sm:text-3xl mt-2">
                            Garden Tours
                        </h1>
                        <p class="font-['Roboto'] text-left font-light text-black text-md sm:text-lg">
                            Garden Tours run approximately forty-five minutes and give tourists an inside look into the Pavilion gardens at the University. 
                            The tours explore the role of the gardens during the early University and their transformation to the modern day spaces students enjoy today.
                        </p>
                        <!--Request Tour Button-->
                        <div class="w-full flex justify-start">
                            <a href="/request-specialty-tours">
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                                    <p class="font-['Roboto'] text-gray-800 font-semibold text-sm sm:text-base md:text-lg">
                                        Request Tour
                                    </p>
                                    <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                        <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>

    <Footer />

</template>

<script setup>
    import { onMounted } from "vue"
    import Footer from '~/components/Footer.vue'

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
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 8rem;
    }
    .scrollElement {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .scrollElement.show {
        opacity: 1;
        transform: translateY(0);
    }
    .about-carousel-body {
        width: 100%;
        height: var(--height);
        display: grid;
        place-items: center;
    }
    .about-slider{
        height: 300px;
        margin: auto;
        position: relative;
        width: 100%;
        display: grid;
        place-items: center;
        overflow: hidden;
    }
    .about-slide-track{
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
    .about-slide{
        height: 250px;
        width: 350px;
        display: flex;
        align-items: center;
        padding: 5px;
    }
    .about-carousel-img{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
</style>