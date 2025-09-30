<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_ForEducators.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-8xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-right whitespace-nowrap text-[clamp(1rem,7vw,3rem)] lg:text-[clamp(1rem,8vw,4rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                BEYOND THE CLASSROOM
            </h1>
            <p class="font-['Roboto'] text-base sm:text-md md:text-lg font-semibold leading-snug text-center xl:text-right uppercase [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                History Tours of the University of Virginia
            </p>
            <p class="font-['Roboto'] text-base sm:text-md md:text-lg font-semibold leading-snug text-center xl:text-right uppercase [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                For K-12 & College Groups
            </p>
        </div>
    </header> 

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative z-20 -mt-10 px-4 mb-10">
        <!-- Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-royal-blue -z-10 hidden sm:block"></div>

        <div class="shadow-lg p-6 max-w-2xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4 text-white">
                <a href="/join-guides" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    About Us
                </a>
                <a href="/request-specialty-tours" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Specialty Tour Request Form
                </a>
                <a href="/about-tours#specialty-tours" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Other Tours
                </a>
            </div>
        </div>
    </section>

    <!-- Info Section for different age groups -->
    <section class="p-5 sm:p-8 md:p-6 mb-5">
        <!--Section Header-->
        <div class="flex flex-col justify-center text-center lg:text-left max-w-7xl mx-auto gap-3 mb-5 lg:mb-10">
            <h1 class="uppercase font-['Playfair_Display'] italic font-medium text-dark-green text-4xl sm:text-5xl">
                History for all ages
            </h1>
            <p class="font-['Montserrat'] text-dark-green text-lg sm:text-xl">
                Whether you're visiting with young learners, future students, or fellow scholars, we offer tours tailored to every stage of the educational journey.
            </p>
        </div>

        <!--Info Section For Different Age Groups-->
        <div class="flex flex-col lg:flex-row justify-center items-stretch max-w-7xl mx-auto gap-10">
            <!--Image-->
            <div class="w-full lg:w-[40%] flex"> 
                <img 
                    src="/for-educators-page/ChildrensTour.jpg" 
                    alt="Childrens Tour at the Amphiteather steps" 
                    class="w-full object-cover rounded-md shadow-md"
                />
            </div>
            <!--Text Info-->
            <div class="w-full lg:w-[60%] flex flex-col gap-5"> 
                <!--Kids-->
                <div class="flex flex-col">
                    <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                        Kids (K-5) 
                    </h1>
                    <p class="font-['Montserrat'] text-base sm:text-lg font-light">
                        A one-hour introduction to UVA that blends key moments in history with what college life is like today. Kids will hear about the University's founding vision, 
                        explore the Academical Village's architecture, learn about the 1895 burning of the Rotunda, and see how the University and its community 
                        have changed over time through resilience and creativity.
                    </p>
                </div>
                <!--Middle and High School-->
                <div class="flex flex-col">
                    <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                        Middle and High School Groups
                    </h1>
                    <p class="font-['Montserrat']  text-base sm:text-lg font-light">
                        Explore UVA's traditions, architecture, and the history of student activism and community leadership, including the legacies of slavery, the Civil War, 
                        and Civil Rights movement after, alongside at the opportunities, culture, and student life that has developed on Grounds today.
                    </p>
                </div>
                <!--College Students-->
                <div class="flex flex-col">
                    <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                        College Students 
                    </h1>
                    <p class="font-['Montserrat']  text-base sm:text-lg font-light">
                        A deeper, more detailed examination of UVA's past and present, tracing its founding ideals through periods marked by slavery, the Civil War, 
                        the 20th century eugenics movement, and progress in Civil Rights. From the 1800s to the present day, this tour reflects on how the University 
                        has acknowledged and responded to these histories through community resistance and efforts to address complex social, political, and cultural challenges still shaping the world today.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!--Banner-->
    <section>
        <div class="flex flex-col lg:flex-row w-full gap-y-3 gap-x-3 bg-gray-300 text-center py-6 px-10 lg:px-20 justify-center items-center">
            <p class="w-full lg:w-3/4 font-Roboto text-royal-blue italic text-center text-base sm:text-lg md:text-md">
                <span class="font-bold">
                    Because Virginia Guides is student-run, we do not provide tours during exam periods, reading days, or student breaks, which are specified 
                    <a href="https://registrar.virginia.edu/calendar/academic" class="underline">
                        here
                    </a>
                </span>. 
                If interested in a student tour group, 
                <span class="font-bold">
                    please complete the
                    <a href="/request-specialty-tours" class="underline">
                        specialty tour form 
                    </a> at least 3 weeks in advance,
                </span> to better plan with you for your tour group size, 
                interests, and needs.
            </p>
            <!--Request Tour Button-->
            <div class="w-full lg:w-1/4 flex justify-center items-center">
                <a href="/request-specialty-tours">
                    <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                        <p class="font-['Roboto'] text-gray-800 font-semibold text-base md:text-lg">
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
    </section>

    <!-- Last Info Section -->
    <section class="p-5 sm:p-8 md:p-6 m-2 lg:m-8">
        <div class="flex flex-col justify-center text-left max-w-6xl mx-auto gap-3">
            <ul class="list-disc font-['Montserrat'] text-base sm:text-lg space-y-2">
                <li>
                    <span class="font-bold">
                        Tours typically last between 1-1.5 hours
                    </span>
                     limited to the areas in and surrounding the Academical Village, the heart of the UNESCO World Heritage Site designation at the University of Virginia.
                </li>
                <li>
                    <span class="font-bold">
                        All tours are free of charge,
                    </span> regardless of group size. Donations to support work are welcome.
                </li>
                <li>
                    Please include any unique interests or needs for your tour group in your tour-request email, we will be in contact shortly to schedule guides and information.
                </li>
            </ul>
        </div>
    </section>

    <!-- Explore UVA History Section -->
    <section class="bg-royal-blue py-16 sm:py-20 md:py-24">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">

            <!-- Header -->
            <h1 class="font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                Explore UVA History
            </h1>

            <!-- Description -->
            <p class="font-['Montserrat'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                which focus on a specific aspect of UVA's extensive 200 year history.
            </p>

            <!-- Button -->
            <a href="/about-tours">
                <button class="inline-flex items-center space-x-3 rounded-full border text-white font-['Montserrat'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-royal-blue hover:bg-neutral-300 transition-all duration-300 ease-in-out hover:cursor-pointer">
                    <span>HISTORY TOURS</span>
                    <svg class="flex-shrink-0" height="25px" width="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 12H18M18 12L13 7M18 12L13 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </a>
        </div>

        <!-- Carousel: Our Tours-->
        <div class="carousel-body">
            <div class="slider">
                <div class="slide-track">
                    <a href="/about-tours/#history-of-women-at-uva">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                    <!--Same 5 slides (doubled)-->
                    <a href="/about-tours/#history-of-women-at-uva">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" alt="">
                            <p class="carousel-text self-start text-white font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!--Footer Section-->
    <section>
        <div class="relative overflow-hidden">

            <!-- Background Image -->
            <NuxtImg 
            src="/Header_PageFooters.jpg"
            alt="My image file description"
            class="w-full min-h-screen sm:h-[120vh] object-cover"
            />

            <!-- Overlay Content -->
            <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-center z-10">

            <!-- Header -->
            <div class="mt-[-6rem] sm:mt-[-8rem] md:mt-[-10rem]">
                <h1 class="font-['Playfair_Display'] text-white italic text-[clamp(2.5rem,9vw,5rem)] leading-tight">
                    SHED LIGHT
                </h1>
                <p class="font-['Roboto'] text-white text-base sm:text-lg md:text-xl font-semibold leading-snug">
                    ON HISTORY
                </p>
            </div>

            <!-- Buttons -->
            <div class="mt-40 flex flex-col sm:flex-row justify-center items-center gap-x-10 gap-y-4 pointer-events-auto">
                <a href="/your-visit">
                    <button class="font-['Roboto'] border border-white text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 hover:border-transparent rounded-full py-3 px-10 cursor-pointer transition-all duration-300 ease-in-out">
                        PLAN YOUR VISIT
                    </button>
                </a>
                <a href="/donate">
                    <button class="font-['Roboto'] border border-white text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 hover:border-transparent rounded-full py-3 px-18 cursor-pointer transition-all duration-300 ease-in-out">
                        DONATE
                    </button>
                </a>
            </div>

            <!-- Description -->
            <p class="mt-20 font-['Roboto'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                The Virginia Guides Service at UVA is an entirely student-run independent volunteer organization. 
                If you would like to provide additional support, please consider donating to our day-to-day operations 
                <a href="/donate" class="underline">here</a>. We appreciate your time and thank you for continuing to support our mission.
            </p>

            </div>
        </div>
    </section>

    <!--Footer Link Section-->
    <section>
        <div class="relative w-full bg-black py-10 px-6">
            <div class="max-w-screen-xl mx-auto flex flex-col md:flex-row gap-10">

                <!-- Left Side Footer -->
                <div class="basis-1/2 flex flex-wrap justify-between gap-6 text-sm text-zinc-400 font-['Roboto']">
                    <!-- Column 1 -->
                    <ul class="flex flex-col gap-2 min-w-[100x]">
                        <li class="font-['Playfair_Display'] italic underline text-white text-lg">Visit</li>
                        <a href="your-visit">
                            <li class="cursor-pointer">Directions + FAQ</li>
                        </a>
                        <a href="about-tours#about-tours">
                            <li class="cursor-pointer">History Tours</li>
                        </a>
                        <a href="/about-tours#specialty-tours">
                            <li class="cursor-pointer">Specialty Tours</li>
                        </a>
                        <a href="/request-specialty-tours">
                            <li class="cursor-pointer">Specialty Tours Request</li>
                        </a>
                    </ul>

                    <!-- Column 2 -->
                    <ul class="flex flex-col gap-2 min-w-[100px]">
                        <li class="font-['Playfair_Display'] italic underline text-white text-lg">About Us</li>
                        <a href="/about-tours#about-tours">
                            <li class="cursor-pointer">Our Mission</li>
                        </a>
                        <a href="/join-guides#join-guides">
                            <li class="cursor-pointer">Become a Guide</li>
                        </a>
                        <a href="/feedback">
                            <li class="cursor-pointer">Feedback</li>
                        </a>
                        <a href="https://www.instagram.com/virginiaguides/">
                            <li class="cursor-pointer">Instagram</li>
                        </a>
                    </ul>

                    <!-- Column 3 -->
                    <ul class="flex flex-col gap-2 min-w-[100px]">
                        <li class="font-['Playfair_Display'] italic underline text-white text-lg">More</li>
                        <a href="/for-educators">
                            <li class="cursor-pointer">For Educators</li>
                        </a>
                        <a href="/donate">
                            <li class="cursor-pointer">Donate</li>
                        </a>
                    </ul>
                </div>

                <!-- Right Side Footer -->
                <div class="basis-1/2 flex flex-col gap-3 text-zinc-400 text-sm md:text-base font-light">
                    <div class="flex items-start gap-4 font-['Roboto']">
                        <img class="h-12 w-12 obSject-contain" src="/guides-logo.png" alt="Virginia Guides Logo" />
                        <p>
                            The Virginia Guides continues 75 years of guiding visitors through UVA in Charlottesville VA. The Guides Service is a 
                            student-run organization independent of the University of Virginia, carrying forward tradition while bringing a more complete light to the past.
                        </p>
                    </div>

                    <div class="flex justify-center md:justify-end">
                        <a href="/contact-us">
                            <button class="border border-white text-white rounded-full px-6 py-2 font-['Montserrat'] hover:bg-zinc-500 hover:border-zinc-500 hover:text-black transition-all duration-300 ease-in-out cursor-pointer">
                                CONTACT US
                            </button>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

</template>

<style>
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