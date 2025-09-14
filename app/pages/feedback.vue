<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_Feedback.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh]">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-screen-2xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-left text-[clamp(1rem,6vw,3rem)] lg:text-[clamp(1rem,8vw,4rem)] [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                BETTER TOURS, TOGETHER
            </h1>
            <p class="font-['Roboto'] text-center xl:text-left uppercase text-base sm:text-md md:text-lg font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                History Tours of the University of Virginia
            </p>
        </div>
    </header>

    <!-- Feedback Form -->
    <section id="times-and-registration" class="relative bg-neutral-100 pt-5">
        <div class="flex flex-col lg:flex-row items-start max-w-7xl mx-auto gap-10 p-8 sm:p-6 md:p-4">
            <!-- Right: Registration Form (overlapping the section) -->
            <div class="w-full relative">
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
                            <textarea id="notes" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4"></textarea>

                            <button type="submit" class="font-[Montserrat] bg-royal-blue text-white font-semibold rounded-lg px-4 py-2 hover:bg-blue-900 transition-all duration-300 ease-in-out">
                                Register
                            </button>
                        </form>
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