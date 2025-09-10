<template>
    <!--Header Section-->
    <header class="relative overflow-visible h-[110vh] w-full bg-[url('/Header_FrontPage.png')] bg-cover bg-center md:bg-left sm:bg-center" aria-label="Virginia Guides Hero Section">
        <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
            <h1 class="font-['Playfair_Display'] italic whitespace-nowrap text-[clamp(3rem,9.5vw,5.5rem)] leading-tight">
                VIRGINIA GUIDES
            </h1>
            <p class="font-['Roboto'] text-base sm:text-lg md:text-xl font-semibold leading-snug">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
            <button class="font-['Roboto'] mt-15 px-6 py-2 text-lg text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 border hover:border-neutral-300 rounded-full cursor-pointer transition-all duration-300 ease-in-out"
            aria-label="Explore Virginia Guides">
                Plan Your Visit
            </button>
        </div>
        <div class="absolute flex flex-col items-center top-3/4 md:top-5/6 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 text-white text-center">
            <p class="font-['Montserrat'] text-base sm:text-lg md:text-xl font-light leading-snug">
                The Virginia Guides Service continues 75 years of students guiding visitors through UVA.<br />
                Carrying forward tradition while bringing new light to the past.
            </p>
            <!-- <svg class="pt-3 w-12 h-12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M12 17L12 7M12 17L8 13M12 17L16 13M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#ffffff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg> -->
        </div>
    </header>

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
                            src="/index-page/1800UVA.jpg"
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
                        <!--Button-->
                        <div class="absolute left-1/2 bottom-20 -translate-x-1/2">
                            <button class="font-['Montserrat'] text-lg font-semibold px-6 py-2 rounded-[20px] text-white hover:text-white bg-dark-orange border-neutral-700 hover:bg-neutral-900/85 cursor-pointer transition-all duration-300 ease-in-out"
                                aria-label="Explore Virginia Guides">
                                TAKE A TOUR
                            </button>
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

    <!-- Carousel: Cards Link Section -->
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
            :breakpoints="{
                320: { slidesPerView: 2, slidesPerGroup: 2, spaceBetween: 10 },
                640: { slidesPerView: 3, slidesPerGroup: 3, spaceBetween: 35 },
                1024: { slidesPerView: 3, slidesPerGroup: 3, spaceBetween: 25 },
                1280: { slidesPerView: 4, slidesPerGroup: 4, spaceBetween: 30 }
            }"
        >
            <!-- Card 1 -->
            <swiper-slide>
                <div class="relative w-full p-4 group cursor-pointer">
                <NuxtImg
                    src="/index-page/carousel-cards/Carousel_Tours.jpg"
                    alt="Columns at the Academical Village"
                    class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                />
                <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                    Our Tours
                </p>
                </div>
            </swiper-slide>
        
            <!-- Card 2 -->
            <swiper-slide>
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
            </swiper-slide>
        
            <!-- Card 3 -->
            <swiper-slide>
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
            </swiper-slide>
        
            <!-- Card 4 -->
            <swiper-slide>
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
            </swiper-slide>
            
            <!-- Card 5 -->
            <swiper-slide>
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
            </swiper-slide>
        
            <!-- Card 6 -->
            <swiper-slide>
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
            </swiper-slide>
        
            <!-- Card 7 -->
            <swiper-slide>
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
            </swiper-slide>
        
            <!-- Card 8 -->
            <swiper-slide>
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
            </swiper-slide>
        </swiper>
    </section>

    <!-- Who We Are Section -->
    <section>
        <div class="relative overflow-visible">

            <!--Background Image-->
            <NuxtImg 
                src="/index-page/FrontPage_WhoWeAre.jpg"
                alt="My image file description"
                class="overflow-visible min-h-screen w-full object-cover mask-t-from-10% opacity-40"
            >
            </NuxtImg>

            <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-center">
                <!-- Header -->
                <h1 class="font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                    Who We Are
                </h1>

                <!-- Description -->
                <p class="font-['Montserrat'] text-black sm:text-lg md:text-xl leading-relaxed mx-auto mt-10">
                    The Virginia Guides Service is an independent student-run volunteer tour-giving organization that provides the admissions and historical tours of the University of Virginia.
                    Virginia Guides is an organization that embodies a spirit of student self-governance and seeks to foster a sense of unity and cohesion among its members. 
                    <br>
                    <br>
                    Our tour guides are students who are put through a rigorous training semester where they learn the ins and outs of UVA's history while practicing crucial tour-giving skills.
                    Trainees receive mentorship from experienced guides, professors, and historical organization leaders in the Charlottesville community. All tours are conducted free of charge.
                </p>

                <!-- Button Section -->
                <div class="mt-10 flex flex-col md:flex-row justify-center items-center gap-x-25 gap-y-4 pointer-events-auto">
                    <!-- Button 1: Learn More -->
                    <button class="font-['Roboto'] bg-royal-blue hover:bg-blue-950 text-white rounded-full py-4 px-14 transition-all duration-300 ease-in-out cursor-pointer">
                        Learn More
                    </button>

                    <!-- Button 2: Donate -->
                    <button class="font-['Roboto'] bg-royal-blue hover:bg-blue-950 text-white rounded-full py-4 px-18 transition-all duration-300 ease-in-out cursor-pointer">
                        Donate
                    </button>

                    <!-- Button 3: Become a Guide -->
                    <button class="font-['Roboto'] bg-royal-blue hover:bg-blue-950 text-white rounded-full py-4 px-10 transition-all duration-300 ease-in-out cursor-pointer">
                        Become a Guide
                    </button>
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
                    <!--Wrap in a link-->
                    <a href="https://www.instagram.com/virginiaguides/">
                        <!-- Instagram Icon -->
                        <svg class="w-10 h-10" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12 18C15.3137 18 18 15.3137 18 12C18 8.68629 15.3137 6 12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18ZM12 16C14.2091 16 16 14.2091 16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16Z" fill="#ffffff"></path> <path d="M18 5C17.4477 5 17 5.44772 17 6C17 6.55228 17.4477 7 18 7C18.5523 7 19 6.55228 19 6C19 5.44772 18.5523 5 18 5Z" fill="#ffffff"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M1.65396 4.27606C1 5.55953 1 7.23969 1 10.6V13.4C1 16.7603 1 18.4405 1.65396 19.7239C2.2292 20.8529 3.14708 21.7708 4.27606 22.346C5.55953 23 7.23969 23 10.6 23H13.4C16.7603 23 18.4405 23 19.7239 22.346C20.8529 21.7708 21.7708 20.8529 22.346 19.7239C23 18.4405 23 16.7603 23 13.4V10.6C23 7.23969 23 5.55953 22.346 4.27606C21.7708 3.14708 20.8529 2.2292 19.7239 1.65396C18.4405 1 16.7603 1 13.4 1H10.6C7.23969 1 5.55953 1 4.27606 1.65396C3.14708 2.2292 2.2292 3.14708 1.65396 4.27606ZM13.4 3H10.6C8.88684 3 7.72225 3.00156 6.82208 3.0751C5.94524 3.14674 5.49684 3.27659 5.18404 3.43597C4.43139 3.81947 3.81947 4.43139 3.43597 5.18404C3.27659 5.49684 3.14674 5.94524 3.0751 6.82208C3.00156 7.72225 3 8.88684 3 10.6V13.4C3 15.1132 3.00156 16.2777 3.0751 17.1779C3.14674 18.0548 3.27659 18.5032 3.43597 18.816C3.81947 19.5686 4.43139 20.1805 5.18404 20.564C5.49684 20.7234 5.94524 20.8533 6.82208 20.9249C7.72225 20.9984 8.88684 21 10.6 21H13.4C15.1132 21 16.2777 20.9984 17.1779 20.9249C18.0548 20.8533 18.5032 20.7234 18.816 20.564C19.5686 20.1805 20.1805 19.5686 20.564 18.816C20.7234 18.5032 20.8533 18.0548 20.9249 17.1779C20.9984 16.2777 21 15.1132 21 13.4V10.6C21 8.88684 20.9984 7.72225 20.9249 6.82208C20.8533 5.94524 20.7234 5.49684 20.564 5.18404C20.1805 4.43139 19.5686 3.81947 18.816 3.43597C18.5032 3.27659 18.0548 3.14674 17.1779 3.0751C16.2777 3.00156 15.1132 3 13.4 3Z" fill="#ffffff"></path> </g></svg>

                    </a>
                    <a href="https://www.instagram.com/virginiaguides/">
                        virginiaguides
                    </a>
                </div>

            </div>
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
            <button class="inline-flex items-center space-x-3 rounded-full border text-white font-['Montserrat'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-royal-blue hover:bg-neutral-300 transition-all duration-300 ease-in-out">
                <span>HISTORY TOURS</span>
                <svg class="flex-shrink-0" height="25px" width="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 12H18M18 12L13 7M18 12L13 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
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
                            <p class="carousel-text self-start text-white  font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-white  font-['Roboto']">Garden Tours</p>
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

    <!--Carousel: Tour Review Section-->
    <div class="review-carousel-body">
        <div class="review-slider">
            <div class="review-slide-track grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

                <!-- Review 1 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <!-- Date -->
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        January 2024
                    </p>
                    <!-- Review Text -->
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “[Guide name]—he was so well informed and thoughtful in explaining the historical
                        relationship to history and the importance of understanding it in the present.”
                    </p>
                </div>

                <!-- Review 2 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)]  p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “Well researched presentation. She did a great job putting various events onto a timeline, 
                        which in turned helped to explain the contemporary mindset. She also communicated her love of the university.”
                    </p>
                </div>

                <!-- Review 3 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
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
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “Our tour guide, [guide], was incredibly knowledgeable and engaging. 
                        We learned a lot about UVA, Charlottesville, and Virginia through her fantastic storytelling.”
                    </p>
                </div>

                <!-- Review 5 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “[Guide], the tour guide, was knowledgeable, enthusiastic, and articulate. 
                        The tour itself was well-balanced and managed, in a well-structured way, to cover a variety of interesting subjects.”
                    </p>
                </div>

                <!--Same 5 slides (doubled)-->

                <!-- Review 1 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <!-- Date -->
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        January 2024
                    </p>
                    <!-- Review Text -->
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “[Guide name]—he was so well informed and thoughtful in explaining the historical
                        relationship to history and the importance of understanding it in the present.”
                    </p>
                </div>

                <!-- Review 2 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “Well researched presentation. She did a great job putting various events onto a timeline, 
                        which in turned helped to explain the contemporary mindset. She also communicated her love of the university.”
                    </p>
                </div>

                <!-- Review 3 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
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
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “Our tour guide, [guide], was incredibly knowledgeable and engaging. 
                        We learned a lot about UVA, Charlottesville, and Virginia through her fantastic storytelling.”
                    </p>
                </div>

                <!-- Review 5 -->
                <div class="review-slide flex flex-col w-full h-64 bg-white rounded-lg shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] p-4 relative">
                    <p class="absolute top-2 right-4 text-black text-sm sm:text-base font-semibold font-['Montserrat']">
                        February 2024
                    </p>
                    <p class="mt-8 text-black text-base sm:text-lg font-medium font-['Montserrat'] line-clamp-6">
                        “[Guide], the tour guide, was knowledgeable, enthusiastic, and articulate. 
                        The tour itself was well-balanced and managed, in a well-structured way, to cover a variety of interesting subjects.”
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!--Our Events Section-->
    <section class="relative w-full">
    <!-- Background image with opacity -->
    <div class="absolute inset-0">
        <div class="w-full h-full bg-[url('/index-page/OurEvents_Background.jpg')] bg-cover bg-left opacity-50"></div>
    </div>

    <!-- Content above background -->
    <div class="relative px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
        <div class="flex flex-col md:flex-row items-stretch gap-10">

        <!-- Left: Column Information -->
        <div class="w-full md:w-2/5 flex justify-center md:justify-end">
            <div class="relative w-full max-w-sm sm:max-w-md overflow-hidden mt-5">
            <p class="font-['Playfair_Display'] font-bold text-black text-4xl sm:text-5xl leading-tight mb-6">
                Our Events
            </p>
            <p class="font-['Montserrat'] font-semibold text-base sm:text-lg leading-relaxed text-black">
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
            class="events-swiper w-full"
        >
            <!-- Card 1 -->
            <swiper-slide>
            <div class="relative w-full lg:w-[75%] mx-auto p-4 pb-10 group cursor-pointer">
                <img class="events-image mb-2" src="/index-page/OurEvents_Tour.jpg">
                <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                Summer Tours: History of UVA and Prospective Student Tour*
                </p>
                <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                Our commitment to providing a more complete history of the University of Virginia carries on this summer.
                </p>
            </div>
            </swiper-slide>

            <!-- Card 2 -->
            <swiper-slide>
            <div class="relative w-full lg:w-[75%] mx-auto p-4 pb-10 group cursor-pointer">
                <img class="events-image mb-2" src="/index-page/OurEvents_Fundraising.jpg">
                <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                Fundraising Event Title Here
                </p>
                <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                Insert fundraising information here.
                </p>
            </div>
            </swiper-slide>

            <!-- Card 3 -->
            <swiper-slide>
            <div class="relative w-full lg:w-[75%] mx-auto p-4 pb-10 group cursor-pointer">
                <img class="events-image mb-2" src="/index-page/OurEvents_SpecialtyTours.jpg">
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
                <button class="font-['Roboto'] border border-white text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 hover:border-transparent rounded-full py-3 px-10 cursor-pointer transition-all duration-300 ease-in-out">
                PLAN YOUR VISIT
                </button>
                <button class="font-['Roboto'] border border-white text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-neutral-300 hover:border-transparent rounded-full py-3 px-18 cursor-pointer transition-all duration-300 ease-in-out">
                DONATE
                </button>
            </div>

            <!-- Description -->
            <p class="mt-20 font-['Roboto'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                The Virginia Guides Service at UVA is an entirely student-run independent volunteer organization. 
                If you would like to provide additional support, please consider donating to our day-to-day operations 
                <a href="" class="underline">here</a>. We appreciate your time and thank you for continuing to support our mission.
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
                    <li class="cursor-pointer">Directions + FAQ</li>
                    <li class="cursor-pointer">History Tours</li>
                    <li class="cursor-pointer">Specialty Tours</li>
                    <li class="cursor-pointer">Specialty Tours Request</li>
                </ul>

                <!-- Column 2 -->
                <ul class="flex flex-col gap-2 min-w-[100px]">
                    <li class="font-['Playfair_Display'] italic underline text-white text-lg">About Us</li>
                    <li class="cursor-pointer">Our Mission</li>
                    <li class="cursor-pointer">Become a Guide</li>
                    <li class="cursor-pointer">Feedback</li>
                    <li class="cursor-pointer">Instagram</li>
                </ul>

                <!-- Column 3 -->
                <ul class="flex flex-col gap-2 min-w-[100px]">
                    <li class="font-['Playfair_Display'] italic underline text-white text-lg">More</li>
                    <li class="cursor-pointer">For Educators</li>
                    <li class="cursor-pointer">Donate</li>
                </ul>
                </div>


                <!-- Right Side Footer -->
                <div class="basis-1/2 flex flex-col gap-3 text-zinc-400 text-sm md:text-base font-light">
                    <div class="flex items-start gap-4 font-['Roboto']">
                        <img class="h-12 w-12 obSject-contain" src="/guides-logo.png" alt="Virginia Guides Logo" />
                        <p>
                            The Virginia Guides continues 75 years of guiding visitors through UVA. The Guides Service is a student-run organization independent of the University of Virginia, carrying forward tradition while bringing a more complete light to the past.
                        </p>
                    </div>

                    <div class="flex justify-center md:justify-end">
                        <button class="border border-white text-white rounded-full px-6 py-2 font-['Montserrat'] hover:bg-zinc-500 hover:border-zinc-500 hover:text-black transition-all duration-300 ease-in-out cursor-pointer">
                            CONTACT US
                        </button>
                    </div>
                </div>

            </div>
        </div>
    </section>

</template>

<style>
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 6rem;
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
        width: calc(350px * 18);
        animation: scroll-right 20s linear infinite;
    }
    /* Right to left */
    @keyframes scroll-right {
        0% {
            transform: translateX(calc(-350px * 5));
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

<script>
    import { Swiper, SwiperSlide } from "swiper/vue";
    import "swiper/css";
    import "swiper/css/pagination";
    import "swiper/css/navigation";
    import { Pagination, Navigation, Autoplay } from "swiper/modules";

    export default {
        components: {
        Swiper,
        SwiperSlide,
        },
        setup() {
        return {
            modules: [Pagination, Navigation, Autoplay],
        };
        },
    };
</script>