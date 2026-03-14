<!-- 
============================================================================
FRONT PAGE (virginiaguides.org)
============================================================================
  
  Main landing page for the Virginia Guide Service website
  
  Page Structure:
  1. Hero Section - Full-screen header with branding and scroll animations
  2. Mission & Tour Info - Two-column layout with mission statement and tour times
  3. Navigation Carousel - 8 interactive cards linking to main site sections
  4. Who We Are - Organization overview with background image
  5. Instagram Plug - Social media banner
  6. Explore UVA History - Component for historical content carousel
  7. Tour Reviews - Infinite scrolling carousel of visitor testimonials
  8. Our Events - Upcoming events with image slider
  9. Footer - Site-wide footer component

  Performance Choices:
  1. Hero image preloaded via useHead (fixes LCP — browser fetches before CSS parses)
  2. Google Fonts preconnect added to useHead (reduces font load latency)
  3. NuxtImg carousel cards get explicit width/height/loading=lazy (fixes CLS, defers offscreen fetches)
  4. Who We Are NuxtImg gets loading=eager + fetchpriority=high (it's near-fold)
  5. will-change: transform on both animated CSS tracks (GPU compositing)

============================================================================
-->
<template>
    <!-- Intersection Observer target - invisible element that triggers scroll animations when out of view -->
    <div ref="topElement" class="w-full"></div>

    <!-- ========================================
         HERO SECTION
         Full-height header (115vh) with main branding, call to action (CTA) button, and scroll indicators
         ======================================== -->
    <header class="relative overflow-visible h-[115vh] w-full bg-[url('https://virginia-guides-website-images.s3.amazonaws.com/public/Header_FrontPageNew.jpg')] bg-cover bg-center" aria-label="Virginia Guides Hero Section">
        <!-- Main Title Container - Centered with slight offset on XL screens -->
        <div class="absolute top-[50%] xl:top-[52%] left-[50%] xl:left-[48%] w-full max-w-7xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
                <!-- 
                    Main Heading: "VIRGINIA GUIDES"
                    - First letters (V, G) enlarged for visual emphasis
                    - Fluid typography: clamp(min, preferred, max) for responsive scaling
                    - Text shadow for legibility over background image
                -->
                <h1 class="font-['Playfair_Display'] text-center xl:text-right italic text-[clamp(2.5rem,9.5vw,6rem)] leading-tight [text-shadow:0px_4px_4px_rgb(0_0_0/0.25)]">
                    <!-- V and G in "Virignia Guides" are slightly bigger for style -->
                    <span class="text-[clamp(3.5rem,10.5vw,7rem)]">V</span>IRGINIA
                    <span class="text-[clamp(3.5rem,10.5vw,7rem)]">G</span>UIDES
                </h1>
            <!-- Subtitle - Site tagline -->
            <p class="font-Roboto text-center xl:text-right text-sm sm:text-lg md:text-md font-semibold leading-snug [text-shadow:3px_3px_6px_rgb(0_0_0/0.70)]">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
            <!-- Primary call to action button - Links to tour registration page -->
            <div class="text-center xl:text-right xl:pr-30">
                <a href="/your-visit">
                    <button class="font-Roboto font-medium mt-10 px-6 py-2 sm:px-8 sm:py-2 text-lg md:px-12 md:py-3 md:text-2xl text-white hover:text-royal-blue bg-[rgba(0,0,0,0.45)] hover:bg-gray-100 border hover:border-gray-100 rounded-full cursor-pointer hover:scale-105 transition-all duration-300 ease-in-out" aria-label="Explore Virginia Guides">
                        Take a Tour
                    </button>
                </a>
            </div>
        </div>

        <!-- 
            Animated Scroll Indicator (Down Arrow)
            - Visible only when user is at top of page (isAtTop = true)
            - Bouncing animation encourages scrolling
            - Smooth fade-out transition when scrolling begins
            - Links to #more-info section
        -->
        <a href="#more-info">
            <div ref="iconWrap" :class="['absolute flex flex-col items-center top-[75%] lg:pt-8 left-1/2 w-full max-w-4xl px-4 -translate-x-1/2 text-white text-center transition-all duration-500', isAtTop ? 'opacity-100 scale-100 pointer-events-auto' : 'opacity-0 scale-90 pointer-events-none']" aria-hidden="!isAtTop">
                <!-- Down Arrow Circle SVG with bounce animation -->
                <svg
                    class="animate-bounce pt-3 w-14 h-14 cursor-pointer hover:scale-105 transition-all duration-300 ease-in-out"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    d="M12 17L12 7M12 17L8 13M12 17L16 13M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                    stroke="#ffffff"
                    stroke-width="1.25"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                ></path>
                </svg>
            </div>
        </a>
        
        <!-- 
            Mission Statement Text (appears after scrolling)
            - Hidden when at top, fades in after user scrolls down
            - Inverse visibility to scroll icon (when icon disappears, text appears)
            - Provides context about 75-year tradition of student guides
        -->
        <div ref="textWrap" :class="['absolute flex flex-col items-center top-[83%] lg:pt-8 md:top-5/6 left-1/2 w-full max-w-4xl px-4 -translate-x-1/2 text-white text-center transition-all duration-500', isAtTop ? 'opacity-0 translate-y-3 pointer-events-none' : 'opacity-100 translate-y-0 pointer-events-auto']" aria-hidden="isAtTop">
            <p class="font-['Montserrat'] italic text-base sm:text-lg md:text-xl font-light leading-snug">
                The Virginia Guide Service continues 75 years of students guiding visitors through UVA,
                carrying forward tradition while bringing new light to the past.
            </p>
        </div>
    </header>

    <!-- ========================================
         MISSION & TOUR INFO SECTION
         Two-column responsive layout:
         - Left: Mission statement
         - Right: Tour times card with schedule overlay
        ======================================== -->
    <section id="more-info" class="bg-white">
        <div class="mx-auto px-4 sm:px-6 lg:px-8 pt-12">
            <div class="flex flex-col lg:flex-row items-center gap-10 max-w-7xl mx-auto">
                <!-- ========================================
                     LEFT COLUMN: Mission Statement
                     ======================================== -->
                <div class="w-full lg:w-3/5">
                    <!-- Main Tagline -->
                    <p class="scrollElement font-['Playfair_Display'] italic font-bold text-dark-green text-4xl sm:text-5xl leading-tight pb-6">
                        Where The Past Stands<br />
                        And More Is Told.
                    </p>
                    <!-- 
                        Mission Statement 
                        CRITICAL NOTE: Keep font syntax as font-Montserrat 
                        DO NOT CHANGE TO font-['Montserrat']
                        Reason: Tailwind config issue - arbitrary syntax doesn't properly 
                        apply bold+italic combination with this font
                    -->
                    <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                        The American promise rests on the idea that all are created equal, and every story has a place in that legacy. 
                        Many who have shaped this University have long gone unrecognized. As we learn more, 
                        <a class="font-Montserrat font-semibold italic text-dark-green">our tours evolve — not to change the past, but to share more of it.</a>
                        <br /><br />
                        Jefferson's Academical Village is more than its founding. From the history of enslavement to 
                        liberation, desegregation to coeducation, it shapes and reflects the American story, recognized by UNESCO for this role, 
                        and is made richer as we share more.
                        <br /><br />
                        <!-- Emphasis: All tours are free -->
                        <a class="font-Montserrat text-dark-green font-medium italic">With this mission, </a>
                        <a class="font-Montserrat text-dark-green font-medium italic underline">all tours are offered free of charge.</a>
                    </p>
                </div>

                <!-- ========================================
                     RIGHT COLUMN: Tour Times Card
                     Interactive card with blurred background image and schedule overlay
                     ======================================== -->
                <div class="scrollElement w-full lg:w-2/5 flex flex-col">
                    <!-- Tour Times Card Container -->
                    <div class="relative flex justify-center lg:justify-end">
                        <div class="relative w-full max-w-sm sm:max-w-md h-[573px] overflow-hidden rounded-[35px] shadow-lg">

                            <!-- Background Image - Blurred and semi-transparent for text readability -->
                            <!-- Performance: explicit width/height prevent layout shift; loading=lazy defers this below-fold image -->
                            <img
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/TourTaking1_Blurry.jpg"
                                alt="Tour illustration"
                                width="448"
                                height="573"
                                loading="lazy"
                                class="absolute inset-0 w-full h-full object-cover rounded-[35px] opacity-80"
                            />

                            <!-- Header: "Tour Times" with Clock Icon -->
                            <div class="absolute top-[110px] left-6 text-left flex items-start gap-2 w-auto sm:w-90 md:w-90 lg:w-auto">
                                <!-- Clock Icon SVG -->
                                <svg viewBox="0 0 24 24" fill="none" class="w-7 h-7 mt-1 shrink-0" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 7V12L14.5 13.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" 
                                        stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>

                                <!-- Title and Meeting Location -->
                                <div class="flex flex-col">
                                    <p class="text-black text-2xl font-bold font-['Montserrat']">TOUR TIMES*</p>
                                    <p class="text-black text-sm font-medium font-['Montserrat']">
                                        All tours leave from the front Rotunda steps
                                    </p>
                                </div>
                            </div>

                            <!-- Overlay: Days and Times -->
                            <!-- Tour Schedule: Friday -->
                            <div class="absolute top-[179px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">FRIDAY</p>
                                <p class="text-black text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <!-- Tour Schedule: Saturday -->
                            <div class="absolute top-[234px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SATURDAY</p>
                                <p class="text-black text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <!-- Tour Schedule: Sunday -->
                            <div class="absolute top-[289px] left-15 w-36 text-left">
                                <p class="text-UVA-orange text-2xl font-semibold font-['Montserrat']">SUNDAY</p>
                                <p class="text-black text-base font-medium font-['Montserrat'] relative left-[25px]">11:00am-12:15PM</p>
                            </div>
                            <!-- Button: Take a Tour - Links to registration page -->
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
                    <!-- 
                        Disclaimer: Academic Calendar Notice
                        Links to UVA registrar for schedule exceptions
                        Positioned below the tour times card
                    -->
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

    <!-- ========================================
         NAVIGATION CAROUSEL SECTION
         Interactive card carousel with 8 navigation links
         Features:
         - Auto-play with 4s delay, pauses on hover
         - Looping enabled for continuous scrolling
         - Click, drag, and swipe interactions
         - Responsive breakpoints for all screen sizes
         - Image hover effects (brightness reduction)

         Performance: Wrapped in <ClientOnly> so Swiper JS is not included in the
         SSR bundle and does not block initial page render. A lightweight
         skeleton placeholder is shown while the component hydrates.
         ======================================== -->
    <section>
        <div class="scrollElement pb-20 md:pb-0">
            <div v-if="isMounted">
                <!-- 
                    Swiper Configuration:
                    Responsive breakpoints:
                    - 320px+: 1 slide per view (mobile portrait)
                    - 640px+: 2 slides per view (mobile landscape/small tablet)
                    - 1024px+: 3 slides per view (tablet)
                    - 1280px+: 4 slides per view (desktop)
                    
                    Navigation: Arrow buttons enabled
                    Pagination: Clickable dots enabled
                    Loop: Seamless infinite scrolling
                    Speed: 800ms transition
                    Autoplay: 4s delay, doesn't disable on interaction, pauses on hover
                -->
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
                    <!-- Card 1: About Tours -->
                    <!-- Links to general tour information page -->
                    <swiper-slide>
                        <a href="/about-tours">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <!-- Performance: width/height reserve space to prevent CLS; loading=lazy defers offscreen fetch -->
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/TourTaking3_Cropped.jpg"
                                alt="Columns at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                About Tours
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 2: Take a Tour -->
                    <!-- Links to visitor information and tour signup page -->
                    <swiper-slide>
                        <a href="/your-visit">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_YourVisit.jpg"
                                alt="Panels of a Pavillion at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                Take a Tour
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 3: For Educators -->
                    <!-- Links to educational resources for K-12+ teachers -->
                    <swiper-slide>
                        <a href="/for-educators">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_ForEducators.jpg"
                                alt="Close up of bottom of the columns at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                For Educators (K-12+)
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 4: Contact Us -->
                    <!-- Links to contact form -->
                    <swiper-slide>
                        <a href="/contact-us">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_ContactUs.jpg"
                                alt="Image of a tree and an arch made of brick"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                Contact Us
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                    
                    <!-- Card 5: About Our Guides -->
                    <!-- Links to information about the guide service -->
                    <swiper-slide>
                        <a href="/join-guides">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_AboutOurGuides.jpeg"
                                alt="Columns at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                About Our Guides
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 6: Feedback -->
                    <!-- Links to visitor feedback form -->
                    <swiper-slide>
                        <a href="/feedback">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_Feedback.jpeg"
                                alt="Panels of a Pavillion at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                Feedback
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 7: Become a Guide -->
                    <!-- Links to guide recruitment section -->
                    <!-- Note: Darker base brightness to make white text more readable -->
                    <swiper-slide>
                        <a href="/join-guides#join-guides">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_BecomeAGuide.jpeg"
                                alt="Close up of bottom of the columns at the Academical Village"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out brightness-70 group-hover:brightness-60"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                Become a Guide
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                
                    <!-- Card 8: Donate -->
                    <!-- Links to donation page -->
                    <swiper-slide>
                        <a href="/donate">
                            <div class="relative w-full p-4 group cursor-pointer">
                            <NuxtImg
                                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/carousel-cards/Carousel_Donate.jpeg"
                                alt="Image of a tree and an arch made of brick"
                                width="400"
                                height="300"
                                loading="lazy"
                                class="w-full rounded-lg transition-all duration-300 ease-in-out group-hover:brightness-75"
                            />
                            <!-- Centered overlay text -->
                            <p class="absolute inset-0 flex items-center justify-center font-['Montserrat'] text-center px-2 text-white font-bold text-base sm:text-lg md:text-xl">
                                Donate
                            </p>
                            </div>
                        </a>
                    </swiper-slide>
                </swiper>
            </div>
        </div>
    </section>

    <!-- ========================================
         WHO WE ARE SECTION
         Organization overview with background image
         Explains Virginia Guide Service mission and structure
         Features three CTA buttons for engagement
         ======================================== -->
    <section>
        <div class="relative overflow-visible">

            <!-- 
                Background Image - Semi-transparent with top gradient mask
                Performance: loading=eager because this image is close to the fold and
                visible shortly after scrolling. fetchpriority=high tells the
                browser to request it before other lazy images.
            -->
            <NuxtImg 
                src="https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/FrontPage_WhoWeAre.jpg"
                alt="Students giving a tour on the Lawn at UVA"
                width="1920"
                height="1080"
                loading="eager"
                fetchpriority="high"
                class="overflow-visible h-screen w-full object-cover mask-t-from-10% opacity-40"
            />

            <!-- Content Overlay - Centered on background -->
            <div class="scrollElement absolute top-1/2 left-1/2 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20 -translate-x-1/2 -translate-y-1/2 text-center">
                <!-- Section Header -->
                <h1 class="font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                    Who We Are
                </h1>

                <!-- Organization Description - Paragraph 1 -->
                <p class="scrollElement font-['Montserrat'] text-black sm:text-lg md:text-xl leading-relaxed mx-auto mt-10">
                    The Virginia Guide Service is an independent student-run volunteer tour-giving organization that provides the historical and admissions tours of the University of Virginia.
                    Virginia Guides is an organization that embodies a spirit of student self-governance and seeks to foster a sense of unity and cohesion among its members. 
                </p>
                <!-- Organization Description - Paragraph 2: Training and Free Tours -->
                <p class="scrollElement font-['Montserrat'] text-black sm:text-lg md:text-xl leading-relaxed mx-auto mt-2">
                    Our tour guides are students who are put through a rigorous training semester where they learn the ins and outs of UVA's history while practicing crucial tour-giving skills.
                    Trainees receive mentorship from experienced guides, professors, and historical organization leaders in the Charlottesville community. All tours are conducted free of charge.
                </p>

                <!-- Action Buttons Row - Three CTAs -->
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

    <!-- ========================================
         INSTAGRAM PLUG SECTION
         Social media call-to-action banner
         Encourages visitors to follow Instagram for updates
         Full-width banner with royal blue background
        ======================================== -->
    <section>
        <div class="relative w-full shadow-md bg-royal-blue py-6 px-4">
            <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-evenly gap-5">
                <!-- Description Text - Why to follow Instagram -->
                <div class="scrollElement font-['Montserrat'] text-white italic text-center justify-start text-sm md:text-base md:text-left max-w-xl">
                    Follow us on 
                    <a href="https://www.instagram.com/virginiaguides/" class="underline cursor-pointer">Instagram</a>
                     for updates on Virginia history, mission and development tours, scheduling, and inclement weather alerts. Stay connected and never miss important news or events!
                </div>
                <!-- Instagram Logo and Handle - Clickable link -->
                <div class="scrollElement font-['Montserrat'] text-white flex items-center justify-between gap-3 text-2xl md:text-3xl font-semibold">
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

    <!-- ========================================
         EXPLORE UVA HISTORY SECTION
         Imported component with historical tour content (components/ExploreUVAHistoryBlue.vue)
     ======================================== -->
    <ExploreUVAHistory blue />

    <!-- ========================================
        TOUR REVIEWS CAROUSEL SECTION
        Imported component with tour reviews (components/TourReviews.vue)
    ======================================== -->
    <TourReviews />

    <!-- ========================================
        OUR EVENTS SECTION
        Displays upcoming Virginia Guides events with image carousel
        
        Layout:
        - Left column: Section title and description (2/5 width on desktop)
        - Right column: Event cards in Swiper carousel (remaining width)
        
        Carousel Features:
        - Single slide view with auto-play (10s delay)
        - Pagination dots for navigation
        - Links to Instagram posts for each event
        - Images with text descriptions below
        ======================================== -->
    <section class="relative w-full">
        <!-- Semi-transparent Background Image Layer -->
        <div class="absolute inset-0">
            <div class="w-full h-full bg-[url('https://virginia-guides-website-images.s3.amazonaws.com/public/index-page/OurEvents_Background.jpg')] bg-cover bg-center opacity-50"></div>
        </div>

        <!-- Content Container (positioned above background) -->
        <div class="relative px-6 sm:px-8 lg:px-16 py-12 sm:py-16">
            <div class="flex flex-col md:flex-row items-start gap-10">
            
                <!-- ========================================
                    LEFT COLUMN: Section Header and Description
                    ======================================== -->
                <div class="w-full md:w-2/5 flex justify-start">
                    <div class="relative w-full">
                        <!-- Section Title -->
                        <p class="scrollElement font-['Playfair_Display'] font-bold text-black text-4xl sm:text-5xl leading-tight mb-6">
                            Our Events
                        </p>
                        <!-- Section Description -->
                        <p class="scrollElement font-['Montserrat'] font-semibold text-base sm:text-lg leading-relaxed text-black">
                            Join us in our work of telling a more honest, just, and complete telling of UVA's history.
                        </p>
                    </div>
                </div>

                <!-- ========================================
                    RIGHT COLUMN: Event Image Carousel
                    Swiper slider with event cards linking to Instagram posts
                    ======================================== -->
                <div v-if="isMounted">
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
                   <!-- Event Card 1: INCLEMENT WEATHER -->
                    <swiper-slide class="flex justify-center items-start">
                        <a href="https://www.instagram.com/p/DT6DdoiidTO/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==">
                            <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                                <img class="events-image mb-2 object-top" loading="lazy" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/weather-recruitment-update.jpg" alt="Weather Recruitment Update">
                                <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                                    Inclement Weather Recruitment Updates
                                </p>
                                <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                                    Despite the inclement weather, we're excited about what's ahead. Recruiting new guides, sharing history, and more. Check out
                                    our Instagram to see new dates for our recruitment events this season and stay warm!
                                </p>
                            </div>
                        </a>
                    </swiper-slide>

                    <!-- Event Card 2: Shine with Guides -->
                    <swiper-slide class="flex justify-center items-start">
                        <a href="https://www.instagram.com/p/DTqzVa_CfFw/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==">
                            <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                                <img class="events-image mb-2 object-top" loading="lazy" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/shine.jpg" alt="Shine with Guides Infographic">
                                <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                                    Shine with Guides: Spring 2026 Recruitment
                                </p>
                                <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                                    Join us on the of last week of January to hear from current guides about what we do and how you can become a guide!
                                    Learn more about the recruitment process, ask questions, meet current tour guides, and sign up for your trial tour.
                                    Info sessions are mandatory for potential guides to sign up for the next step in recruitment. Learn more about the process
                                    on our "Join Guides" page!
                                </p>
                            </div>
                        </a>
                    </swiper-slide>

                    <!-- Event Card 3: Raising the bar -->
                    <swiper-slide class="flex justify-center items-start">
                        <a href="https://www.instagram.com/p/DT-zAhwjRc8/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==">
                            <div class="relative max-w-2xl mx-auto p-4 pb-10 group cursor-pointer">
                                <img class="events-image mb-2 object-top" loading="lazy" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/RTB.jpg" alt="Raising the bar Infographic">
                                <p class="font-['Montserrat'] font-bold text-black text-2xl sm:text-3xl leading-tight mb-2">
                                    OAAAPA X VGS: Raising The Bar
                                </p>
                                <p class="font-['Montserrat'] font-medium text-base sm:text-lg leading-relaxed text-gray-900">
                                    Join OAAAPA and Guides on Wednesday, January 28th 5pm-7pm for the first RTB of the semester (if weather permits)! 
                                    It will be hosted at the PAC (first floor of Newcomb Hall) and food will be provided!
                                </p>
                            </div>
                        </a>
                    </swiper-slide>
                    </swiper>
                </div>
            </div>
        </div>
    </section>

    <!-- ========================================
        FOOTER COMPONENT
        Site-wide footer with links and information
     ======================================== -->
    <Footer />
</template>

<style>
    /* Enable smooth scrolling for anchor links */
    html {
        scroll-behavior: smooth;
        /* Offset scroll position for fixed headers */
        scroll-padding-top: 4rem;
    }
    /* === Scroll Reveal Animation (For Entire Page) === */
    /* Elements start hidden and slightly shifted down */
    .scrollElement {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    /* Applied when element enters viewport */
    .scrollElement.show {
        opacity: 1;
        transform: translateY(0);
    }
    /* === Our Events Section (Swiper) === */
    .events-swiper{
        width: 100%;
    }
    /* Pagination container inside events swiper */
    .events-swiper .swiper-pagination {
        position: absolute;
    }
    /* Pagination dots */
    .events-swiper .swiper-pagination-bullet {
        height: 10px;
        width: 10px;
        background: black;
    }
    /* Event images */
    .events-image {
        width: 100%;
        height: 450px;
        object-fit: cover;     
    }
    /* === Link Cards Swiper === */
    .mySwiper{
        width: 100%;
        padding: 40px 40px;
    }
    /* Pagination bullets */
    .swiper-pagination {
        position: absolute;
    }
    .swiper-pagination-bullet {
        height: 7px;
        width: 26px;
        border-radius: 25px;
        background: #A86645;
    }
    /* Swiper navigation arrows */
    .swiper-button-next,
    .swiper-button-prev {
        color: #A86645;
    }
</style>

<script setup>
    /* Swiper Imports */
    import { Swiper, SwiperSlide } from "swiper/vue";
    import "swiper/css";
    import "swiper/css/pagination";
    import "swiper/css/navigation";
    import { Pagination, Navigation, Autoplay } from "swiper/modules";

    /* Vue Imports */
    import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';

    /* Components */
    import Footer from '~/components/Footer.vue';
    import ExploreUVAHistory from '~/components/ExploreUVAHistory.vue';
    import TourReviews from '~/components/TourReviews.vue'

    /* Page Metadata
        Performance Choices:
    1. Preload the hero background image so the browser fetches it
        during the <head> parse rather than waiting to discover it
        inside CSS — this directly improves Largest Contentful Paint (LCP).
    2. preconnect to fonts.googleapis.com opens the TCP/TLS handshake
        early so font CSS downloads faster.
    3. crossorigin preconnect to fonts.gstatic.com (the actual font file
        CDN) shaves one round-trip off each font file request.
    */
    useHead({
        title: 'Tours of the University of Virginia | Virginia Guides Service',
        link: [
            // PERF 1: Preload hero background image (biggest LCP improvement)
            {
                rel: 'preload',
                as: 'image',
                href: 'https://virginia-guides-website-images.s3.amazonaws.com/public/Header_FrontPageNew.jpg',
                fetchpriority: 'high',
            },
            // PERF 2: Preconnect to Google Fonts CSS endpoint
            {
                rel: 'preconnect',
                href: 'https://fonts.googleapis.com',
            },
            // PERF 3: Preconnect to Google Fonts file CDN (needs crossorigin for CORS fonts)
            {
                rel: 'preconnect',
                href: 'https://fonts.gstatic.com',
                crossorigin: 'anonymous',
            },
        ],
    })

    /* Swiper features enabled for this page */
    const modules = [Pagination, Navigation, Autoplay]

    const isMounted = ref(false)
    let observerElements = null

    /* Scroll Effect / Reveal (IntersectionObserver for .scrollElement) */
    onMounted(() => {
        isMounted.value = true
        // Prevent errors during server-side rendering
        if (typeof window === "undefined") return

            // Observe elements as they enter the viewport
            const observerElements = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    // Show animation when visible
                    entry.target.classList.add("show")
                } else {
                    // Hide when out of view
                    entry.target.classList.remove("show")
                }
            })

            const attachObserver = () => {
                document.querySelectorAll(".scrollElement").forEach((el) => {
                observerElements.observe(el)
                })
            }

            attachObserver()

            isMounted.value = true
            nextTick(() => attachObserver())
            
        })

        // Attach observer to all scroll animation elements
        const scrollElements = document.querySelectorAll(".scrollElement")
        scrollElements.forEach((el) => observerElements.observe(el))
    })

    /* Scroll Icon / Text Switch for Header Section  */
    // References to DOM elements
    const topElement = ref(null)
    const iconWrap = ref(null)
    const textWrap = ref(null)

    // Tracks whether the user is at the top of the page
    const isAtTop = ref(true) // true = show arrow icon

    let observerTopElement = null

    onMounted(() => {
        // Prevent SSR issues
        if (typeof window === "undefined") return

        // Observer options
        const options = {
            root: null,
            rootMargin: '0px',
            threshold: 0
        }

        // Observe the top invisible element
        observerTopElement = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                isAtTop.value = entry.isIntersecting
            })
        }, options)

        if (topElement.value) observerTopElement.observe(topElement.value)

        // Scroll icon and text elements
        const scrollIcon = document.getElementById("scroll-icon")
        const scrollText = document.getElementById("scroll-text")

        // Toggle visibility based on scroll position
        function handleScroll() {
            if (window.scrollY > 20) {
                if (scrollIcon) scrollIcon.style.opacity = "0"
                if (scrollText) scrollText.style.opacity = "1"
            } else {
                if (scrollIcon) scrollIcon.style.opacity = "1"
                if (scrollText) scrollText.style.opacity = "0"
            }
        }

        // Initial state check
        handleScroll()
        window.addEventListener("scroll", handleScroll)

        // Cleanup observers and listeners
        onBeforeUnmount(() => {
            window.removeEventListener("scroll", handleScroll)
            if (observerTopElement && topElement.value) observerTopElement.unobserve(topElement.value)
        })
    })
</script>
