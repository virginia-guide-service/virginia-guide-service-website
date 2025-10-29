<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_YourVisit.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[90vh]">
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
    <section class="relative z-20 -mt-10 px-4">
        <!-- Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-royal-blue -z-10 hidden sm:block"></div>

        <div class="shadow-lg p-6 max-w-3xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4 text-white">
                <a href="#times-and-registration" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Times & Registration
                </a>
                <a href="#location-and-parking" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Location & Parking
                </a>
                <a href="#frequently-asked-questions" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Frequently Asked Questions
                </a>
            </div>
        </div>
    </section>

    <!--Banner-->
    <section class="pt-5 sm:pt-10 md:pt-8">
        <div class="w-full bg-gray-300 textpcenter py-6 px-4 sm:px-6 lg:px-8 flex justify-center items-center">
            <p class="scrollElement font-['Roboto'] text-royal-blue italic text-center font-medium text-base sm:text-lg md:text-md">
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
        <div class="scrollElement w-full lg:w-1/2 flex justify-center items-center relative">
            <!-- Base Image -->
            <img 
                src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/your-visit-page/YourVisit_Image.jpg" 
                alt="Historical Tour Image" 
                class="w-full max-w-lg h-auto rounded-md shadow-md"
                loading="lazy"
            />

            <!-- Overlay Image (half size, shifted) -->
            <img 
                src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/your-visit-page/YourVisit_Image.jpg" 
                alt="Overlay Image" 
                class="hidden lg:block absolute w-full max-w-lg top-35 rounded-md"
                loading="lazy"
            />
        </div>

        <!-- Left: Text -->
        <div class="w-full lg:w-1/2 px-5 lg:px-0">
            <p class="scrollElement font-['Montserrat'] text-center lg:text-left font-medium text-dark-green text-4xl sm:text-5xl leading-tight mb-4">
            HISTORICAL TOURS
            </p>
            <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900">
                From its founding to the Civil War. From the Civil Rights Movement to the present day, 
                student-led history tours trace over 200 years of change, resistance, and community. 
                Tours navigate the outdoor grounds of the UNESCO World Heritage Site and are written by 
                students after a semester of intensive training, research, and critical reflection.
                <br /><br />
                <span class="scrollElement font-bold">
                    All tours are free of charge,
                </span> regardless of group size. Donations to support work are welcome.
                <br /><br />
                <span class="scrollElement font-bold italic">
                    The University of Virginia expects parents or guardians to provide supervision over minors on University property. 
                    Parents or guardians should not leave minors unsupervised on University property.
                </span>
            </p>
            <br /><br />
            <div class="scrollElement flex justify-center items-center px-4">
                <a href="/about-tours">
                    <button class="border-1 text-white rounded-full py-3 px-10 cursor-pointer font-semibold shadow-md hover:shadow-large bg-dark-green hover:bg-green-700 hover:scale-105 transition-all duration-300 ease-in-out">
                        Learn More
                    </button>
                </a>
            </div>
        </div>

        </div>
    </section>

    <!-- Tour Schedule + Banner + Registration Form -->
    <section id="times-and-registration" class="relative bg-neutral-100 pt-5">
        <div class="flex flex-col lg:flex-row items-start max-w-7xl mx-auto gap-10 px-4 sm:px-6 lg:px-8 py-6">
            <!-- Left: Tour Schedule Text -->
            <div class="w-full lg:w-1/2 flex flex-col items-center lg:items-start">
                <p class="scrollElement font-['Montserrat'] text-left font-medium text-UVA-orange text-4xl sm:text-5xl leading-tight mb-6">
                    TOUR SCHEDULE
                </p>
                <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-3xl lg:max-w-xl px-4 lg:pb-5">
                    <li class="scrollElement">
                        Standard Tours will leave at 11:00 AM from the Lawn-side of the Rotunda Steps every Friday, Saturday, and Sunday 
                        <a class="underline" href="http://www.virginia.edu/registrar/calendar.html">
                            during the academic school year.
                        </a>
                    </li>
                    <li class="scrollElement">
                        Exceptions to our schedule is
                        <a class="underline" href="https://registrar.virginia.edu/calendar/academic">
                            when classes are not in session.
                        </a>
                    </li>
                    <li class="scrollElement">
                        Tours last around 1 Hour.
                    </li>
                </ul>
            </div>
        </div>

        <!-- Banner + Registraton Form -->
        <div class="bg-royal-blue w-full relative z-10 py-6">
            <div class="flex flex-col lg:flex-row items-start px-4 sm:px-6 md:px-8">
                <!--Left: Banner Text-->
                <div class="w-full lg:w-1/2 flex flex-col justify-center items-center max-w-7xl mx-auto">
                    <p class="scrollElement font-['Montserrat'] font-light text-base sm:text-lg leading-relaxed text-white">
                        <span class="font-semibold">Registration for Standard History Tours are encouraged to receive possible updates on your tour. </span>
                        <br/>
                        <span class="text-gray-400">Standard Historical tours are public for anyone to join and occur regularly throughout the school year. You can request specialty tours <a href="/request-specialty-tours" class="underline"> here.</a></span>
                    </p>
                    <a href="/contact-us" class="scrollElement">
                        <button class="rounded-full border-2 border-white text-white font-semibold text-base px-6 py-2 mt-3 cursor-pointer hover:bg-gray-200 hover:text-black hover:border-gray-200 hover:scale-105 transition-all duration-300 ease-in-out">
                            Contact Us
                        </button>
                    </a>
                </div>

                <!-- Right: Registration Form (overlapping the section) -->
                <div class="w-full lg:w-1/2 relative pt-5 lg:pt-0">
                    <div class="relative lg:absolute lg:-bottom-110 z-20 w-full">
                        <div class="flex flex-col shadow-[0px_2px_16px_0px_rgba(14,30,37,0.32)] rounded-xl p-6 bg-white">
                            <h1 class="font=['Montserrat'] font-medium text-3xl text-royal-blue mb-4">
                                Register Here for a Historical Tour
                            </h1>
                            <form @submit="submitForm" class="flex flex-col">
                                <label for="fname" class="font-[Montserrat] font-light text-royal-blue">First Name</label>
                                <input v-if="!fieldErrors.first_name" type="text" id="fname" name="fname" v-model="form.first_name" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                <input v-if="fieldErrors.first_name" type="text" id="fname" name="fname" v-model="form.first_name" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                <p v-if="fieldErrors.first_name" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.first_name[0] }}
                                </p>

                                <label for="lname" class="font-[Montserrat] font-light text-royal-blue">Last Name</label>
                                <input v-if="!fieldErrors.last_name" type="text" id="lname" name="lname" v-model="form.last_name" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                <input v-if="fieldErrors.last_name" type="text" id="lname" name="lname" v-model="form.last_name" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                <p v-if="fieldErrors.last_name" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.last_name[0] }}
                                </p>

                                <label for="email" class="font-[Montserrat] font-light text-royal-blue">Email</label>
                                <input v-if="!fieldErrors.email" ype="email" id="email" name="email" v-model="form.email" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                <input v-if="fieldErrors.email" ype="email" id="email" name="email" v-model="form.email" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                <p v-if="fieldErrors.email" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.email[0] }}
                                </p>

                                <label for="number" class="font-[Montserrat] font-light text-royal-blue">Phone Number</label>
                                <input v-if="!fieldErrors.phone_number" type="tel" id="number" name="number" v-model="form.phone_number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                <input v-if="fieldErrors.phone_number" type="tel" id="number" name="number" v-model="form.phone_number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                <p v-if="fieldErrors.phone_number" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.phone_number[0] }}
                                </p>

                                <div class="flex flex-col lg:flex-row justify-between lg:gap-4">
                                    <div class="flex flex-col">
                                        <label for="date" class="font-[Montserrat] font-light text-royal-blue">Date of Tour</label>
                                        <input v-if="!fieldErrors.date" type="date" id="date" name="date" v-model="form.date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                        <input v-if="fieldErrors.date" type="date" id="date" name="date" v-model="form.date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                        <p v-if="fieldErrors.date" class="text-red-500 text-sm p-0 mb-2">
                                            {{ fieldErrors.date[0] }}
                                        </p>
                                    </div>
                                    <div class="flex flex-col">
                                        <label for="guestNum" class="font-[Montserrat] font-light text-royal-blue">Guest(s)</label>
                                        <input v-if="!fieldErrors.guests" type="number" id="guestNum" name="guestNum" v-model="form.guests" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                        <input v-if="fieldErrors.guests" type="number" id="guestNum" name="guestNum" v-model="form.guests" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                        <p v-if="fieldErrors.guests" class="text-red-500 text-sm p-0 mb-2">
                                            {{ fieldErrors.guests[0] }}
                                        </p>
                                    </div>
                                </div>

                                <label for="minorNum" class="font-[Montserrat] font-light text-royal-blue">How many minors are in your group?</label>
                                <input v-if="!fieldErrors.minors" type="number" id="minorNum" name="minorNum" v-model="form.minors" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                <input v-if="fieldErrors.minors" type="number" id="minorNum" name="minorNum" v-model="form.minors" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                                <p v-if="fieldErrors.minors" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.minors[0] }}
                                </p>

                                <label for="tour" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                                <input type="text" id="tour" name="tour" value="Standard Historical Tour" readonly class="font-[Montserrat] text-royal-blue border border-gray-300 bg-gray-100 cursor-not-allowed rounded-lg px-4 py-2 focus:outline-none mb-5"/>


                                <label for="notes" class="font-[Montserrat] font-light text-royal-blue">Notes for the Tour</label>
                                <textarea id="notes" v-model="form.notes" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4"></textarea>

                                <button type="submit" class="font-[Montserrat] bg-royal-blue text-white font-semibold rounded-lg px-4 py-2 hover:bg-blue-900 transition-all duration-300 ease-in-out cursor-pointer">
                                    Register
                                </button>

                                <!-- Success Toast -->
                                <div v-if="success" class="fixed inset-0 flex items-center justify-center z-50 pointer-events-none">
                                    <div class="font-[Montserrat] bg-green-600 text-white px-6 py-4 rounded-md shadow-lg pointer-events-auto">
                                        Thank you! Your registration has been submitted.
                                    </div>
                                </div>

                                <!-- Error Toast -->
                                <div v-if="errorMsg" class="fixed inset-0 flex items-center justify-center z-50 pointer-events-none">
                                    <div class="font-[Montserrat] bg-red-600 text-white px-6 py-4 rounded-md shadow-lg pointer-events-auto">
                                        {{ errorMsg }}
                                    </div>
                                </div>

                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Location and Parking -->
    <section id="location-and-parking" class="bg-neutral-100">
        <div class="flex flex-col lg:flex-row items-start max-w-7xl mx-auto gap-10 px-4 sm:px-6 lg:px-8 pt-12 pb-6">
            <!-- Left: Parking Text -->
            <div class="w-full lg:w-1/2 flex flex-col items-center lg:items-start">
                <!--Header-->
                <p class="scrollElement font-['Montserrat'] text-left font-medium text-UVA-orange text-4xl sm:text-5xl leading-tight mb-6">
                    LOCATION & PARKING
                </p>
                <!--Bullet Points-->
                <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-3xl lg:max-w-xl px-4">
                    <li class="scrollElement">
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
                    <li class="scrollElement">
                        Access to the Lawn and Rotunda from the parking garage is also wheelchair accessible. Please see here for more information on accessibility. 
                    </li>
                    <li class="scrollElement">
                        Tours will meet at the Front Rotunda Steps & Entrance, facing the Lawn.
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Map Section -->
    <section class="w-full flex justify-center px-10 pb-12 bg-neutral-100">
        <div class="scrollElement w-full max-w-6xl mx-auto h-64 sm:h-80 md:h-96 lg:h-[600px]">
            <iframe
                src="https://www.google.com/maps/d/embed?mid=16Uf_oN9AUEKhU3pVgavoqg6AHNG1o-o&ehbc=2E312F&noprof=1"
                class="w-full h-full border-0"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
            ></iframe>

            <!--General Map-->
            <!-- <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5207.173557834788!2d-78.50912734315418!3d38.03665224800225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b3864f8f4cfb4b%3A0x13fd676a940c94c6!2sCentral%20Grounds%20Garage!5e0!3m2!1sen!2sus!4v1757214405792!5m2!1sen!2sus"
                class="w-full h-full border-0"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade">
            </iframe> -->
        </div>
    </section>

    <!-- FAQ Section -->
    <section id="frequently-asked-questions" class="bg-white py-16 px-6 sm:px-12 lg:px-20">
        <div class="max-w-5xl mx-auto">
            <!-- Title -->
            <h2 class="scrollElement uppercase font-['Montserrat'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-semibold text-center mb-12">
                Frequently Asked Questions
            </h2>

            <!-- FAQ Accordion -->
            <div class="scrollElement space-y-6 text-dark-green font-['Montserrat']">
                <!-- FAQ Item -->

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">What is the tour about?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        UVA's student-led tours trace over 200 years of history, from its founding through decades of change, resistance, 
                        and community. Drawing on in-depth student research, they include often-overlooked stories of enslaved 
                        laborers and activists who helped shape the university. Each guide crafts their own tour after an intensive semester 
                        of research and training, resulting in the same histories being told threaded through an evolving set of different perspectives.
                    </p>
                    <div class="flex flex-col sm:flex-row flex-wrap gap-3 mt-4">
                        <a href="/about-tours" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg hover:scale-105 transition-all duration-300 ease-in-out">
                                Learn More
                            </button>
                        </a>
                    </div>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">How much does a tour cost per guest?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
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
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">How long should I plan for my tour?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Tours typically last around 1-1.5 hours. Please meet at the tour-start location around 5-10 minutes before your tour.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">Can I bring water to the site?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Water is encouraged, especially on warm days, as most of the tour is outdoors with some shaded areas. Food is not allowed inside historic buildings, but the Lawn and “The Corner” nearby are great places to eat before or after your visit.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">Is photography allowed?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Personal photography of the site is welcome. To respect privacy and intellectual property, recording of tours, tour content, or identifiable individuals (including students) is not permitted without prior written consent.
                    </p>
                </details>

                <details class="group border-b pb-4">
                    <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                        <span class="pl-5 xl:pl-0">Do I need to register for large groups?</span>
                        <span class="text-UVA-orange group-open:rotate-45 transition-transform hidden xl:block">+</span>
                    </summary>
                    <p class="mt-3 text-base sm:text-lg text-gray-700 leading-relaxed">
                        Yes, please complete the tour registration form so we can prepare for your needs. School groups should see 
                        <a href="/for-educators" class="italic">
                        For Educators
                        </a>
                         for more information and opportunities.
                    </p>
                    <div class="flex flex-col sm:flex-row flex-wrap gap-3 mt-4">
                        <a href="#times-and-registration" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg hover:scale-105 transition-all duration-300 ease-in-out">
                            Registration
                            </button>
                        </a>
                        <a href="/request-specialty-tours" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg hover:scale-105 transition-all duration-300 ease-in-out">
                            Specialty Tour Registration
                            </button>
                        </a>
                        <a href="/for-educators" class="w-full sm:w-auto">
                            <button class="w-full sm:w-auto px-6 py-2 sm:px-8 sm:py-3 rounded-full bg-dark-green text-white font-semibold text-sm sm:text-base shadow-md hover:bg-green-700 hover:shadow-lg hover:scale-105 transition-all duration-300 ease-in-out">
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
        <h2 class="scrollElement font-['Montserrat'] text-white text-3xl sm:text-4xl md:text-5xl font-semibold text-center mb-12">
            ACCESSIBILITY
        </h2>

        <!-- FAQ Accordion -->
        <div class="scrollElement space-y-6 text-[#DC8051] font-['Montserrat']">
            <!-- FAQ Item -->
            <details class="group border-b pb-4">
                <summary class="cursor-pointer text-xl sm:text-2xl font-medium xl:flex xl:justify-between xl:items-start">
                    <span class="text-[#DC8051] pl-5 xl:pl-0">Is the Academical Village wheelchair-accessible from the parking garage?</span>
                    <span class="text-[#DC8051] group-open:rotate-45 transition-transform hidden xl:block">+</span>
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
                <summary class="cursor-pointer text-xl sm:text-2xl xl:flex xl:justify-between xl:items-start">
                    <span class="text-[#DC8051] pl-5 xl:pl-0">What accommodations are available for deaf or hard-of-hearing visitors?</span>
                    <span class="text-[#DC8051] group-open:rotate-45 transition-transform hidden xl:block">+</span>
                </summary>
                <p class="mt-3 text-base sm:text-lg text-white leading-relaxed">
                    Our guided tours are not currently interpreted for deaf or hard-of-hearing visitors.
                </p>
            </details>
        </div>
    </div>
    </section>

    <!-- Explore UVA History Section -->
    <ExploreUVAHistoryWhite />

    <!--Footer Section-->
    <Footer />


</template>

<script setup lang="ts">
    import { onMounted } from "vue"
    import { ref } from 'vue'
    import Footer from '~/components/Footer.vue'
    import ExploreUVAHistoryWhite from '~/components/ExploreUVAHistoryWhite.vue';

    useHead({
        title: 'Take a Tour & Plan Your Visit | Virginia Guides Service',
    })

    const form = ref({
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        date: '',
        guests: 1,
        minors: 0,
        tour_type: 'Standard Historical Tour',
        notes: ''
    })

    const success = ref(false)
    const errorMsg = ref('')
    const fieldErrors = ref<Record<string, string[]>>({})

    async function submitForm(e: Event) {
        e.preventDefault()
        fieldErrors.value = {}
        errorMsg.value = ''
        success.value = false

        try {
            const config = useRuntimeConfig()
            const { data, error } = await useFetch(`${config.public.apiBase}/register-tour/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form.value)
            })

            if (error.value) {
                console.log('Form submission error:', error.value)
                if (error.value.data) {
                    fieldErrors.value = error.value.data // store per-field errors
                } else {
                    errorMsg.value = 'Something went wrong. Please try again. If the issue persist, feel free to contact our schedulers (schedulersofugs@gmail.com) personally to schedule a tour!'
                }
                return
            }

            success.value = true
        
            // clear form fields
            form.value = {
                first_name: '',
                last_name: '',
                email: '',
                phone_number: '',
                date: '',
                guests: 1,
                minors: 0,
                tour_type: 'Standard Historical Tour',
                notes: ''
            }

        } catch (err) {
            errorMsg.value = 'Network error. Please try again. If the issue persist, feel free to contact our schedulers (schedulersofugs@gmail.com) personally to schedule a tour!'
        }
    }

    // fade out success toast
    watch(success, (val) => {
        if (val) setTimeout(() => (success.value = false), 3000)
    })

    // fade out error toast
    watch(errorMsg, (val) => {
        if (val) setTimeout(() => (errorMsg.value = ''), 3000)
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