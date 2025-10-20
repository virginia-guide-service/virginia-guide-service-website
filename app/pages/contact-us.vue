<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_ContactUS.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-7xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] text-center xl:text-right italic text-[clamp(2rem,9.5vw,5rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                VIRGINIA GUIDES
            </h1>
            <p class="font-Roboto text-center xl:text-right text-sm sm:text-lg md:text-md font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
        </div>
    </header> 

    <!-- Overlapping Section For Contact Us Form-->
    <section class="relative z-20 -mt-20 px-4 sm:px-6 lg:px-8">
        <div class="shadow-xl p-6 max-w-7xl mx-auto bg-white mb-10">
            <div class="flex flex-col lg:flex-row justify-between gap-y-8 gap-x-10">
                <!-- Left: Information Section -->
                <div class="w-full lg:w-[40%] flex flex-col bg-royal-blue text-white font-Roboto p-6 sm:p-8 lg:p-10 text-center md:text-left">
                    <!--Text-->
                    <div class="flex flex-col gap-8 mb-10">
                        <h1 class="text-3xl sm:text-4xl md:text-5xl font-medium">
                            Contact Us
                        </h1>
                        <div class="text-base md:text-lg font-light flex flex-col gap-3">
                            <p>Got questions or want to plan a tour with us? We'd love to hear from you!</p>
                            <p>Let's get in touch.</p>
                            <p>
                            If you would like to personally contact our chairs,
                            <a href="mailto:jyr7db@virginia.edu, xuy8gc@virginia.edu" class="underline">
                                Nina and Rose,
                            </a>
                            feel free to do so as well!
                            </p>
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

                    <a href="/request-specialty-tours">
                        <button class="font-medium rounded-full border-2 border-white px-4 py-3 mt-6 hover:bg-white hover:scale-105 hover:text-royal-blue transition-all duration-300 ease-in-out cursor-pointer">
                            Specialty Tour Request Form
                        </button>
                    </a>
                    </div>
                </div>

                <!-- Right: Contact Us Form -->
                <div class="w-full lg:w-[60%] flex flex-col h-full">
                    <form @submit="submitForm" class="flex flex-col p-6 sm:p-8 lg:p-10 h-full">
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
                        <input v-if="!fieldErrors.email" type="email" id="email" name="email" v-model="form.email" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                        <input v-if="fieldErrors.email" type="email" id="email" name="email" v-model="form.email" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                        <p v-if="fieldErrors.email" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.email[0] }}
                        </p>

                        <label for="subject" class="font-[Montserrat] font-light text-royal-blue">Subject</label>
                        <input v-if="!fieldErrors.subject" type="text" id="subject" name="subject" v-model="form.subject" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                        <input v-if="fieldErrors.subject" type="text" id="subject" name="subject" v-model="form.subject" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                        <p v-if="fieldErrors.subject" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.subject[0] }}
                        </p>

                        <label for="message" class="font-[Montserrat] font-light text-royal-blue">Message</label>
                        <textarea v-if="!fieldErrors.message" id="message" v-model="form.message" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4"></textarea>
                        <textarea v-if="fieldErrors.message" id="message"  v-model="form.message" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue"></textarea>
                        <p v-if="fieldErrors.message" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.message[0] }}
                        </p>

                        <button type="submit"
                            class="font-[Montserrat] bg-dark-green text-white font-semibold rounded-lg px-4 py-2 hover:bg-green-700 transition-all duration-300 ease-in-out cursor-pointer">
                            Send Message
                        </button>

                        <!-- Success Toast -->
                        <div v-if="success" class="fixed inset-0 flex items-center justify-center z-50 pointer-events-none">
                            <div class="font-[Montserrat] bg-green-600 text-white px-6 py-4 rounded-md shadow-lg pointer-events-auto">
                                Thank you! Your message has been sent!
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
    </section>

    <!--Instagram Plug section-->
    <section>
        <div class="scrollElement relative w-full shadow-md bg-dark-green py-6 px-4 sm:px-6 lg:px-8">
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
    <section class="bg-white py-16 sm:py-20 md:py-24">
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">

            <!-- Header -->
            <h1 class="scrollElement font-['Playfair_Display'] text-UVA-orange text-3xl sm:text-4xl md:text-5xl font-medium">
                Explore UVA History
            </h1>

            <!-- Description -->
            <p class="scrollElement font-['Montserrat'] text-black text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                In addition to our regularly scheduled historical tours, we also offer Specialty Tours by request,
                which focus on a specific aspect of UVA's extensive 200 year history.
            </p>

            <!-- Button -->
            <a href="/about-tours">
                <button class="scrollElement inline-flex items-center space-x-3 rounded-full border-1 border-gray-300 text-black font-['Montserrat'] text-base sm:text-lg md:text-xl py-3 px-6 hover:text-royal-blue hover:bg-gray-100 hover:scale-105 transition-all duration-300 ease-in-out hover:cursor-pointer">
                    <span>HISTORY TOURS</span>
                    <svg class="flex-shrink-0" height="25px" width="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 12H18M18 12L13 7M18 12L13 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </a>
        </div>

        <!-- Carousel: Our Tours-->
        <div class="scrollElement carousel-body">
            <div class="slider">
                <div class="slide-track">
                    <a href="/about-tours/#history-of-women-at-uva">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black  font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black  font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">Children's Tour</p>
                        </div>
                    </a>
                    <!--Same 5 slides (doubled)-->
                    <a href="/about-tours/#history-of-women-at-uva">
                        <div class="slide flex flex-col justify-start">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_womenatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">History of Women</p>
                        </div>
                    </a>
                    <a href="/about-tours/#history-of-african-americans-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img object-top" src="/index-page/carousel-history-tours/UVAhistoryCarousel_africanamericansatuva.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">History of African-Americans</p>
                        </div>
                    </a>
                    <a href="/about-tours/#garden-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_GardenTours.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">Garden Tours</p>
                        </div>
                    </a>
                    <a href="/about-tours/#MEL-tour">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_MEL.jpeg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">Memorial to Enslaved Laborers</p>
                        </div>
                    </a>
                    <a href="/about-tours/#childrens-tours">
                        <div class="slide flex flex-col">
                            <img class="carousel-img" src="/index-page/carousel-history-tours/UVAhistoryCarousel_childrenstour.jpg" loading="lazy" alt="">
                            <p class="carousel-text self-start text-black font-['Roboto']">Children's Tour</p>
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
            class="w-full min-h-screen sm:h-[120vh] object-cover object-top"
            />

            <!-- Overlay Content -->
            <div class="absolute top-1/2 left-1/2 w-full max-w-6xl px-4 sm:px-6 lg:px-8 -translate-x-1/2 -translate-y-1/2 text-center z-10">

                <!-- Header -->
                <div class="absolute left-1/2 w-full max-w-6xl px-4 -translate-x-1/2 -translate-y-1/2 text-white text-center">
                    <h1 class="scrollElement font-['Playfair_Display'] italic text-center xl:text-left whitespace-nowrap text-[clamp(3rem,9.5vw,4rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                        SHED LIGHT
                    </h1>
                    <p class="scrollElement font-Roboto text-center xl:max-w-sm xl:text-right text-xl sm:text-2xl md:text-3xl font-extralight leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                        ON HISTORY
                    </p>
                </div>

                <!-- Buttons -->
                <div class="scrollElement mt-35 md:mt-40 flex flex-col sm:flex-row justify-center items-center gap-x-10 gap-y-4 pointer-events-auto">
                    <a href="/your-visit">
                        <button class="font-['Roboto'] border-1 border-gray-300 text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-gray-100 hover:scale-105 rounded-full py-3 px-10 cursor-pointer transition-all duration-300 ease-in-out">
                            TAKE A TOUR
                        </button>
                    </a>
                    <a href="/donate">
                        <button class="font-['Roboto'] border-1 border-gray-300 text-white hover:text-black bg-[rgba(0,0,0,0.30)] hover:bg-gray-100 hover:scale-105 rounded-full py-3 px-15 cursor-pointer transition-all duration-300 ease-in-out">
                            DONATE
                        </button>
                    </a>
                </div>

                <!-- Description -->
                <p class="scrollElement mt-20 font-['Roboto'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
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
                <div class="scrollElement basis-1/2 flex flex-wrap justify-between gap-6 text-sm text-zinc-400 font-['Roboto']">
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
                <div class="scrollElement basis-1/2 flex flex-col gap-3 text-zinc-400 text-sm md:text-base font-light">
                    <div class="flex items-start gap-4 font-['Roboto']">
                        <img class="h-12 w-12 obSject-contain" src="/guides-logo.png" loading="lazy" alt="Virginia Guides Logo" />
                        <p>
                            The Virginia Guides continues 75 years of guiding visitors through UVA in Charlottesville VA. The Guides Service is a 
                            student-run organization independent of the University of Virginia, carrying forward tradition while bringing a more complete light to the past.
                        </p>
                    </div>

                    <div class="flex justify-center md:justify-end">
                        <a href="/contact-us">
                            <button class="border-1 border-gray-300 text-white rounded-full px-6 py-2 font-['Montserrat'] hover:bg-gray-100 hover:scale-105 hover:text-black transition-all duration-300 ease-in-out cursor-pointer">
                                CONTACT US
                            </button>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

</template>

<script setup lang="ts">
    import { onMounted } from "vue"
    import { ref } from 'vue'

    const form = ref({
        first_name: '',
        last_name: '',
        email: '',
        subject: '',
        message: ''
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
            const { data, error } = await useFetch('http://127.0.0.1:8000/contact-us/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(form.value)
            })

            if (error.value) {
                if (error.value.data) {
                    fieldErrors.value = error.value.data // store per-field errors
                } else {
                    errorMsg.value = 'Something went wrong. Please try again. If the issue persist, feel free to contact our chairs or schedulers personally!'
                }
                return
            }

            success.value = true

            // clear form fields
            form.value = {
                first_name: '',
                last_name: '',
                email: '',
                subject: '',
                message: ''
            }

        } catch (err) {
            errorMsg.value = 'Network error. Please try again. If the issue persist, feel free to contact our chairs or schedulers personally!'
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
    .scrollElement {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .scrollElement.show {
        opacity: 1;
        transform: translateY(0);
    }
</style>