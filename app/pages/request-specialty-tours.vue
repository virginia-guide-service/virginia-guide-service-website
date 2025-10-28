<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_SpecialtyToursRequest.jpeg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-[40%] left-1/2 w-full max-w-8xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] text-center xl:text-right italic text-[clamp(2rem,9.5vw,5rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                VIRGINIA GUIDES
            </h1>
            <p class="font-Roboto text-center xl:text-right text-sm sm:text-lg md:text-md font-semibold leading-snug [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                HISTORICAL TOURS OF THE UNIVERSITY OF VIRGINIA
            </p>
        </div>
        <!--Banner-->
        <div class="absolute top-[70%] left-1/2 w-full -translate-x-1/2 -translate-y-1/2 flex flex-col items-center justify-evenly gap-1 shadow-md bg-dark-green/80 py-6 px-4 sm:px-6 lg:px-8">
            <!-- Description -->
            <div class="font-['Montserrat'] text-white text-center justify-start text-sm md:text-base max-w-6xl">
                <a class="italic">To ensure guide availability for special topic or large tour groups, all tour requests. should be submitted at least </a>
                    <a class="underline italic">two to three weeks in advance</a>. 
                <a class="italic"> Complete this form and we can get back to you with more details on your tour!</a> 
                Standard Historical tours occur regularly throughout the school year and do not require a special request.
            </div>
        </div>
    </header> 

    <!-- Overlapping Section For Feedback Form-->
    <section class="relative z-20 -mt-10 md:-mt-15 px-4 sm:px-6 lg:px-8">
        <div class="shadow-xl p-6 max-w-7xl mx-auto bg-white mb-10">
            <div class="flex flex-col lg:flex-row justify-between gap-y-8 gap-x-10">
                <!-- Left: Information Section -->
                <div class="w-full lg:w-[40%] flex flex-col bg-royal-blue text-white font-Roboto p-6 sm:p-8 lg:p-10 text-center md:text-left">
                    <!--Text-->
                    <div class="flex flex-col gap-8 mb-10">
                        <h1 class="text-3xl sm:text-4xl md:text-5xl font-medium">
                            Specialty Tour Request
                        </h1>
                        <div class="text-base md:text-lg font-light flex flex-col gap-3">
                            <p>Got questions or want to plan a tour with us? Include the information in the message or email us. We'd love to hear from you!</p>
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

                        <div class="flex flex-col text-center items-center gap-4 justify-center md:justify-start mt-30">
                            <p>
                                After completing your tour request, click here for information on directions, parking and your visit.
                            </p>
                            <a href="/your-visit">
                                <button class="font-medium rounded-full border-2 border-white px-6 py-2 hover:bg-white hover:text-royal-blue hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer">
                                    Plan Your Visit
                                </button>
                            </a>
                        </div>

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

                        <label for="number" class="font-[Montserrat] font-light text-royal-blue">Phone Number</label>
                        <input v-if="!fieldErrors.phone_number" type="tel" id="number" name="number" v-model="form.phone_number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5" />
                        <input v-if="fieldErrors.phone_number" type="tel" id="number" name="number" v-model="form.phone_number" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue" />
                        <p v-if="fieldErrors.phone_number" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.phone_number[0] }}
                        </p>

                        <div class="flex flex-col lg:flex-row justify-between lg:gap-4">
                            <div class="flex flex-col">
                                <label for="date" class="font-[Montserrat] font-light text-royal-blue">Requested Date of Tour</label>
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

                        <label for="tour-type" class="font-[Montserrat] font-light text-royal-blue">Type of Tour</label>
                        <select v-if="!fieldErrors.tour_type" name="tour-type" id="tour-type" v-model="form.tour_type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">>
                            <option value="Standard Historical">Standard Historical Tour</option>
                            <option value="History of African Americans at UVA">History of African Americans at UVA</option>
                            <option value="Memorial to Enslaved Laborers">Memorial to Enslaved Laborers</option>
                            <option value="History of Women">History of Women at UVA</option>
                            <option value="Children's Tour">Children's Tour</option>
                            <option value="Private Admissions Tours">Private Admissions Tours</option>
                            <option value="Garden Tours">Garden Tours</option>
                        </select>
                        <select v-if="fieldErrors.tour_type" name="tour-type" id="tour-type" v-model="form.tour_type" class="font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5">>
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

                        <label for="notes" class="font-[Montserrat] font-light text-royal-blue">Tour Group Information & Details</label>
                        <textarea v-if="!fieldErrors.notes" id="notes" v-model="form.notes" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue mb-5"> </textarea>
                        <textarea v-if="fieldErrors.notes" id="notes" v-model="form.notes" class="flex-grow font-[Montserrat] text-royal-blue border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-royal-blue"> </textarea>
                        <p v-if="fieldErrors.notes" class="text-red-500 text-sm p-0 mb-2">
                            {{ fieldErrors.notes[0] }}
                        </p>

                        <button type="submit"
                            class="font-[Montserrat] bg-dark-green text-white font-semibold rounded-lg px-4 py-2 hover:bg-green-700 transition-all duration-300 ease-in-out cursor-pointer">
                            Request Tour
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
        title: 'Specialty Tour Request | Virginia Guides Service',
    })

    const form = ref({
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        date: '',
        guests: 1,
        minors: 0,
        tour_type: '', // can set a default
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
            const { data, error } = await useFetch(`${config.public.apiBase}/request-specialty-tours/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(form.value)
            })

            if (error.value) {
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
                tour_type: '',
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