<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_Tours.jpg')] w-full bg-cover bg-right bg-no-repeat h-[60vh] sm:h-[75vh]">
        <!-- Centered Text -->
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
    <section class="relative z-20 -mt-12 px-4 mb-5">
        <!-- Blue Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-royal-blue -z-10 hidden sm:block"></div>

        <div class="shadow-lg p-6 max-w-2xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4 text-white">
                <a href="#specialty-tours" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Specialty Tours
                </a>
                <a href="/your-visit" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Plan Your Visit
                </a>
                <a href="/for-educators" class="text-lg hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    For Educators
                </a>
            </div>
        </div>
    </section>

    <!-- Historical Tour Info Section -->
    <section id="about-tours" class="p-4 sm:p-8 md:p-6">
        <div class="flex flex-col lg:flex-row justify-center items-center max-w-7xl mx-auto gap-10">

            <!-- Right: Image -->
            <div class="w-full lg:w-1/2 flex justify-center items-center">
                <img src="/about-tours-page/Tourpage_LawnRooms.jpg" alt="Historical Tour Image" class="w-full max-w-xl h-auto rounded-md shadow-md">
            </div>

            <!-- Left: Text -->
            <div class="w-full lg:w-1/2 px-5 lg:px-0">
                <p class="font-['Playfair_Display'] italic text-center font-medium text-dark-green text-4xl sm:text-5xl leading-tight mb-6">
                HISTORICAL TOURS
                </p>
                <p class="font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                    Founded in 1819 by Thomas Jefferson to promote education as a defense against tyranny, 
                    UVA's history is more than its founding ideals. It is also shaped by the labor, activism, 
                    and voices of those once excluded. Built and maintained by an estimated 4,000 enslaved 
                    laborers between 1817 and 1865, the University's grounds hold stories long overlooked.
                </p>
                <p class="font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 pt-2">
                    From its founding to construction, from the Civil War to Civil Rights, our student-led tours 
                    explore 200+ years of change, resistance, and community that shape the present. Tours navigate 
                    the outdoor grounds of the UNESCO World Heritage Site and are written by students after a 
                    semester of intensive training, research, and critical reflection.
                </p>
                <div class="flex flex-col justify-center items-center pt-5">
                    <div class="flex flex-col justify-center items-center border-4 border-double border-dark-green rounded-md p-3">
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
                        <NuxtLink to="/your-visit#times-and-registration" class="justify-center items-center mt-2">
                            <button class="rounded-full bg-dark-green px-6 py-3 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-md hover:shadow-lg hover:bg-green-700 hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                                <p class="font-['Roboto'] text-white text-sm sm:text-base md:text-lg">
                                    Register Here
                                </p>
                            </button>
                        </NuxtLink>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Carousel of pictures-->
    <section>
        <div class="about-carousel-body">
            <div class="about-slider">
                <div class="about-slide-track">
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_womenatuva.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="/about-tours-page/carousel-history/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_GardenTours.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_MEL.jpeg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_childrenstour.jpg" alt="">
                    </div>
                    <!--Same 5 slides (doubled)-->
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_womenatuva.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="/about-tours-page/carousel-history/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_GardenTours.jpg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_MEL.jpeg" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="/about-tours-page/carousel-history/UVAhistoryCarousel_childrenstour.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--Specialty Tours Section-->
    <section id="specialty-tours" class="py-4 sm:py-8 md:py-6">
        <div class="flex flex-col justify-center items-center">

            <!--Heading-->
            <div class="flex flex-col justify-center items-center mb-5">
                <h1 class="font-['Playfair_Display'] italic text-center font-medium text-dark-green text-5xl sm:text-6xl leading-tight mb-2">
                    SPECIALTY TOURS
                </h1>
                <p class="font-['Playfair_Display'] w-full sm:w-[70%] text-center font-light text-black text-base sm:text-xl px-10">
                    In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                    which focus on a specific aspect of UVA's extensive 200 year history.
                </p>
            </div>

            <!--Banner-->
            <div class="bg-dark-green py-6 px-10">
                <div class="flex flex-col md:flex-row w-full items-center justify-between gap-8">

                    <!-- Description -->
                    <div class="font-Montserrat text-white text-left text-base lg:text-lg">
                        <p class="italic">
                            To ensure guide availability for special topic or large tour groups, all tour requests should be submitted at least 
                            <span class="underline font-semibold">two to three weeks in advance</span>.
                        </p>
                        <p class="pt-2">
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
                <div id="history-of-african-americans-tour" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/HistoryofAfricanAmericansatUVA.jpg" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
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
                <div id="MEL-tour" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/MemorialtoEnslavedLaborers.jpg" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
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
                <div id="history-of-women-at-uva-tour" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/HistoryofWomen.jpg" class="w-full h-full object-cover object-top" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
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
                <div id="childrens-tours" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/ChildrensTour.jpg" class="w-full h-full object-cover object-bottom" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out hover:cursor-pointer">
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
                <div id="private-admissions-tour" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/PrivateTour.jpg" class="w-full h-full object-cover object-bottom" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
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
                <div id="garden-tours" class="flex flex-col md:flex-row lg:h-[50vh] justify-center gap-1 sm:gap-3 md:gap-2 items-stretch">
                    <!--Picture-->
                    <div class="w-full md:w-1/2 px-2 sm:px-6 md:px-0">
                        <img src="/about-tours-page/specialty-tours/GardenTour.jpg" class="w-full h-full object-cover object-center" alt="History of African Americans at UVA">
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
                                <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
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
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 8rem;
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