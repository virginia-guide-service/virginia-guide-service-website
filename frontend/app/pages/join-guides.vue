<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.amazonaws.com/public/Header_JoinGuides.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[100vh]">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-7xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <p class="font-Roboto text-xs sm:text-sm md:text-md text-royal-blue font-semibold leading-snug text-center xl:text-right uppercase">
                EST. 1951 - celebrating 75 years
            </p>
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-right whitespace-nowrap text-[clamp(1rem,7vw,3rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                Our tours evolve
                <br />
                not to change the past,
                <br />
                but to share more of it.
            </h1>
        </div>
    </header>

    <!-- About Guides Info Section -->
    <section id="about-tours">
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <p class="scrollElement font-['Playfair_Display'] italic text-center font-medium text-dark-green text-4xl sm:text-5xl leading-tight py-5 lg:pt-0">
                ESTABLISHED 1951
            </p>
            <!--Flex-->
            <div class="flex justify-center items-center flex-col lg:flex-row gap-x-10">
                <!-- Left: Image -->
                <div class="scrollElement w-full lg:w-1/2 flex justify-center items-center">
                    <img src="https://virginia-guides-website-images.s3.amazonaws.com/public/join-guides-page/TourTaking2.jpg" alt="Historical Tour Image" loading="lazy" class="object-cover w-full rounded-md max-w-sm md:max-w-md lg:max-w-lg shadow-md">
                </div>

                <!-- Right: Text -->
                <div class="scrollElement w-full lg:w-1/2">
                    <p class="font-['Montserrat'] text-center lg:text-start text-base sm:text-lg leading-relaxed text-gray-900 pt-5">
                        The Virginia Guide Service, founded in 1951, is a completely student-run and independent organization dedicated 
                        to preserving and sharing the history of the University of Virginia. Through honest, inclusive, and engaging storytelling, 
                        our guides strive to represent the diversity of student experiences while fostering a welcoming environment for all visitors.
                    </p>
                    <p class="font-['Montserrat'] text-center lg:text-start text-base sm:text-lg leading-relaxed text-gray-900 pt-5">
                        Each semester, new trainees undergo a rigorous training process where they study UVA’s history, practice essential 
                        tour-giving skills, and receive mentorship from experienced guides, professors, and community leaders. Together, we are committed to 
                        providing the highest quality tour experience while honoring and expanding the University’s historical narrative—ensuring it remains 
                        accessible, accurate, and meaningful for generations to come.
                    </p>
                </div>
            </div>

            <!--Volunteer Statement-->
            <span class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-dark-green text-center pt-5 lg:pt-10">
                The Virginia Guide Service is independent and volunteer-based, which gives each guide the opportunity to craft their own tour. 
                Students are encouraged to follow their passion and engage deeply with history. If you would like to provide additional support, please consider 
                donating to our day-to-day operations <a href="/donate" class="underline p-0 m-0">here</a>. We appreciate your time and thank you for continuing to support our mission.
            </span>
        </div>
    </section>

    <!--Directions: Join Guides-->
    <section id="join-guides">

        <!--Running Banner: Join Guides-->
        <div class="scrollElement running-text-container font-[Roboto] font-medium text-[#ECE9E9]">
            <!--First Copy-->
            <ul>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
            </ul>
            <!--First Copy for seamless animation-->
            <ul aria-hidden="true">
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
            </ul>
        </div>

        <!--Step 1 and 2 Container-->
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <!--Step 1-->
            <div class="scrollElement text-center sm:text-start">
                <h1 class="font-Roboto text-lg sm:text-xl font-bold italic pb-2">
                    Step 1: Attend an Info Session and Learn About the Virginia Guides Service
                </h1>
                <p class="font-Roboto font-light text-base sm:text-lg pb-2">
                    Guides accepts new members at the beginning of each semester. These probationary members, known as “probies," 
                    spend a semester being trained by their Guides Probationary Chairs (fellow students and current Guides) and learning 
                    from older guides to prepare to give tours. Students trying out for Guides must be in their first, second, or third year, 
                    and should be able to commit to attending weekly Probie Class - a crash course in UVA history led by your Probie Chair - 
                    for three hours each Thursday night during their Probie Semester.
                </p>
                <p class="font-Roboto font-light text-base sm:text-lg">
                    As the recruitment season begins, follow us on Instagram to keep up to date throughout the recruitment process! Our instagram
                    will also give you a closer look at the regular happenings of the Virginia Guides Service-make sure to check out our student 
                    spotlights and takeovers, which let you hear from current Guides about their experiences in the organization!
                </p>
            </div>

            <!--Info Sessions and Step 2-->
            <div class="flex flex-col lg:flex-row">
                <div class="w-full text-center sm:text-start">
                    <p class="scrollElement font-Roboto font-light text-base sm:text-lg italic pt-5 pb-2">
                        <span class="font-bold">Info Sessions:</span>
                        We ask that you attend an information session to learn more about the Virginia Guide Service and 
                        speak to current Guides. Attending information and Q&A sessions will help you learn about the try-out process, get tips from current guides, 
                        and learn more about what is expected of VGS members. Information sessions are <span class="font-bold underline">mandatory</span> and a great way to get your questions 
                        answered and better understand what makes VGS so great! In addition to our general information sessions, we have <span class="font-bold">BIPOC-centered information sessions</span>
                        as well. BIPOC Guides will be at these specialized info sessions to answer questions and discuss what it's like to identify within these communities while being part of VGS.
                        Below is our info session schedule for Spring 2026.
                    </p>
                    <ul class="scrollElement text-center font-Roboto text-base sm:text-lg pb-2">
                        <li class="font-bold ">General Information Sessions:</li>
                        <li>Monday, January 26th 6:30 PM - 7:30 PM (MOVED <a class="underline text-blue-500" href="https://virginia.zoom.us/j/97903234893?pwd=gSXbR9jGhdDznmM4aZJ9fkbaA8afPC.1">ONLINE</a>)</li>
                        <li>Wednesday, January 28th 6:30 PM - 7:30 PM @ MPR</li>
                        <li>Friday, January 30th 4:00 PM - 5:00 PM @ MPR</li>
                        <li>Saturday, January 31st 12:00 PM - 1:00 PM @ MPR</li>
                        <li>Monday, February 2nd 7:30 PM - 8:30 PM @ Cocke Hall 101</li>
                        <li class="font-bold pt-2">BIPOC Centered Information Sessions:</li>
                        <li>Tuesday, January 27th 7:30 PM - 8:30 PM (MOVED <a class="underline text-blue-500" href="https://us05web.zoom.us/j/89324547703?pwd=CtZgycVEWFu1KmdplFOlad27cfBDaB.1">ONLINE</a>)</li>
                        <li>Thursday, January 29th 6:30 PM - 7:30 PM @ MPR</li>
                        <li class="text-UVA-orange italic font-bold pt-2">LW: Lower West Oval Room (inside the Rotunda basement)</li>
                        <li class="text-UVA-orange italic font-bold">MPR: Multipurpose Room (beneath Rotunda steps)</li>
                    </ul>
                    <p class="scrollElement font-Roboto font-light text-base sm:text-lg italic">
                        For additional Preparation we encourage all those planning on trying out to attend a tour the week of <span class="font-bold underline">January 18th</span> to get a better understanding of all our 
                        tours encapsulate. While this is not a requirement by any means, the best way to learn what we do is to see it in action!
                    </p>
                    <div class="scrollElement">
                        <h1 class="font-Roboto text-lg sm:text-xl font-bold italic mb-2 pt-5">
                            Step 2: Prepare to Try Out
                        </h1>
                        <p class="font-Roboto font-light text-base sm:text-lg pb-2">
                            For our Spring 2026 recruitment season, you will give a 15 minute historical “trial tour” of the Lawn area to two current Guides 
                            (who will act as your "tourists"). The trial tour is meant to see how well you can craft an organized and meaningful tour, 
                            as well as to assess your public speaking abilities.
                        </p>
                        <p class="font-Roboto font-light text-base sm:text-lg">
                            You will be able to sign up for a time slot between <span class="font-bold underline italic">February 2nd through the 7th</span> for your trial tour at one of our 
                            info sessions (which is why it is important to attend a session)! Other sign-up opportunities may be offered, 
                            and will be announced via Instagram. If you can't make it to the sign-up times, or need to cancel or reschedule 
                            your trial tour for any reason, you can reach out to our Recruitment Co-Chairs to see what slots are available.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!--Banner-->
        <div>
            <div class="scrollElement w-full bg-dark-green text-center py-6 px-10 lg:px-20 flex justify-center items-center">
                <span class="font-Roboto text-white text-center text-base sm:text-lg md:text-md">
                    To begin writing, we encourage you to refer to this <a href="https://docs.google.com/document/d/1SgT3gxmUICInw1gs1LGYnTQ4pzVWFVgJZrtIZ2Z4Mes/edit?usp=sharing" class="underline">historical fact sheet</a>
                    we have put together for you. Once you have written your tour, we recommend practicing giving your tour before you do so officially. 
                    As you prepare, please reach out to our Recruitment Co-Chairs, Natalie <a href="mailto:wmz4hj@virginia.edu" class="underline">(wmz4hj@virginia.edu)</a>
                     and Menna <a href="mailto:wab7sk@vriginia.edu" class="underline">(wab7sk@vriginia.edu)</a>, for any help you may need. 
                    They are equipped to offer you advice on how to go about your tours, suggestions for what to include, 
                    and any help you might need to prepare! The Recruitment Co-Chairs have no say in the selection process, 
                    meaning that you can truly ask them anything - they're here to make sure you have the best possible experience trying out.
                </span>
            </div>
        </div>

        <!--Step 3 and 4 Container-->
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <!--Step 3-->
            <div class="scrollElement text-center sm:text-start">
                <h1 class="font-Roboto text-lg sm:text-xl font-bold italic pb-2">
                    Step 3: Give Your Trial Tour
                </h1>
                <p class="font-Roboto font-light text-base sm:text-lg pb-2">
                    Before your trial tour, you will receive an email with the Lawn room number where your “tourists” will meet you for your trial tour. 
                    Please plan to arrive ten minutes early to help the process run smoothly.
                </p>
                <p class="font-Roboto font-light text-base sm:text-lg pb-2">
                    We completely understand that giving a trial tour can be very nerve wracking, but we highly encourage you to just go ahead and do it! Your “tourists” 
                    are your biggest supporters and would love to see you do an incredible job. If you're feeling nervous, we strongly recommend reaching out to 
                    the Recruitment Co-Chairs who would be happy to help you with any concerns you may have.
                </p>
                <p class="font-Roboto font-light text-base sm:text-lg">
                    Once you arrive, there will be a current Guide there to answer any last minute questions you may have and help you with what you may need then. Feel free to 
                    leave your belongings in this room and they will be happy to watch over your items. Your “tourists” will meet you at the room and they will provide 
                    some starting information. You can then walk with them to the starting location that you have selected for your tour before your time for the tour starts.
                </p>
            </div>

            <!--Step 4-->
            <div class="scrollElement text-center sm:text-start">
                <h1 class="font-Roboto text-lg sm:text-xl font-bold italic mb-2 pt-5">
                    Step 4: Interview
                </h1>
                <p class="font-Roboto font-light text-base sm:text-lg">
                    At the end of your trial tour, your “tourists” will tell you when and where the list of students selected to receive an interview will be posted.
                    The interview will be the week following trial tours, and is conducted by a panel of current guides who will assess your diplomacy and ability 
                    to improvise in response to tough tour questions. It's also a chance for you to share with us what sets you apart and would make you an excellent 
                    member of Guides. More information on the interview stage of the process is provided after trial tours have concluded. After the interview process, 
                    we will welcome new probationary members for the amazing semester ahead!
                </p>
            </div>
        </div>
    
        <!--Running Banner: Join Guides-->
        <div class="scrollElement running-text-container font-[Roboto] font-medium text-[#ECE9E9] pb-12">
            <!--First Copy-->
            <ul>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
            </ul>
            <!--First Copy for seamless animation-->
            <ul aria-hidden="true">
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">JOIN GUIDES&nbsp;</span>
                </li>
            </ul>
        </div>

    </section>

    <!-- Explore UVA History Section -->
    <ExploreUVAHistoryBlue />

    <!--Footer Section-->
    <Footer />

</template>

<script setup>
    import { ref } from 'vue';
    import { onMounted } from "vue"
    import Footer from '~/components/Footer.vue'
    import ExploreUVAHistoryBlue from '~/components/ExploreUVAHistoryBlue.vue';

    useHead({
        title: 'Join Guides | Virginia Guides Service',
        link: [
            { rel: 'preload', as: 'image', href: 'https://virginia-guides-website-images.s3.amazonaws.com/public/Header_JoinGuides.jpg', fetchpriority: 'high' }
        ]
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

    const joinGuides = ref(true); // set to true so that the section shows up on the page on load
    const beingAGuide = ref(false);

    const toggleBeingAGuide = () => {
        beingAGuide.value = true;
        joinGuides.value = false;
    }

    const toggleJoinGuides = () => {
        joinGuides.value = true;
        beingAGuide.value = false;
    }
    
</script>

<style>
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 6rem;
    }
    .about-carousel-body {
        width: 100%;
        height: var(--height);
        display: grid;
        place-items: center;
    }
    .about-slider{
        height: 300px;
        margin: auto;
        position: relative;
        width: 100%;
        display: grid;
        place-items: center;
        overflow: hidden;
    }
    .about-slide-track{
        display: flex;
        width: calc(350px * 10);
        animation: scroll 15s linear infinite;
        will-change: transform;
    }
    @keyframes scroll {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(calc(-350px * 10));
        }
    }
    .about-slide{
        height: 250px;
        width: 350px;
        display: flex;
        align-items: center;
        padding: 5px;
    }
    .about-carousel-img{
        width: 100%;
        height: 100%;
        object-fit: cover;
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
    .running-text-container {
        /* margin: 20px; */
        font-size: 5em;
        /* padding-block: 8px;
        border-block: 1px solid; */
        overflow: hidden;
        user-select: none;

        --gap: 20px;
        display: flex;
        gap: var(--gap);
    }
    .running-text-container ul {
        display: flex;
        flex-shrink: 0;
        min-width: 100%;
        justify-content: space-between;
        align-items: center;
        gap: var(--gap);
        animation: text-scroll 20s linear infinite;
        will-change: transform;
    }

    @keyframes text-scroll {
        to {
            transform: translateX(calc(-100% - var( --gap)));
        }
    }
</style>
