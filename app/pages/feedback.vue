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

    <!-- Overlapping Section For Feedback Form-->
    <section class="relative z-20 -mt-20 px-4">
        <div class="shadow-xl p-6 max-w-7xl mx-auto bg-white mb-10">
            <div class="flex flex-col lg:flex-row justify-between gap-y-8 gap-x-10">
                <!-- Left: Information Section -->
                <div class="w-full lg:w-[40%] flex flex-col bg-royal-blue text-white font-Roboto p-6 sm:p-8 lg:p-10 text-center md:text-left">
                    <!--Text-->
                    <div class="flex flex-col gap-8 mb-10">
                        <h1 class="text-3xl sm:text-4xl md:text-5xl font-medium">
                            Feedback
                        </h1>
                        <div class="text-base md:text-lg font-light flex flex-col gap-3">
                            <p>Thank you for submitting your feedback. We greatly appreciate the chance to hear back from 
                                the community and guests, and use your feedback to improve our tours.</p>
                            <p>Have any further questions? We'd love to hear from you! </p>
                            <p>Lets get in touch.</p>
                        </div>
                    </div>

                    <!--Icons and Links-->
                    <div class="text-base md:text-lg font-light flex flex-col gap-3">
                        <div class="flex items-center gap-2 justify-center md:justify-start">
                            <a href="mailto:chair@virginiaguides.org">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path d="M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z" />
                                <path d="M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z" />
                            </svg>
                            </a>
                            <a href="mailto:chair@virginiaguides.org">
                            <p>chair@virginiaguides.org</p>
                            </a>
                        </div>

                        <div class="flex items-center gap-2 justify-center md:justify-start">
                            <a href="mailto:schedulersofugs@gmail.com">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path d="M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z" />
                                <path d="M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z" />
                            </svg>
                            </a>
                            <a href="mailto:schedulersofugs@gmail.com">
                            <p>schedulersofugs@gmail.com</p>
                            </a>
                        </div>

                        <div class="flex items-center gap-2 justify-center md:justify-start">
                            <a href="https://instagram.com/virginiaguides">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                            </svg>
                            </a>
                            <a href="https://instagram.com/virginiaguides">
                            <p>@virginiaguides</p>
                            </a>
                        </div>

                        <div class="flex items-center gap-2 justify-center md:justify-start">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                            <path fill-rule="evenodd" d="m11.54 22.351.07.04.028.016a.76.76 0 0 0 .723 0l.028-.015.071-.041a16.975 16.975 0 0 0 1.144-.742 19.58 19.58 0 0 0 2.683-2.282c1.944-1.99 3.963-4.98 3.963-8.827a8.25 8.25 0 0 0-16.5 0c0 3.846 2.02 6.837 3.963 8.827a19.58 19.58 0 0 0 2.682 2.282 16.975 16.975 0 0 0 1.145.742ZM12 13.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd" />
                            </svg>
                            <p>Charlottesville, Virginia 22904</p>
                        </div>
                    </div>
                </div>

                <!-- Right: Contact Us Form -->
                <div class="w-full lg:w-[60%] flex flex-col h-full">
                    <form class="flex flex-col p-6 sm:p-8 lg:p-10 h-full">
                    <label for="fname" class="font-[Montserrat] font-light text-royal-blue">First Name</label>
                    <input type="text" id="fname" name="fname"
                        class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                    <label for="lname" class="font-[Montserrat] font-light text-royal-blue">Last Name</label>
                    <input type="text" id="lname" name="lname"
                        class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                    <label for="email" class="font-[Montserrat] font-light text-royal-blue">Email</label>
                    <input type="email" id="email" name="email"
                        class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                    <label for="number" class="font-[Montserrat] font-light text-royal-blue">Phone Number</label>
                    <input type="tel" id="number" name="number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                    <label for="rating" class="font-[Montserrat] font-light text-royal-blue">How satisified were you with the tour overall? (Scale of 1-10)</label>
                    <select name="rating" id="rating" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>

                    <div class="flex flex-col lg:flex-row justify-between lg:gap-4">
                        <div class="flex flex-col">
                            <label for="date" class="font-[Montserrat] font-light text-royal-blue">Intended Date of Tour</label>
                            <input type="date" id="date" name="date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                        </div>
                        <div class="flex flex-col">
                            <label for="time" class="font-[Montserrat] font-light text-royal-blue">Time of Tour</label>
                            <input type="time" id="time" name="time" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                        </div>
                    </div>

                    <label for="tour-type" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                    <select name="tour-type" id="tour-type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">>
                        <option value="StandardHistorical">Standard Historical Tour</option>
                        <option value="HistoryofAfricanAmericansatUVA">History of African Americans at UVA</option>
                        <option value="MemorialtoEnslavedLaborer">Memorial to Enslaved Laborers</option>
                        <option value="HistoryofWomen">History of Women at UVA</option>
                        <option value="ChildrensTour">Children's Tour</option>
                        <option value="PrivateAdmissionsTours">Private Admissions Tours</option>
                        <option value="GardenTours">Garden Tours</option>
                    </select>

                    <label for="best-part" class="font-[Montserrat] font-light text-royal-blue">Best part of the tour?</label>
                    <textarea id="best-part"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <label for="improvement" class="font-[Montserrat] font-light text-royal-blue">Part of the tour that needs more improvement?</label>
                    <textarea id="improvement"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <label for="length" class="font-[Montserrat] font-light text-royal-blue">How was the length of the tour?</label>
                    <textarea id="length"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <label for="topics" class="font-[Montserrat] font-light text-royal-blue">Were there topics or places you wish your Guide went to or discussed?</label>
                    <textarea id="topics"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <label for="source" class="font-[Montserrat] font-light text-royal-blue">How did you hear about our tours?</label>
                    <textarea id="source"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <label for="comments" class="font-[Montserrat] font-light text-royal-blue">Feel free to add any other comments you have. Thank you!</label>
                    <textarea id="comments"
                        class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                    </textarea>

                    <button type="submit"
                        class="font-[Montserrat] bg-dark-green text-white font-semibold rounded-lg px-4 py-2 hover:bg-green-700 transition-all duration-300 ease-in-out cursor-pointer">
                        Submit Feedback
                    </button>
                    </form>
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