<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_YourVisit.jpg')] w-full bg-cover bg-right bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
            <h1 class="font-['Playfair_Display'] italic whitespace-nowrap text-[clamp(3rem,9.5vw,5.5rem)] leading-tight">
                YOUR VISIT
            </h1>
            <p class="font-['Roboto'] text-base sm:text-md md:text-lg font-semibold leading-snug">
                DIRECTIONS & FREQUENTLY ASKED QUESTIONS
            </p>
        </div>
    </header>

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative z-20 -mt-10 px-4">
        <div class="shadow-lg rounded-xl p-6 max-w-4xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4">
                <a href="#about-tours" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition duration-300 font-semibold">
                    Times & Registration
                </a>
                <a href="#specialty-tours" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition duration-300 font-semibold">
                    Location & Parking
                </a>
                <a href="/your-visit" class="px-6 py-2 bg-white text-royal-blue text-lg rounded-full hover:bg-gray-200 hover:scale-105 transition duration-300 font-semibold">
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
                    All tours are free of charge
                </span>, regardless of group size. Donations to support work are welcome.
            </p>
            <br /><br />
            <div class="flex justify-center items-center px-4">
                <button class="border-1 text-gray-600 rounded-full py-3 px-10 cursor-pointer hover:bg-gray-200 transition duration-300">
                    Learn More
                </button>
            </div>
        </div>

        </div>
    </section>

    <!-- Tour Schedule -->
    <section class="relative bg-neutral-100">
        <div class="max-w-7xl mx-auto gap-10 p-8 sm:p-6 md:p-4 ">

            <div class="flex flex-col lg:flex-row items-start">
                    <!-- Left: Tour Schedule Text -->
                    <div class="flex flex-col items-center lg:items-start">
                        <p class="font-['Montserrat'] text-left font-medium text-UVA-orange text-4xl sm:text-5xl leading-tight mb-6">
                            TOUR SCHEDULE
                        </p>
                        <ul class="list-disc font-['Montserrat'] text-base sm:text-lg leading-relaxed text-gray-900 max-w-xl px-4">
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
                                    Register Here
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

                                    <div class="flex flex-row justify-between gap-4">
                                        <div class="flex flex-col">
                                            <label for="date" class="font-[Montserrat] font-light text-royal-blue">Date</label>
                                            <input type="date" id="date" name="date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                        </div>
                                        <div class="flex flex-col">
                                            <label for="guestNum" class="font-[Montserrat] font-light text-royal-blue">Guest(s)</label>
                                            <input type="number" id="guestNum" name="guestNum" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                                        </div>
                                    </div>

                                    <label for="guestNum" class="font-[Montserrat] font-light text-royal-blue">How many minors are in your group?</label>
                                    <input type="number" id="guestNum" name="guestNum" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />


                                    <label for="tour" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                                    <input type="text" id="tour" name="tour" value="Standard Historical Tour" readonly class="font-[Montserrat] text-royal-blue border border-gray-300 bg-gray-100 cursor-not-allowed rounded-lg px-4 py-2 focus:outline-none mb-5"/>


                                    <label for="notes" class="font-[Montserrat] font-light text-royal-blue">Notes for the Tour</label>
                                    <textarea id="notes" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4"></textarea>

                                    <button type="submit" class="font-[Montserrat] bg-royal-blue text-white font-semibold rounded-lg px-4 py-2 hover:bg-blue-900 transition duration-300">
                                        Register
                                    </button>
                                </form>
                            </div>
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
                <button class="rounded-full border border-white text-white text-base sm:text-lg px-6 py-2 mt-5 cursor-pointer hover:bg-gray-200 hover:text-black hover:border-gray-200 transition duration-300">
                    Contact Us
                </button>
            </div>
        </div>
    </section>

    <!-- Location and Parking -->
    <section class="bg-neutral-100">
        
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
                        <a href="https://maps.app.goo.gl/7nHgafiEj1LqNrcN8" class="underline text-blue-400">
                            400 Emmet Street, Charlottesville, VA, 22903
                        </a> for single family cars.
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

</template>