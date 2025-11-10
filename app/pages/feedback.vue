<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Rotundabasementhall.jpeg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh]">
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
                            <a href="mailto:scheduler@virginiaguides.org">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path d="M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z" />
                                <path d="M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z" />
                            </svg>
                            </a>
                            <a href="mailto:scheduler@virginiaguides.org ">
                            <p>scheduler@virginiaguides.org</p>
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
                        <select v-if="!fieldErrors.rating" name="rating" id="rating" v-model="form.rating" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">>
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
                        <select v-if="fieldErrors.rating" name="rating" id="rating" v-model="form.rating" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue">>
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
                        <p v-if="fieldErrors.rating" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.rating[0] }}
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
                                <label for="time" class="font-[Montserrat] font-light text-royal-blue">Time of Tour</label>

                                <!-- Normal state -->
                                <select
                                    v-if="!fieldErrors.time"
                                    id="time"
                                    v-model="form.time"
                                    class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5"
                                >
                                    <option value="" disabled>Select a time</option>
                                    <option
                                    v-for="time in times"
                                    :key="time.value"
                                    :value="time.value"
                                    >
                                    {{ time.display }}
                                    </option>
                                </select>

                                <!-- Error state -->
                                <select
                                    v-else
                                    id="time"
                                    v-model="form.time"
                                    class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-2 sm:px-12 md:px-20 lg:px-5 xl:px-13 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue"
                                >
                                    <option value="" disabled>Select a time</option>
                                    <option
                                    v-for="time in times"
                                    :key="time.value"
                                    :value="time.value"
                                    >
                                    {{ time.display }}
                                    </option>
                                </select>

                                <p v-if="fieldErrors.time" class="text-red-500 text-sm p-0 mb-2">
                                    {{ fieldErrors.time[0] }}
                                </p>
                            </div>
                        </div>

                        <label for="tour-type" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                        <select  v-if="!fieldErrors.tour_type" name="tour-type" id="tour-type" v-model="form.tour_type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">>
                            <option value="Standard Historical">Standard Historical Tour</option>
                            <option value="History of African Americans at UVA">History of African Americans at UVA</option>
                            <option value="Memorial to Enslaved Laborers">Memorial to Enslaved Laborers</option>
                            <option value="History of Women">History of Women at UVA</option>
                            <option value="Children's Tour">Children's Tour</option>
                            <option value="Private Admissions Tours">Private Admissions Tours</option>
                            <option value="Garden Tours">Garden Tours</option>
                        </select>
                        <select v-if="fieldErrors.tour_type" name="tour-type" id="tour-type" v-model="form.tour_type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue">>
                            <option value="Standard Historical">Standard Historical Tour</option>
                            <option value="History of African Americans at UVA">History of African Americans at UVA</option>
                            <option value="Memorial to Enslaved Laborers">Memorial to Enslaved Laborers</option>
                            <option value="History of Women">History of Women at UVA</option>
                            <option value="Children's Tour">Children's Tour</option>
                            <option value="Private Admissions Tours">Private Admissions Tours</option>
                            <option value="Garden Tours">Garden Tours</option>
                        </select>
                        <p v-if="fieldErrors.tour_type" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.tour_type[0] }}
                        </p>

                        <label for="best-part" class="font-[Montserrat] font-light text-royal-blue">Best part of the tour?</label>
                        <textarea id="best-part" v-model="form.best_part_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <label for="improvement" class="font-[Montserrat] font-light text-royal-blue">Part of the tour that needs more improvement?</label>
                        <textarea id="improvement" v-model="form.improvement_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <label for="length" class="font-[Montserrat] font-light text-royal-blue">How was the length of the tour?</label>
                        <textarea id="length" v-model="form.length_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <label for="topics" class="font-[Montserrat] font-light text-royal-blue">Were there topics or places you wish your Guide went to or discussed?</label>
                        <textarea id="topics" v-model="form.topics_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <label for="source" class="font-[Montserrat] font-light text-royal-blue">How did you hear about our tours?</label>
                        <textarea id="source" v-model="form.source_message"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <label for="comments" class="font-[Montserrat] font-light text-royal-blue">Feel free to add any other comments you have. Thank you!</label>
                        <textarea id="comments" v-model="form.other_comments"
                            class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">
                        </textarea>

                        <button type="submit"
                            class="font-[Montserrat] bg-dark-green text-white font-semibold rounded-lg px-4 py-2 hover:bg-green-700 transition-all duration-300 ease-in-out cursor-pointer">
                            Submit Feedback
                        </button>

                        <!-- Loading Spinner Overlay -->
                        <transition
                            enter-active-class="transition ease-out duration-500"
                            enter-from-class="opacity-0 translate-y-3"
                            enter-to-class="opacity-100 translate-y-0"
                            leave-active-class="transition ease-in duration-500"
                            leave-from-class="opacity-100 translate-y-0"
                            leave-to-class="opacity-0 translate-y-3"
                        >
                            <div v-if="loading" class="fixed inset-0 flex flex-col items-center justify-center z-50 bg-gray-900/60">
                                <div class="w-12 h-12 border-4 border-gray-300 border-t-transparent rounded-full animate-spin mb-4"></div>
                                <p class="text-gray-100 text-center text-sm sm:text-base px-4">
                                    Our server is waking up… this may take a few seconds. Please do not refresh or close this page.
                                </p>
                            </div>
                        </transition>

                        <!-- Success Toast -->
                        <transition
                            enter-active-class="transition transform ease-out duration-500"
                            enter-from-class="opacity-0 translate-x-10"
                            enter-to-class="opacity-100 translate-x-0"
                            leave-active-class="transition transform ease-in duration-500"
                            leave-from-class="opacity-100 translate-x-0"
                            leave-to-class="opacity-0 translate-x-10"
                        >
                            <div v-if="success && showToast" class="fixed bottom-6 right-6 z-50 pointer-events-auto animate-slide-in max-w-[90%] sm:w-80 sm:right-6 sm:bottom-6 w-full px-4 sm:px-0 flex justify-center sm:justify-end">
                                <div class="backdrop-blur-lg bg-green-700 text-white px-5 sm:px-6 py-3 sm:py-4 rounded-xl shadow-lg flex items-center justify-between space-x-3 sm:space-x-4 w-full sm:w-80">
                                <span class="font-[Montserrat] flex items-center space-x-2 text-sm sm:text-base">
                                    <svg
                                        class="w-5 h-5 text-white flex-shrink-0"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        viewBox="0 0 24 24"
                                    >
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                                    </svg>
                                    <span>Message sent successfully!</span>
                                </span>
                                <button @click="showToast = false" class="text-white hover:text-gray-200 text-lg leading-none cursor-pointer">&times;</button>
                                </div>
                            </div>
                        </transition>

                        <!-- Error Toast -->
                        <transition
                            enter-active-class="transition transform ease-out duration-500"
                            enter-from-class="opacity-0 translate-x-10"
                            enter-to-class="opacity-100 translate-x-0"
                            leave-active-class="transition transform ease-in duration-500"
                            leave-from-class="opacity-100 translate-x-0"
                            leave-to-class="opacity-0 translate-x-10"
                        >
                            <div v-if="errorMsg && showToast" class="fixed bottom-6 right-6 z-50 pointer-events-auto animate-slide-in max-w-[90%] sm:w-[28rem] sm:right-6 sm:bottom-6 w-full px-4 sm:px-0 flex justify-center sm:justify-end">
                                <div class="backdrop-blur-lg bg-red-700 text-white px-5 sm:px-6 py-3 sm:py-4 rounded-xl shadow-lg flex items-center justify-between space-x-3 sm:space-x-4 w-full sm:w-[28rem]">
                                    <svg class="w-5 h-5 text-white justify-center items-center flex-shrink-0" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
                                    </svg>
                                    <span class="text-sm sm:text-base flex-1">
                                        Something went wrong. Please try again later.
                                    </span>
                                    <button @click="showToast = false" class="text-white hover:text-gray-200 text-lg leading-none cursor-pointer">&times;</button>
                                </div>
                            </div>
                        </transition>

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
        title: 'Feedback | Virginia Guides Service',
    })

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
    const loading = ref(false)
    const showToast = ref(false)

    // Times array with display (AM/PM) and value (24-hour)
    const times = ref<{ display: string; value: string }[]>([])

    for (let h = 11; h <= 18; h++) {
    const hour12 = h > 12 ? h - 12 : h
    const period = h >= 12 && h < 24 ? 'PM' : 'AM'

    const display0 = `${hour12}:00 ${period}`
    const display30 = `${hour12}:30 ${period}`

    const value0 = `${h.toString().padStart(2, '0')}:00`
    const value30 = `${h.toString().padStart(2, '0')}:30`

    times.value.push({ display: display0, value: value0 })
    if (!(h === 18)) times.value.push({ display: display30, value: value30 }) // skip 6:30 PM
    }

    async function submitForm(e: Event) {
    e.preventDefault()
    loading.value = true
    showToast.value = false
    fieldErrors.value = {}
    errorMsg.value = ''
    success.value = false

    try {
        const config = useRuntimeConfig()
        const { data, error } = await useFetch(`${config.public.apiBase}/submit-feedback/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form.value),
            timeout: 60000 // 60 seconds
        })

        if (error.value) {
            console.log('Form submission error:', error.value)
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
            console.error('Network error or timeout:', err)
            errorMsg.value = 'Request timed out or network error. Please try again or email scheduler@virginiaguides.org to schedule a tour!'
        } finally {
            loading.value = false
            await nextTick()
            showToast.value = true
        }
    }

    // fade out success toast
    watch(success, (val) => {
        if (val) setTimeout(() => {
            success.value = false
            showToast.value = false
        }, 3000)
    })

    // fade out error toast
    watch(errorMsg, (val) => {
        if (val) setTimeout(() => {
            errorMsg.value = ''
            showToast.value = false
        }, 3000)
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