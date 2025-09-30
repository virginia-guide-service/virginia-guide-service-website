<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_YourVisit.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[90vh]">
        <!-- Centered Text -->
        <div class="absolute top-1/2 xl:top-[45%] left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] text-center xl:text-right italic whitespace-nowrap text-[clamp(3rem,9.5vw,5.5rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                YOUR VISIT
            </h1>
            <p class="font-['Roboto'] text-center xl:text-right text-base sm:text-md md:text-lg font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                DIRECTIONS & FREQUENTLY ASKED QUESTIONS
            </p>
        </div>
    </header>

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative z-20 -mt-14 px-4">
        <!-- Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-dark-burgandy -z-10"></div>

        <div class="shadow-lg rounded-xl p-6 max-w-4xl mx-auto text-center bg-white border-6 border-dark-burgandy">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4">
                <a href="#times-and-registration" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Times & Registration
                </a>
                <a href="#location-and-parking" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Location & Parking
                </a>
                <a href="#frequently-asked-questions" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Frequently Asked Questions
                </a>
            </div>
        </div>
    </section>

    <!--Banner-->
    <section class="pt-5 sm:pt-10 md:pt-8">
        <div class="w-full bg-gray-300 textpcenter py-6 px-4 flex justify-center items-center">
            <p class="font-['Roboto'] text-royal-blue italic text-center font-medium text-base sm:text-lg md:text-md">
                Because Virginia Guides is student-run, we do not provide tours during exam periods, reading days, or student breaks, which are specified 
                <a href="https://registrar.virginia.edu/calendar/academic">
                    <span class="underline">
                        here.
                    </span>
                </a>
            </p>
        </div>
    </section>

    <!-- Historical Tour Info Section -->
    <section class="p-4 sm:p-8 md:p-6 mb-3 sm:mb-5 md:mb-10 lg:mb-35">
        <div class="flex flex-col lg:flex-row justify-center items-start max-w-7xl mx-auto gap-10">

        <!-- Right: Image with Half Overlay -->
        <div class="w-full lg:w-1/2 flex justify-center items-center relative">
            <!-- Base Image -->
            <img 
                src="/your-visit-page/YourVisit_Image.jpg" 
                alt="Historical Tour Image" 
                class="w-full max-w-lg h-auto rounded-md shadow-md"
            />

            <!-- Overlay Image (half size, shifted) -->
            <img 
                src="/your-visit-page/YourVisit_Image.jpg" 
                alt="Overlay Image" 
                class="hidden lg:block absolute w-full max-w-lg top-35 rounded-md"
            />
        </div>

        <!-- Left: Text -->
        <div class="w-full lg:w-1/2 px-5 lg:px-0">
            <p class="font-['Montserrat'] text-center lg:text-left font-medium text-dark-green text-4xl sm:text-5xl leading-tight mb-6">
            HISTORICAL TOURS
            </p>
            <p class="font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                From its founding to the Civil War. From the Civil Rights Movement to the present day, 
                student-led history tours trace over 200 years of change, resistance, and community. 
                Tours navigate the outdoor grounds of the UNESCO World Heritage Site and are written by 
                students after a semester of intensive training, research, and critical reflection.
                <br /><br />
                <span class="font-bold">
                    All tours are free of charge,
                </span> regardless of group size. Donations to support work are welcome.
            </p>
            <br /><br />
            <div class="flex justify-center items-center px-4">
                <a href="/about-tours">
                    <button class="border-1 text-white rounded-full py-3 px-10 cursor-pointer font-semibold shadow-md hover:shadow-large bg-dark-green hover:bg-green-700 transition-all duration-300 ease-in-out">
                        Learn More
                    </button>
                </a>
            </div>
        </div>

        </div>
    </section>

    <!-- Tour Schedule -->
    <section id="times-and-registration" class="relative bg-neutral-100 pt-5">
        <div class="flex flex-col lg:flex-row items-start max-w-7xl mx-auto gap-10 p-8 sm:p-6 md:p-4">
            <!-- Left: Tour Schedule Text -->
            <div class="w-full lg:w-1/2 flex flex-col items-center lg:items-start">
                <p class="font-['Montserrat'] text-left font-medium text-UVA-orange text-4xl sm:text-5xl leading-tight mb-6">
                    TOUR SCHEDULE
                </p>
                <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-3xl lg:max-w-xl px-4 lg:pb-5">
                    <li>
                    Standard Tours will leave at 11:00 AM from the Lawn-side of the Rotunda Steps every Friday, Saturday, and Sunday 
                    <a class="underline" href="http://www.virginia.edu/registrar/calendar.html">
                        during the academic school year.
                    </a>
                    </li>
                    <li>
                    Exceptions include 
                    <a class="underline" href="https://virginiasports.com/sports/football/schedule/">
                        home football game days
                    </a> and 
                    <a class="underline" href="https://registrar.virginia.edu/calendar/academic">
                        when classes are not in session.
                    </a>
                    </li>
                    <li>
                    Tours last around 1 Hour.
                    </li>
                </ul>
            </div>

            <!-- Right: Registration Form (overlapping the section) -->
            <div class="w-full lg:w-1/2 relative">
                <div class="relative lg:absolute lg:-bottom-190 z-20 w-full">
                    <div class="flex flex-col shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] rounded-xl p-6 bg-white">
                        <h1 class="font=['Montserrat'] font-medium text-3xl text-royal-blue mb-4">
                            Register Here for a Historical Tour
                        </h1>
                        <form class="flex flex-col">
                            <label for="fname" class="font-[Montserrat] font-light text-royal-blue">First Name</label>
                            <input type="text" id="fname" name="fname" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                            <label for="lname" class="font-[Montserrat] font-light text-royal-blue">Last Name</label>
                            <input type="text" id="lname" name="lname" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                            <label for="email" class="font-[Montserrat] font-light text-royal-blue">Email</label>
                            <input type="email" id="email" name="email" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                            <label for="number" class="font-[Montserrat] font-light text-royal-blue">Phone Number</label>
                            <input type="tel" id="number" name="number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                            <div class="flex flex-col lg:flex-row justify-between lg:gap-4">
                                <div class="flex flex-col">
                                    <label for="date" class="font-[Montserrat] font-light text-royal-blue">Date</label>
                                    <input type="date" id="date" name="date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                </div>
                                <div class="flex flex-col">
                                    <label for="guestNum" class="font-[Montserrat] font-light text-royal-blue">Guest(s)</label>
                                    <input type="number" id="guestNum" name="guestNum" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                </div>
                            </div>

                            <label for="guestNum" class="font-[Montserrat] font-light text-royal-blue">How many minors are in your group?</label>
                            <input type="number" id="guestNum" name="guestNum" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />


                            <label for="tour" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                            <input type="text" id="tour" name="tour" value="Standard Historical Tour" readonly class="font-[Montserrat] text-royal-blue border border-gray-300 bg-gray-100 cursor-not-allowed rounded-lg px-4 py-2 focus:outline-none mb-5"/>


                            <label for="notes" class="font-[Montserrat] font-light text-royal-blue">Notes for the Tour</label>
                            <textarea id="notes" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4"></textarea>

                            <button type="submit" class="font-[Montserrat] bg-royal-blue text-white font-semibold rounded-lg px-4 py-2 hover:bg-blue-900 transition-all duration-300 ease-in-out cursor-pointer">
                                Register
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Banner -->
        <div class="bg-royal-blue w-full p-8 relative z-10">
            <div class="w-full lg:w-1/2 flex flex-col justify-center items-center">
                <p class="font-['Montserrat'] font-light text-base sm:text-lg leading-relaxed text-white">
                    <span class="font-semibold">Registration for Standard History Tours are not required but encouraged to receive possible updates on your tour. </span>
                    Standard Historical tours are public for anyone to join and occur regularly throughout the school year.
                </p>
                <a href="/contact-us">
                    <button class="rounded-full border-2 border-white text-white font-semibold text-base sm:text-lg px-6 py-2 mt-5 cursor-pointer hover:bg-gray-200 hover:text-black hover:border-gray-200 transition-all duration-300 ease-in-out">
                        Contact Us
                    </button>
                </a>
            </div>
        </div>
    </section>

    <!-- Location and Parking -->
    <section id="location-and-parking" class="bg-neutral-100">
        <div class="flex flex-col lg:flex-row justify-center gap-10 p-10 sm:p-8 md:p-6 w-full lg:w-1/2">
            <!-- Left: Tour Schedule Text -->
            <div class="flex flex-col items-center lg:items-start">
                <p class="font-['Montserrat'] text-left font-medium text-UVA-orange text-4xl sm:text-5xl leading-tight mb-6">
                    LOCATION & PARKING
                </p>
                <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-3xl lg:max-w-xl px-4">
                    <li>
                        We recommend 
                        <span class="font-medium">
                            Central Grounds Garage 
                        </span> 
                        <span class="italic">
                            (fees will apply)
                        </span> at 
                        <a href="https://maps.app.goo.gl/7nHgafiEj1LqNrcN8" class="underline text-blue-500">
                            400 Emmet Street, Charlottesville, VA, 22903
                        </a>
                        for single family cars.
                    </li>
                    <li>
                        Access to the Lawn and Rotunda from the parking garage is also wheelchair accessible. Please see here for more information on accessibility. 
                    </li>
                    <li>
                        Tours will meet at the Front Rotunda Steps & Entrance, facing the Lawn.
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!--Switch to leaflet-->
    <!-- Map Section -->
    <section class="w-full flex justify-center px-10 p-5 lg:p-5 bg-neutral-100">
        <div class="w-full max-w-5xl aspect-video">

            <!-- John's Map -->
            <iframe 
                src="https://www.google.com/maps/d/embed?mid=16Uf_oN9AUEKhU3pVgavoqg6AHNG1o-o&ehbc=2E312F&noprof=1" 
                class="w-full h-full border-0"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade">
            </iframe> 

            <!--General Map-->
            <!-- <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5207.173557834788!2d-78.50912734315418!3d38.03665224800225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b3864f8f4cfb4b%3A0x13fd676a940c94c6!2sCentral%20Grounds%20Garage!5e0!3m2!1sen!2sus!4v1757214405792!5m2!1sen!2sus"
                class="w-full h-full border-0"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade">
            </iframe> -->
        </div>
    </section>

    <!-- What is the Tour About? Section -->
    <section id="frequently-asked-questions" class="bg-white py-16 px-6 sm:px-12 lg:px-20">
        <div class="max-w-5xl mx-auto">
            <!-- Title -->
            <h2 class="font-['Montserrat'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-semibold text-center mb-12">
                WHAT IS THE TOUR ABOUT?
            </h2>

            <!-- FAQ Accordion -->
            <div class="space-y-6 text-dark-green font-['Montserrat']">
                <!-- FAQ Item -->
                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                        <span>How much does a tour cost per guest?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        <span class="font-semibold">
                            Tours are free for all group sizes
                        </span>; donations are welcome. For single-family cars, we recommend parking at the Central Grounds Garage (
                        <a href="https://maps.app.goo.gl/7nHgafiEj1LqNrcN8" class="underline text-blue-500 m-0 p-0">
                            400 Emmet Street, Charlottesville, VA, 22903
                        </a>; UVA parking fees apply). Parking fees can be found 
                        <a href="https://parking.virginia.edu/visitor-parking" class="underline text-blue-500">
                            here.
                        </a>
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                        <span>How long should I plan for my tour?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Tours typically last around 1-1.5 hours. Please meet at the tour-start location around 5-10 minutes before your tour.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                        <span>Can I bring water to the site?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Water is encouraged, especially on warm days, as most of the tour is outdoors with some shaded areas. Food is not allowed inside historic buildings, but the Lawn and “The Corner” nearby are great places to eat before or after your visit.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                        <span>Is photography allowed?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Personal photography of the site is welcome. To respect privacy and intellectual property, recording of tours, tour content, or identifiable individuals (including students) is not permitted without prior written consent.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                        <span>Do I need to register for large groups?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Yes. For groups over 10 visitors, please complete the tour registration form so we can prepare for your needs. School groups should see the 
                        <a href="/for-educators">
                            "For Educators"
                        </a> page for more information and opportunities.
                    </p>
                    <div class="flex flex-col sm:flex-row flex-wrap gap-3 mt-4">
                        <a href="#times-and-registration" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg transition-all duration-300 ease-in-out">
                            Registration
                            </button>
                        </a>
                        <a href="/about-tours#specialty-tours" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg transition-all duration-300 ease-in-out">
                            Specialty Tours
                            </button>
                        </a>
                        <a href="/for-educators" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg transition-all duration-300 ease-in-out">
                            For Educators
                            </button>
                        </a>
                    </div>

                </details>
            </div>
        </div>
    </section>

    <!-- Accessibility Section -->
    <section id="frequently-asked-questions" class="bg-royal-blue py-16 px-6 sm:px-12 lg:px-20">
    <div class="max-w-5xl mx-auto">
        <!-- Title -->
        <h2 class="font-['Montserrat'] text-white text-3xl sm:text-4xl md:text-5xl font-semibold text-center mb-12">
            ACCESSIBILITY
        </h2>

        <!-- FAQ Accordion -->
        <div class="space-y-6 text-[#DC8051] font-['Montserrat']">
            <!-- FAQ Item -->
            <details class="group border-b pb-4">
                <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                    <span class="text-[#DC8051]">Is the Academical Village wheelchair-accessible from the parking garage?</span>
                    <span class="text-[#DC8051] group-open:rotate-45 transition-transform">+</span>
                </summary>
                <ul class="list-disc mt-3 ml-10 text-base sm:text-lg text-white leading-relaxed">
                    <li>
                        Yes. The Lawn and path from Central Grounds Garage is accessible with ramps. If you have any accessibility concerns, questions, or other information that would help us prepare for your visit, please contact us in advance.
                    </li>
                    <li>
                        Tours are mostly outdoors and weather-dependent; we use shaded areas when possible, but summer heat can be significant.
                    </li>
                </ul>
            </details>

            <details class="group border-b pb-4">
                <summary class="cursor-pointer text-xl sm:text-2xl font-medium flex justify-between items-center">
                    <span class="text-[#DC8051]">What accommodations are available for deaf or hard-of-hearing visitors?</span>
                    <span class="text-[#DC8051] group-open:rotate-45 transition-transform">+</span>
                </summary>
                <p class="mt-3 text-base sm:text-lg text-white leading-relaxed">
                    Our guided tours are not currently interpreted for deaf or hard-of-hearing visitors.
                </p>
            </details>
        </div>
    </div>
    </section>

    <!-- Explore UVA History Section -->
    <section class="bg-white py-16 sm:py-20 md:py-24">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">

            <!-- Header -->
            <h1 class="font-['Montserrat'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                Explore UVA History
            </h1>

            <!-- Description -->
            <p class="font-['Montserrat'] text-black text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                which focus on a specific aspect of UVA's extensive 200 year history.
            </p>

            <!-- Button -->
            <a href="/about-tours">
                <button class="inline-flex items-center space-x-3 rounded-full border text-black font-['Montserrat'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-black hover:bg-neutral-300 transition-all duration-300 ease-in-out cursor-pointer">
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
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                    <!--Same 5 slides (doubled)-->
                    <a href="/about-tours/#history-of-women-at-uva">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" alt="">
                            <p class="carousel-text self-start text-black font-normal font-['Roboto']">Children's Tour</p>
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
                            The Virginia Guides continues 75 years of guiding visitors through UVA. The Guides Service is a student-run organization independent of the University of Virginia, carrying forward tradition while bringing a more complete light to the past.
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