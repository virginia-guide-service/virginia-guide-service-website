<template>
    <!--Header Section-->
    <header class="relative bg-[url('/Header_Feedback.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh]">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-screen-2xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-left text-[clamp(2.5rem,6vw,3rem)] lg:text-[clamp(1rem,8vw,4rem)] [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                BETTER TOURS, TOGETHER
            </h1>
            <p class="font-['Roboto'] text-center xl:text-left uppercase text-base sm:text-md md:text-lg font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                History Tours of the University of Virginia
            </p>
        </div>
    </header>

    <!-- Overlapping Section For Feedback Form-->
    <section class="relative z-20 -mt-20 px-4 sm:px-6 lg:px-8">
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
                    <form @submit="submitForm" class="flex flex-col p-6 sm:p-8 lg:p-10 h-full">
                        <label for="fname" class="font-[Montserrat] font-light text-royal-blue">First Name</label>
                        <input type="text" id="fname" name="fname" v-model="form.first_name"
                            class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                        <label for="lname" class="font-[Montserrat] font-light text-royal-blue">Last Name</label>
                        <input type="text" id="lname" name="lname" v-model="form.last_name"
                            class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                        <label for="email" class="font-[Montserrat] font-light text-royal-blue">Email</label>
                        <input type="email" id="email" name="email" v-model="form.email"
                            class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                        <label for="number" class="font-[Montserrat] font-light text-royal-blue">Phone Number</label>
                        <input type="tel" id="number" name="number" v-model="form.phone_number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />

                        <label for="rating" class="font-[Montserrat] font-light text-royal-blue">How satisified were you with the tour overall? (Scale of 1-10)</label>
                        <select name="rating" id="rating" v-model="form.rating" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">>
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
                                <input type="date" id="date" name="date" v-model="form.date" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                            </div>
                            <div class="flex flex-col">
                                <label for="time" class="font-[Montserrat] font-light text-royal-blue">Time of Tour</label>
                                <input type="time" id="time" name="time" v-model="form.time" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                            </div>
                        </div>

                        <label for="tour-type" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                        <select name="tour-type" id="tour-type" v-model="form.tour_type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">>
                            <option value="Standard Historical">Standard Historical Tour</option>
                            <option value="History of African Americans at UVA">History of African Americans at UVA</option>
                            <option value="Memorial to Enslaved Laborers">Memorial to Enslaved Laborers</option>
                            <option value="History of Women">History of Women at UVA</option>
                            <option value="Children's Tour">Children's Tour</option>
                            <option value="Private Admissions Tours">Private Admissions Tours</option>
                            <option value="Garden Tours">Garden Tours</option>
                        </select>

                        <label for="best-part" class="font-[Montserrat] font-light text-royal-blue">Best part of the tour?</label>
                        <textarea id="best-part" v-model="form.best_part_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <label for="improvement" class="font-[Montserrat] font-light text-royal-blue">Part of the tour that needs more improvement?</label>
                        <textarea id="improvement" v-model="form.improvement_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <label for="length" class="font-[Montserrat] font-light text-royal-blue">How was the length of the tour?</label>
                        <textarea id="length" v-model="form.length_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <label for="topics" class="font-[Montserrat] font-light text-royal-blue">Were there topics or places you wish your Guide went to or discussed?</label>
                        <textarea id="topics" v-model="form.topics_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <label for="source" class="font-[Montserrat] font-light text-royal-blue">How did you hear about our tours?</label>
                        <textarea id="source" v-model="form.source_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <label for="comments" class="font-[Montserrat] font-light text-royal-blue">Feel free to add any other comments you have. Thank you!</label>
                        <textarea id="comments" v-model="form.other_comments"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-4">
                        </textarea>

                        <button type="submit"
                            class="font-[Montserrat] bg-dark-green text-white font-semibold rounded-lg px-4 py-2 hover:bg-green-700 transition-all duration-300 ease-in-out cursor-pointer">
                            Submit Feedback
                        </button>

                        <!-- Success Toast -->
                        <div v-if="success" class="fixed inset-0 flex items-center justify-center z-50 pointer-events-none">
                            <div class="font-[Montserrat] bg-green-600 text-white px-6 py-4 rounded-md shadow-lg pointer-events-auto">
                                Thank you! Your Feedback has been recieved!
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
        phone_number: '',
        rating: '',
        date: '',
        time: '',
        tour_type: '',
        best_part_message: '',
        improvement_message: '',
        length_message: '',
        topics_message: '',
        source_message: '',
        other_comments: ''
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
        const { data, error } = await useFetch('http://127.0.0.1:8000/submit-feedback/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form.value)
        })

        if (error.value) {
        if (error.value.data) {
            fieldErrors.value = error.value.data
        } else {
            errorMsg.value = 'Something went wrong. Please try again later.'
        }
        return
        }

        success.value = true

        // Clear the form
        form.value = {
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        rating: '',
        date: '',
        time: '',
        tour_type: '',
        best_part_message: '',
        improvement_message: '',
        length_message: '',
        topics_message: '',
        source_message: '',
        other_comments: ''
        }

    } catch (err) {
        errorMsg.value = 'Network error. Please try again later.'
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
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 8rem;
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