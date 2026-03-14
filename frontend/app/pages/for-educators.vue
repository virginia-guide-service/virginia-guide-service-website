<template>
    <!--Header Section-->
    <header class="relative bg-[url('https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/Header_ForEducators.jpg')] w-full bg-cover bg-center bg-no-repeat h-[60vh] sm:h-[75vh] bg-">
        <!-- Centered Text -->
        <div class="absolute top-1/2 left-1/2 w-full max-w-7xl px-10 -translate-x-1/2 -translate-y-1/2 text-white">
            <h1 class="font-['Playfair_Display'] italic text-center xl:text-right text-[clamp(2.5rem,7vw,3rem)] lg:text-[clamp(1rem,8vw,4rem)] leading-tight [text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)]">
                BEYOND THE CLASSROOM
            </h1>
            <p class="font-['Roboto'] text-base sm:text-md md:text-lg font-semibold leading-snug text-center xl:text-right uppercase [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                History Tours of the University of Virginia
            </p>
            <p class="font-['Roboto'] text-base sm:text-md md:text-lg font-semibold leading-snug text-center xl:text-right uppercase [text-shadow:_3px_3px_6px_rgb(0_0_0_/_0.70)]">
                For K-12 & College Groups
            </p>
        </div>
    </header> 

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative z-20 -mt-10 px-4 mb-10">
        <!-- Line in Background -->
        <div class="absolute top-1/2 left-0 w-full h-2 bg-royal-blue -z-10 hidden sm:block"></div>

        <div class="shadow-lg p-6 max-w-2xl mx-auto text-center bg-royal-blue">
            <div class="flex flex-col sm:flex-row justify-evenly items-center gap-4 text-white">
                <a href="/join-guides" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    About Us
                </a>
                <a href="/your-visit#times-and-registration" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Specialty Tour Request Form
                </a>
                <a href="/about-tours#specialty-tours" class="text-lg rounded-full hover:scale-105 transition-all duration-300 ease-in-out font-semibold">
                    Other Tours
                </a>
            </div>
        </div>
    </section>

    <!-- Info Section for different age groups -->
    <section>
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <!--Section Header-->
            <div class="flex flex-col justify-center text-left gap-3 pb-5 lg:pb-10">
                <h1 class="scrollElement uppercase font-['Playfair_Display'] italic font-medium text-dark-green text-4xl sm:text-5xl">
                    History for all ages
                </h1>
                <p class="scrollElement font-['Montserrat'] text-dark-green text-lg sm:text-xl">
                    Whether you're visiting with young learners, future students, or fellow scholars, we offer tours tailored to every stage of the educational journey.
                </p>
            </div>

            <!--Info Section For Different Age Groups-->
            <div class="flex flex-col lg:flex-row justify-center items-stretch gap-5 lg:gap-10">
                <!--Image-->
                <div class="scrollElement w-full lg:w-[40%] flex"> 
                    <img 
                        src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/for-educators-page/ChildrensTour.jpg" 
                        alt="Childrens Tour at the Amphiteather steps" 
                        class="w-full object-cover rounded-md shadow-md"
                        loading="lazy"
                    />
                </div>
                <!--Text Info-->
                <div class="w-full lg:w-[60%] flex flex-col gap-5"> 
                    <!--Kids-->
                    <div class="scrollElement flex flex-col">
                        <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                            Kids (K-5) 
                        </h1>
                        <p class="font-['Montserrat'] text-base sm:text-lg font-light">
                            A one-hour introduction to UVA that blends key moments in history with what college life is like today. Kids will hear about the University's founding vision, 
                            explore the Academical Village's architecture, learn about the 1895 burning of the Rotunda, and see how the University and its community 
                            have changed over time through resilience and creativity.
                        </p>
                    </div>
                    <!--Middle and High School-->
                    <div class="scrollElement flex flex-col">
                        <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                            Middle and High School Groups
                        </h1>
                        <p class="font-['Montserrat']  text-base sm:text-lg font-light">
                            Explore UVA's traditions, architecture, and the history of student activism and community leadership, including the legacies of slavery, the Civil War, 
                            and Civil Rights movement after, alongside at the opportunities, culture, and student life that has developed on Grounds today.
                        </p>
                    </div>
                    <!--College Students-->
                    <div class="scrollElement flex flex-col">
                        <h1 class="font-['Montserrat'] text-lg sm:text-xl font-semibold">
                            College Students 
                        </h1>
                        <p class="font-['Montserrat']  text-base sm:text-lg font-light">
                            A deeper, more detailed examination of UVA's past and present, tracing its founding ideals through periods marked by slavery, the Civil War, 
                            the 20th century eugenics movement, and progress in Civil Rights. From the 1800s to the present day, this tour reflects on how the University 
                            has acknowledged and responded to these histories through community resistance and efforts to address complex social, political, and cultural challenges still shaping the world today.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--Banner-->
    <section>
        <div class="scrollElement flex flex-col lg:flex-row w-full gap-y-3 gap-x-3 bg-gray-300 text-center py-6 px-10 lg:px-20 justify-center items-center">
            <p class="w-full lg:w-3/4 font-Roboto text-royal-blue italic text-center text-base sm:text-lg md:text-md">
                <span class="font-bold">
                    Because Virginia Guides is student-run, we do not provide tours during exam periods, reading days, or student breaks, which are specified <a href="https://registrar.virginia.edu/calendar/academic" class="underline">here</a>.
                </span>
                If interested in a student tour group, 
                <span class="font-bold">
                    please complete the <a href="/your-visit#times-and-registration" class="underline">specialty tour form</a> at least 3 weeks in advance,
                </span> to better plan with you for your tour group size, 
                interests, and needs.
            </p>
            <!--Request Tour Button-->
            <div class="w-full lg:w-1/4 flex justify-center items-center">
                <a href="/your-visit#times-and-registration">
                    <button class="flex items-center gap-2 rounded-full border border-gray-300 bg-white px-4 py-2 sm:px-6 sm:py-2 md:px-8 md:py-3 shadow-sm hover:bg-gray-100 hover:scale-105 hover:shadow-md transition-all duration-300 ease-in-out cursor-pointer">
                        <p class="font-['Roboto'] text-gray-800 font-semibold text-base md:text-lg">
                            Request Tour
                        </p>
                        <svg class="h-4 w-4 sm:h-5 sm:w-5 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <line x1="3" y1="12" x2="21" y2="12" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            <polyline points="18 15 21 12 18 9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </button>
                </a>
            </div>
        </div>
    </section>

    <!-- Last Info Section -->
    <section>
        <div class="flex flex-col justify-center text-left max-w-7xl mx-auto px-10 sm:px-12 lg:px-12 pt-12 gap-3">
            <ul class="list-disc font-['Montserrat'] text-base sm:text-lg space-y-2">
                <li class="scrollElement">
                    <span class="font-bold">
                        Tours typically last between 1-1.5 hours
                    </span>
                     limited to the areas in and surrounding the Academical Village, the heart of the UNESCO World Heritage Site designation at the University of Virginia.
                </li>
                <li class="scrollElement">
                    <span class="font-bold">
                        All tours are free of charge,
                    </span> regardless of group size. Donations to support work are welcome.
                </li>
                <li class="scrollElement">
                    Please include any unique interests or needs for your tour group in your tour-request email, we will be in contact shortly to schedule guides and information.
                </li>
            </ul>
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
    <ExploreUVAHistoryBlue />

    <!--Footer Section-->
    <Footer />

</template>

<script setup>
    import { onMounted } from "vue"
    import Footer from '~/components/Footer.vue'
    import ExploreUVAHistoryBlue from '~/components/ExploreUVAHistoryBlue.vue';

    useHead({
        title: 'For Educators | Virginia Guides Service',
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