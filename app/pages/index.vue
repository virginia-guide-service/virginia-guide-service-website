<template>
    <!--Header Section-->
    <header class="relative overflow-visible h-[115vh] w-full bg-[url('/Header_FrontPageNew.jpg')] bg-cover bg-center" aria-label="Virginia Guides Hero Section">
        <div class="absolute top-[52%] left-[50%] lg:left-[48%] w-full max-w-7xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
            <h1 class="font-['Playfair_Display'] text-center xl:text-right italic text-[clamp(2.5rem,9.5vw,6rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                <span class="text-[clamp(3.5rem,10.5vw,7rem)]">V</span>IRGINIA 
                <span class="text-[clamp(3.5rem,10.5vw,7rem)]">G</span>UIDES
            </h1>
            <p class="font-Roboto text-center xl:text-right text-sm sm:text-lg md:text-md font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
            <div class="text-center xl:text-right xl:pr-25">
                <a href="/your-visit">
                    <button class="font-Roboto font-medium mt-10 px-10 py-2 text-lg md:px-15 md:py-3 md:text-2xl text-white hover:text-royal-blue bg-[rgba(0,0,0,0.45)] hover:bg-gray-100 border hover:border-gray-100 rounded-full cursor-pointer hover:scale-105 transition-all duration-300 ease-in-out"
                    aria-label="Explore Virginia Guides">
                        Take a Tour
                    </button>   
                </a>
            </div>
        </div>
        <div class="absolute flex flex-col items-center top-[83%] lg:pt-8 md:top-5/6 left-1/2 w-full max-w-4xl px-4 -translate-x-1/2 text-white text-center">
            <p class="font-['Montserrat'] italic text-base sm:text-lg md:text-xl font-light leading-snug">
                The Virginia Guides Service continues 75 years of students guiding visitors through UVA,
                carrying forward tradition while bringing new light to the past.
            </p>
            <!-- <svg class="pt-3 w-12 h-12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M12 17L12 7M12 17L8 13M12 17L16 13M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#ffffff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg> -->
        </div>
    </header>

    <!-- More Tour Info Section -->
    <section class="bg-white">
        <div class="mx-auto px-4 sm:px-6 lg:px-8 pt-12">
            <div class="flex flex-col lg:flex-row items-center gap-10 max-w-7xl mx-auto">
            
                <!-- Left: Text -->
                <div class="w-full lg:w-3/5">
                    <p class="scrollElement font-['Playfair_Display'] italic font-bold text-dark-green text-4xl sm:text-5xl leading-tight pb-6">
                        Where The Past Stands<br />
                        And More Is Told.
                    </p>
                    <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                        The American promise rests on the idea that all are created equal, and every story has a place in that legacy. 
                        Many who have shaped this University have long gone unrecognized. As we learn more, 
                        <a class="font-['Montserrat'] text-dark-green italic font-semibold">our tours evolve — not to change the past, but to share more of it.</a>
                        <br /><br />
                        Jefferson's Academical Village is more than its founding. From the history of enslavement to 
                        liberation, desegregation to coeducation, it shapes and reflects the American story, recognized by UNESCO for this role, 
                        and is made richer as we share more.
                        <br /><br />
                        <a class="font-['Montserrat'] font-semibold italic">With this mission, </a>
                        <a class="font-['Montserrat'] italic font-semibold underline text-dark-green">all tours are offered free of charge.</a>
                    </p>
                </div>

                <!-- Right: Image with Text Overlay + footer notice-->
                <div class="scrollElement w-full lg:w-2/5 flex flex-col">
                    <!-- Image with Text Overlay -->
                    <div class="relative flex justify-center lg:justify-end">
                        <div class="relative w-full max-w-sm sm:max-w-md h-[573px] overflow-hidden rounded-[35px] shadow-lg">

                            <!-- Background Image -->
                            <img
                                src="/index-page/TourTaking1_Blurry.jpg"
                                alt="Tour illustration"
                                class="absolute inset-0 w-full h-full object-cover rounded-[35px]"
                                loading="lazy"
                            />

                            <!-- Overlay: Tour Times with Clock Icon + Subtitle -->
                            <div class="absolute top-[116px] left-6 text-left flex items-start gap-2 w-auto sm:w-72 md:w-80 lg:w-auto">
                                <!-- Clock Icon -->
                                <svg viewBox="0 0 24 24" fill="none" class="w-7 h-7 mt-1 shrink-0" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 7V12L14.5 13.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" 
                                        stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>

                                <!-- Text Block -->
                                <div class="flex flex-col">
                                    <p class="text-stone-800 text-2xl font-bold font-['Montserrat']">TOUR TIMES*</p>
                                    <p class="text-stone-700 text-sm font-medium font-['Montserrat']">
                                        All tours leave from the front Rotunda steps
                                    </p>
                                </div>
                            </div>

                            <!-- Overlay: Days and Times -->
                            <div class="absolute top-[179px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">FRIDAY</p>
                                <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <div class="absolute top-[234px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SATURDAY</p>
                                <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <div class="absolute top-[289px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SUNDAY</p>
                                <p class="text-stone-700 text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <!--Button-->
                            <div class="absolute left-1/2 bottom-20 -translate-x-1/2">
                                <a href="/your-visit#times-and-registration">
                                    <button class="font-['Montserrat'] text-lg font-semibold px-6 py-2 rounded-[20px] text-white hover:text-white bg-dark-orange hover:bg-orange-800 hover:scale-105 cursor-pointer transition-all duration-300 ease-in-out"
                                        aria-label="Explore Virginia Guides">
                                        TAKE A TOUR
                                    </button>
                                </a>
                            </div>

                        </div>
                    </div>
                    <!-- Footer Notice -->
                    <div class="relative flex justify-center lg:justify-end text-center text-stone-900 text-xs font-bold italic font-['Roboto'] mt-3">
                        <p class="relative w-full max-w-sm sm:max-w-md">
                            *Tour dates are subject to the Student Calendar. Some days may not have tours due to student breaks or finals. Click 
                            <a href="https://registrar.virginia.edu/calendar/academic/2025-2026" class="underline">here</a> for details.
                        </p>
                    </div>
                </div>

            </div>
        </div>
        
    </section>

    <!-- Carousel: Cards Link Section -->
    <section>
        <div class="scrollElement pb-20 md:pb-0">
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
            :autoplay="{ delay: 4000, disableOnInteraction: false, pauseOnMouseEnter: true }"
            class="mySwiper"
            :breakpoints="{
                320: { slidesPerView: 1, slidesPerGroup: 1, spaceBetween: 10 },
                640: { slidesPerView: 2, slidesPerGroup: 2, spaceBetween: 35 },
                1024: { slidesPerView: 3, slidesPerGroup: 3, spaceBetween: 25 },
                1280: { slidesPerView: 4, slidesPerGroup: 4, spaceBetween: 30 }
            }"
        >
            <!-- Card 1 -->
            <swiper-slide>
                <a href="/about-tours">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/TourTaking3_Cropped.jpg"
                        alt="Columns at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        About Tours
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 2 -->
            <swiper-slide>
                <a href="/your-visit">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_YourVisit.jpg"
                        alt="Panels of a Pavillion at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        Take a Tour
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 3 -->
            <swiper-slide>
                <a href="/for-educators">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_ForEducators.jpg"
                        alt="Close up of bottom of the columns at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        For Educators (K-12+)
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 4 -->
            <swiper-slide>
                <a href="/contact-us">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_ContactUs.jpg"
                        alt="Image of a tree and an arch made of brick"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        Contact Us
                    </p>
                    </div>
                </a>
            </swiper-slide>
            
            <!-- Card 5 -->
            <swiper-slide>
                <a href="/join-guides">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_AboutOurGuides.jpeg"
                        alt="Columns at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        About Our Guides
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 6 -->
            <swiper-slide>
                <a href="/feedback">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_Feedback.jpeg"
                        alt="Panels of a Pavillion at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        Feedback
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 7 -->
            <swiper-slide>
                <a href="/join-guides#join-guides">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_BecomeAGuide.jpeg"
                        alt="Close up of bottom of the columns at the Academical Village"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out brightness-70 group-hover:brightness-60"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        Become a Guide
                    </p>
                    </div>
                </a>
            </swiper-slide>
        
            <!-- Card 8 -->
            <swiper-slide>
                <a href="/donate">
                    <div class="relative w-full p-4 group cursor-pointer">
                    <NuxtImg
                        src="/index-page/carousel-cards/Carousel_Donate.jpeg"
                        alt="Image of a tree and an arch made of brick"
                        class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                    />
                    <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                        Donate
                    </p>
                    </div>
                </a>
            </swiper-slide>
            </swiper>
        </div>
    </section>

    <!-- Who We Are Section -->
    <section>
        <div class="relative overflow-visible">

            <!--Background Image-->
            <NuxtImg 
                src="/index-page/FrontPage_WhoWeAre.jpg"
                alt="My image file description"
                class="overflow-visible h-screen w-full object-cover mask-t-from-10% opacity-40"
            >
            </NuxtImg>
            <div class="scrollElement absolute top-1/2 left-1/2 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20 -translate-x-1/2 -translate-y-1/2 text-center">
                <!-- Header -->
                <h1 class="font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                    Who We Are
                </h1>

                <!-- Description -->
                <p class="scrollElement font-['Montserrat'] text-black sm:text-lg md:text-xl leading-relaxed mx-auto mt-10">
                    The Virginia Guides Service is an independent student-run volunteer tour-giving organization that provides the historical and admissions tours of the University of Virginia.
                    Virginia Guides is an organization that embodies a spirit of student self-governance and seeks to foster a sense of unity and cohesion among its members. 
                </p>
                <p class="scrollElement font-['Montserrat'] text-black sm:text-lg md:text-xl leading-relaxed mx-auto mt-2">
                    Our tour guides are students who are put through a rigorous training semester where they learn the ins and outs of UVA's history while practicing crucial tour-giving skills.
                    Trainees receive mentorship from experienced guides, professors, and historical organization leaders in the Charlottesville community. All tours are conducted free of charge.
                </p>

                <div class="scrollElement mt-15 flex flex-col md:flex-row justify-center items-center gap-x-6 gap-y-4 pointer-events-auto">
                    <!-- Button 1: Learn More -->
                    <a href="/join-guides">
                        <button class="font-['Roboto'] bg-royal-blue hover:bg-gray-200 hover:shadow-md hover:text-royal-blue text-white rounded-full
                                    py-3 px-10 text-sm
                                    sm:py-4 sm:px-10 sm:text-base
                                    md:px-14 md:text-lg
                                    hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                        Learn More
                        </button>
                    </a>

                    <!-- Button 2: Donate -->
                    <a href="/donate">
                        <button class="font-['Roboto'] bg-royal-blue hover:bg-gray-200 hover:shadow-md hover:text-royal-blue text-white rounded-full
                                    py-3 px-13 text-sm
                                    sm:py-4 sm:px-16 sm:text-base
                                    md:px-18 md:text-lg
                                    hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                        Donate
                        </button>
                    </a>

                    <!-- Button 3: Become a Guide -->
                    <a href="/join-guides#join-guides">
                        <button class="font-['Roboto'] bg-royal-blue hover:bg-gray-200 hover:shadow-md hover:text-royal-blue text-white rounded-full
                                    py-3 px-6 text-sm
                                    sm:py-4 sm:px-8 sm:text-base
                                    md:px-9 md:text-lg
                                    hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                        Become a Guide
                        </button>
                    </a>
                </div>

            </div>
        </div>
    </section>

    <!--Instagram Plug section-->
    <section>
        <div class="relative w-full shadow-md bg-royal-blue py-6 px-4">
            <div class="max-w-screen-xl mx-auto flex flex-col md:flex-row items-center justify-evenly gap-5">

                <!-- Description -->
                <div class="font-['Montserrat'] text-white italic text-center justify-start text-sm md:text-base md:text-left max-w-xl">
                    Follow us on 
                    <a href="https://www.instagram.com/virginiaguides/" class="underline cursor-pointer">Instagram</a>
                     for updates on Virginia history, mission and development tours, scheduling, and inclement weather alerts. Stay connected and never miss important news or events!
                </div>

                <!-- Logo Text -->
                <div class="font-['Montserrat'] text-white flex items-center justify-between gap-3 text-2xl md:text-3xl font-semibold">
                    <a href="https://instagram.com/virginiaguides">
                        <svg class="h-10 w-10" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                        </svg>
                    </a>
                    <a href="https://www.instagram.com/virginiaguides/">
                        virginiaguides
                    </a>
                </div>

            </div>
        </div>

    </section>

    <!-- Explore UVA History Section -->
    <ExploreUVAHistoryBlue />

    <!--Carousel: Tour Review Section-->
    <div class="scrollElement review-carousel-body">
        <div class="review-slider">
            <div class="review-slide-track grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

                <!-- Review 1 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <!-- Date -->
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        January 2024
                    </p>
                    <!-- Review Text -->
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “[Guide name]—he was so well informed and thoughtful in explaining the historical
                        relationship to history and the importance of understanding it in the present.”
                    </p>
                </div>

                <!-- Review 2 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)]  p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Well researched presentation. She did a great job putting various events onto a timeline, 
                        which in turned helped to explain the contemporary mindset. She also communicated her love of the university.”
                    </p>
                </div>

                <!-- Review 3 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “I was very impressed with how well the event was organized. 
                        I reached out in January when most students were still on break and got a response within 2 days! 
                        It was a real pleasure to see such professionalism coming from young people! Bravo and thank you for all you do.”
                    </p>
                </div>

                <!-- Review 4 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Our tour guide, [guide], was incredibly knowledgeable and engaging. 
                        We learned a lot about UVA, Charlottesville, and Virginia through her fantastic storytelling.”
                    </p>
                </div>

                <!-- Review 5 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “[Guide], the tour guide, was knowledgeable, enthusiastic, and articulate. 
                        The tour itself was well-balanced and managed, in a well-structured way, to cover a variety of interesting subjects.”
                    </p>
                </div>

                <!-- Review 6 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “This critical/complicated understanding and connection to the institutions 
                        we come from are so essential to figuring out how we move forward.“
                    </p>
                </div>
            
                <!-- Review 7 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        "Going to Monticello after UVa was really important and looking back at the Rotunda from Monticello 
                        to see how the organization of the house is related to the organization of the institution, citizenship, 
                        and the nation which makes you really question how these spaces normalized what they stood for.”
                    </p>
                </div>
            
                <!-- Review 8 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Thank you for your outstanding tour and extraordinarily generous hospitality. I think our students got 
                        a chance to see through your example what an exemplary UVa student sounds like. You also allowed me to 
                        reconnect with where I come from. So I can't thank you enough.”
                    </p>
                </div>

                <!--Same 8 slides (doubled)-->

                <!-- Review 1 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <!-- Date -->
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        January 2024
                    </p>
                    <!-- Review Text -->
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “[Guide name]—he was so well informed and thoughtful in explaining the historical
                        relationship to history and the importance of understanding it in the present.”
                    </p>
                </div>

                <!-- Review 2 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Well researched presentation. She did a great job putting various events onto a timeline, 
                        which in turned helped to explain the contemporary mindset. She also communicated her love of the university.”
                    </p>
                </div>

                <!-- Review 3 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “I was very impressed with how well the event was organized. 
                        I reached out in January when most students were still on break and got a response within 2 days! 
                        It was a real pleasure to see such professionalism coming from young people! Bravo and thank you for all you do.”
                    </p>
                </div>

                <!-- Review 4 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Our tour guide, [guide], was incredibly knowledgeable and engaging. 
                        We learned a lot about UVA, Charlottesville, and Virginia through her fantastic storytelling.”
                    </p>
                </div>

                <!-- Review 5 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “[Guide], the tour guide, was knowledgeable, enthusiastic, and articulate. 
                        The tour itself was well-balanced and managed, in a well-structured way, to cover a variety of interesting subjects.”
                    </p>
                </div>
            
                <!-- Review 6 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “This critical/complicated understanding and connection to the institutions 
                        we come from are so essential to figuring out how we move forward.“
                    </p>
                </div>
            
                <!-- Review 7 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        "Going to Monticello after UVa was really important and looking back at the Rotunda from Monticello 
                        to see how the organization of the house is related to the organization of the institution, citizenship, 
                        and the nation which makes you really question how these spaces normalized what they stood for.”
                    </p>
                </div>
            
                <!-- Review 8 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        October 2025
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] overflow-auto">
                        “Thank you for your outstanding tour and extraordinarily generous hospitality. I think our students got 
                        a chance to see through your example what an exemplary UVa student sounds like. You also allowed me to 
                        reconnect with where I come from. So I can't thank you enough.”
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!--Our Events Section-->
    <section class="relative w-full">
        <!-- Background image with opacity -->
        <div class="absolute inset-0">
            <div class="w-full h-full bg-[url('/index-page/OurEvents_Background.jpg')] bg-cover bg-center opacity-50"></div>
        </div>

        <!-- Content above background -->
        <div class="relative px-6 sm:px-8 lg:px-16 py-12 sm:py-16">
            <div class="flex flex-col md:flex-row items-start gap-10">
            
            <!-- Left: Column Information -->
            <div class="w-full md:w-2/5 flex justify-start">
                <div class="relative w-full">
                <p class="scrollElement font-['Playfair_Display'] font-bold text-black text-4xl sm:text-5xl leading-tight mb-6">
                    Our Events
                </p>
                <p class="scrollElement font-['Montserrat'] font-semibold text-base sm:text-lg leading-relaxed text-black">
                    Join us in our work of telling a more honest, just, and complete telling of UVA's history.
                </p>
                </div>
            </div>

            <!-- Right: Event Image Slider -->
            <swiper
                :slides-per-view="1"
                :slides-per-group="1"
                :space-between="30"
                :pagination="{ clickable: true }"
                :grabCursor="true"
                :autoplay="{ delay: 10000, disableOnInteraction: false, pauseOnMouseEnter: true }"
                :loop="true"
                :speed="800"
                :modules="modules"
                class="scrollElement events-swiper mx-auto max-w-4xl"
            >
                <!-- Card 1 -->
                <swiper-slide class="flex justify-end items-center">
                    <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                        <img class="events-image mb-2" loading="lazy" src="/index-page/OurEvents_Tour.jpg">
                        <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                        Summer Tours: History of UVA and Prospective Student Tour*
                        </p>
                        <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                        Our commitment to providing a more complete history of the University of Virginia carries on this summer.
                        </p>
                    </div>
                </swiper-slide>

                <!-- Card 2 -->
                <swiper-slide class="flex justify-center items-center">
                    <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                        <img class="events-image mb-2" loading="lazy" src="/index-page/OurEvents_Fundraising.jpg">
                        <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                        Fundraising Event Title Here
                        </p>
                        <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                        Insert fundraising information here.
                        </p>
                    </div>
                </swiper-slide>

                <!-- Card 3 -->
                <swiper-slide class="flex justify-center items-center">
                    <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                        <img class="events-image mb-2" loading="lazy" src="/index-page/OurEvents_SpecialtyTours.jpg">
                        <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                        Specialty Tours Returning in the Fall
                        </p>
                        <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                        Our specialty tours dive deeper into a specific aspect of UVA's history such as Women's History and the History of African Americans at UVA.
                        </p>
                    </div>
                </swiper-slide>
            </swiper>

            </div>
        </div>
    </section>

    <Footer />

</template>

<style>
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 8rem;
    }
    /* Scrolling Effect */
    .scrollElement {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .scrollElement.show {
        opacity: 1;
        transform: translateY(0);
    }
    /* Carousel for the Tour Reviews Section */
    .review-carousel-body {
        width: 100%;
        height: var(--height);
        display: grid;
        place-items: center;
    }
    .review-slider{
        height: 400px;
        margin: auto;
        position: relative;
        width: 100%;
        display: grid;
        place-items: center;
        overflow: hidden;
    }
    .review-slide-track{
        display: flex;
        width: calc(350px * 16);
        animation: scroll-right 20s linear infinite;
    }
    /* Right to left */
    @keyframes scroll-right {
        0% {
            transform: translateX(calc(-350px * 8));
        }
        100% {
            transform: translateX(0);
        }
    }
    .review-slide-track:hover{
        animation-play-state: paused;
    }
    .review-slide{
        height: 250px;
        width: 350px;
        display: flex;
        align-items: center;
        padding: 15px;
        perspective: 100px;
    }

    /* Swiper for the Our Events Section */
    .events-swiper{
        width: 100%;
        /* padding: 15px 40px; */
    }
    /* Target pagination inside .events-swiper */
    .events-swiper .swiper-pagination {
        position: absolute;
    }
    .events-swiper .swiper-pagination-bullet {
        height: 10px;
        width: 10px;
        background: black;
    }
    .events-image {
        width: 100%;
        height: 450px;
        object-fit: cover;     
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
        width: calc(350px * 10); /* total # of slides x individual slide width */
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

    /* Carousel for the Link Cards */
    .mySwiper{
        width: 100%;
        padding: 40px 40px;
    }
    .swiper-pagination {
        position: absolute;
    }
    .swiper-pagination-bullet {
        height: 7px;
        width: 26px;
        border-radius: 25px;
        background: #A86645;
    }
    .swiper-button-next,
    .swiper-button-prev {
        color: #A86645;
    }
</style>

<script setup>
    import { Swiper, SwiperSlide } from "swiper/vue";
    import "swiper/css";
    import "swiper/css/pagination";
    import "swiper/css/navigation";
    import { Pagination, Navigation, Autoplay } from "swiper/modules";
    import { onMounted } from "vue";
    import Footer from '~/components/Footer.vue';
    import ExploreUVAHistoryBlue from '~/components/ExploreUVAHistoryBlue.vue';

    // IntersectionObserver logic
    onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        } else {
            entry.target.classList.remove("show");
        }
        });
    });

    const scrollElements = document.querySelectorAll(".scrollElement");
    scrollElements.forEach((element) => observer.observe(element));
    });

    // Swiper modules for this component
    const modules = [Pagination, Navigation, Autoplay];
</script>
