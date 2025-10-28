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
            <p class="scrollElement font-['Montserrat'] text-base sm:text-lg leading-relaxed text-dark-green text-center pt-5 lg:pt-10">
                The Guide Service is independent and volunteer-based, which gives each guide the opportunity to craft their own tour. 
                Students are encouraged to follow their passion and engage deeply with history. If you would like to provide additional support, please consider 
                donating to our day-to-day operations 
                <a href="/donate" class="underline p-0 m-0">
                    here.
                </a> We appreciate your time and thank you for continuing to support our mission
            </p>
        </div>
    </section>

    <!-- Overlapping Section With Buttons for Navigations-->
    <section class="relative scrollElement">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <!-- Blue Line in Background -->
            <div class="absolute top-1/2 left-0 w-full h-1 bg-royal-blue -z-10"></div>

            <!-- Join/Being Buttons -->
            <div class="shadow-lg rounded-xl max-w-lg mx-auto text-center bg-white border-royal-blue border-4 relative">
                <div class="flex flex-col sm:flex-row items-center">
                    <!--Join Guides Button-->
                    <div :class="['w-1/2 p-6 transition-all duration-300', joinGuides ? 'bg-royal-blue' : '']">
                        <button 
                            @click="toggleJoinGuides"
                            :class="[
                                'px-6 py-2 font-semibold text-lg transition-hover duration-100',
                                joinGuides 
                                    ? 'text-white scale-105' 
                                    : 'text-royal-blue hover:scale-105 hover:[text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)] hover:cursor-pointer'
                            ]"
                        >
                            Join Guides
                        </button>
                    </div>
                    <!--Being a Guide Button-->
                    <div :class="['w-1/2 p-6 transition-all duration-300', beingAGuide ? 'bg-royal-blue' : '']">
                        <button 
                            @click="toggleBeingAGuide"
                            :class="[
                                'px-6 py-2 font-semibold text-lg ransition-hover duration-100',
                                beingAGuide 
                                    ? 'text-white scale-105' 
                                    : 'text-royal-blue hover:[text-shadow:_0px_4px_4px_rgb(0_0_0_/_0.25)] hover:scale-105 hover:cursor-pointer'
                            ]"
                        >
                            Being a Guide
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!--Directions: Join Guides-->
    <section id="join-guides" v-show="joinGuides">

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
                        <span class="font-bold">
                            Info Sessions:
                        </span>
                        We ask that you attend an information session to learn more about the Virginia Guides Service and 
                        speak to current Guides. Attending information and Q&A sessions will help you learn about the try-out process, get tips from current guides, 
                        and learn more about what is expected of UGS members. Information sessions are mandatory and a great way to get your questions 
                        answered and better understand what makes UGS so great! Our general sessions this semester are:
                    </p>
                    <p class="scrollElement font-Roboto text-UVA-orange font-bold text-base sm:text-lg italic">
                        The Rotunda Multipurpose Room is located in the hallway underneath the Rotunda Lawn-side before you enter the building itself.
                    </p>
                    <div class="scrollElement">
                        <h1 class="font-Roboto text-lg sm:text-xl font-bold italic mb-2 pt-5">
                            Step 2: Prepare to Try Out
                        </h1>
                        <p class="font-Roboto font-light text-base sm:text-lg pb-2">
                            For our Fall 2024 recruitment season, you will give a 15 minute historical “trial tour” of the Lawn area to two current Guides 
                            (who will act as your "tourists"). The trial tour is meant to see how well you can craft an organized and meaningful tour, 
                            as well as to assess your public speaking abilities.
                        </p>
                        <p class="font-Roboto font-light text-base sm:text-lg">
                            You will be able to sign up for a time slot between February 3rd through the 7th for your trial tour at one of our 
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
                <p class="font-Roboto text-white text-center text-base sm:text-lg md:text-md">
                    To begin writing, we encourage you to refer to this 
                    <a href="https://docs.google.com/document/d/1SgT3gxmUICInw1gs1LGYnTQ4pzVWFVgJZrtIZ2Z4Mes/edit?usp=sharing" class="underline">
                        historical fact sheet
                    </a> we have put together for you. 
                    Once you have written your tour, we recommend practicing giving your tour before you do so officially. 
                    As you prepare, please reach out to our Recruitment Co-Chairs, 
                    <a href="mailto:gwm6vu@virginia.edu" class="underline">
                        Goretty
                    </a> and 
                    <a href="mailto:tzk9jr@virginia.edu" class="underline">
                        Molly,
                    </a> for any help you may need. 
                    They are equipped to offer you advice on how to go about your tours, suggestions for what to include, 
                    and any help you might need to prepare! The Recruitment Co-Chairs have no say in the selection process, 
                    meaning that you can truly ask them anything - they're here to make sure you have the best possible experience trying out.
                </p>
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

    <!--Directions: Being a Guide-->
    <section v-show="beingAGuide">

        <!--Running Banner: Being A Guide-->
        <div class="scrollElement running-text-container font-[Roboto] font-medium text-[#ECE9E9]">
            <!--First Copy-->
            <ul>
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
            </ul>
            <!--First Copy for seamless animation-->
            <ul aria-hidden="true">
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
                <li>
                    <span class="running-text">BEING A GUIDE&nbsp;</span>
                </li>
            </ul>
        </div>

        <!--College Container 1-->
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-5">
            <!--Collage Section-->
            <!--flex row What We Do Text-->
            <div class="scrollElement flex flex-col lg:flex-row gap-6 pb-5">
                <div class="flex flex-col space-y-1 justify-center text-center lg:text-start">
                    <h2 class="font-['Montserrat'] text-2xl sm:text-3xl font-bold text-black">
                    WHAT WE DO
                    </h2>
                    <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                    Members of the Virginia Guides Service (“Guides”) have the incredible opportunity to serve as keepers of our University's history and to also act as ambassadors of UVA to prospective students and their families. All Guides give historical tours of our University, integrating stories from across our school's 200-year history into a unique and cohesive narrative that speaks to both the Guide and their tourists. Members of Guides give hundreds of tours each semester to prospective and current students, faculty and staff, alumni, community members, and visitors from all across the world!    </p>
                </div>
            </div>

            <!--first flex row-->
            <div class="flex flex-col lg:flex-row gap-x-10">

                <!--flex col-->
                <div class="flex flex-col w-full lg:w-[60%] gap-x-10 gap-y-5 justify-center items-center">
                    <!-- Why We Do It Text -->
                    <div class="scrollElement flex flex-col w-full space-y-1 text-center lg:text-start">
                        <h2 class="font-['Montserrat'] text-2xl sm:text-3xl font-bold text-black">
                            WHY WE DO IT
                        </h2>
                        <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                            Guides come from all around the world, across all the schools at UVA, and from any program of study. 
                            We are involved in many different groups, organizations, and clubs at the University, but what brings us together 
                            is our love for giving tours and connecting with others through the history of UVA. Each Guide joins for their own 
                            reasons—whether it's a passion for storytelling, a desire to welcome 
                            share history, or simply a love for this University—but together we form a community that is 
                            meaningful, supportive, and lasting; a community that members love to be a part of. Being a Guide is 
                            about more than just walking tours; it's about creating a community that reaches far beyond what you might expect.
                        
                        </p>
                    </div>
                    <!-- Img + the honor of representing UVA with hover overlay -->
                    <div class="scrollElement relative flex flex-col lg:flex-row w-[80%] lg:w-full gap-x-5 items-center justify-center p-2 bg-royal-blue text-center lg:text-start">
                        
                        <!-- Image with overlay -->
                        <div class="relative group flex flex-col w-full lg:w-1/2 justify-center items-center">
                            <img 
                                src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/beingaguide_mtnview.png" 
                                class="object-cover w-full max-w-xs md:max-w-sm lg:max-w-md p-2 transition duration-500 filter group-hover:opacity-50"
                                loading="lazy"
                            >
                            
                            <!-- Overlay Text -->
                            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
                                        text-center text-white text-lg font-Roboto font-semibold max-w-7xl mx-auto 
                                        opacity-0 transition duration-500 group-hover:opacity-100 px-2">
                                Guides enjoying the view!
                            </div>
                        </div>

                        <!-- Text -->
                        <div class="flex flex-col w-full lg:w-1/2 space-y-1 p-2">
                            <h2 class="uppercase font-['Montserrat'] text-xl sm:text-2xl font-bold text-white">
                                The Honor of Representing UVA
                            </h2>
                            <p class="font-Roboto text-base sm:text-lg leading-relaxed text-white">
                                The opportunity to serve as the "face of UVA" to so many visitors leaves an indelible impact on our Guides and to the visitors that they have the privilege of interacting with.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Image -->
                <div class="scrollElement relative group flex flex-col w-full lg:w-[40%] justify-center items-center pt-5 lg:pt-0">
                    <!-- Image -->
                    <div class="p-2 border-4 border-dotted border-dark-green">
                        <img 
                            src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/4girls.JPEG" 
                            class="object-cover w-full max-w-2xs md:max-wxs lg:max-w-sm transition duration-400 group-hover:opacity-30"
                            loading="lazy"
                        >
                    </div>

                    <!-- Overlay Text -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 
                                items-center justify-center text-center 
                                text-black text-lg font-Roboto font-semibold max-w-7xl mx-auto opacity-0 transition duration-500 
                                group-hover:opacity-100">
                        Guides make the most of golden hour on Carter's Mountain
                    </div>
                </div>
            </div>

            <!--second flex row-->
            <div class="flex flex-col lg:flex-row py-5 gap-5">
                <!--Text-->
                <div class="flex flex-col w-full lg:w-[35%] space-y-1 items-center justify-center">
                    <div class="scrollElement p-5 border-4 border-dark-green text-center lg:text-start">
                        <h2 class="uppercase font-['Montserrat'] text-xl sm:text-2xl font-bold text-black">
                            Collaboration Across Grounds
                        </h2>
                        <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                            Collaborate with other organizations across Grounds to spread a passion for and understanding of our University's multi-faceted history. For example, we have worked with other organizations and students on Grounds to establish the History of Enslaved African American Laborers (HEAAL) tour for first years to learn about the University’s history.
                        </p>
                    </div>
                </div>
                <!-- Image-->
                <div class="scrollElement relative group flex flex-col w-full lg:w-[30%] items-center justify-center">
                    <!-- Image -->
                    <div class="p-2 bg-dark-green ">
                        <img 
                            src="https://virginia-guides-website-images.s3.amazonaws.com/public/join-guides-page/beingaguide_metthebanner.jpeg" 
                            class="object-cover w-full max-w-3xs md:max-w-2xs lg:max-w-xs transition duration-500 filter group-hover:opacity-50"
                            loading="lazy"
                        >
                    </div>

                    <!-- Overlay Text -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
                                text-center text-white text-lg font-Roboto font-semibold max-w-7xl mx-auto 
                                opacity-0 transition duration-500 group-hover:opacity-100 px-2">
                        Our Guides Banner waiting to be signed by our probie groups
                    </div>
                </div>

                <!--Text-->
                <div class="scrollElement flex flex-col w-full lg:w-[35%] space-y-1 items-center justify-center">
                    <div class="p-5 border-4 border-dark-green text-center lg:text-start">
                        <h2 class="uppercase font-['Montserrat'] text-xl sm:text-2xl font-bold text-black">
                            Exploring HISTORY That Matters To You
                        </h2>
                        <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                            Dive into a topic of history that very specifically speaks to you. Some of our members have chosen to do deeper research and work relating to topics such as the history of women, the history of Asian Americans, LGBTQ+ history, the history of African Americans, and the history of medicine at UVA.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!--Carousel-->
        <div class="scrollElement about-carousel-body">
            <div class="about-slider">
                <div class="about-slide-track">
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/gpcar.JPEG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/phoneinception.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/bamboo.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/lawnroom.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/grouphoto.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/lawn2.JPEG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/meetthe.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/formal.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/cookout.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/yellow.JPG" loading="lazy" alt="">
                    </div>
                    <!--Same 10 slides (doubled)-->
                    <div class="about-slide flex flex-col justify-start">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/gpcar.JPEG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img object-top" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/phoneinception.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/bamboo.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/lawnroom.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/grouphoto.jpeg" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/lawn2.JPEG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/meetthe.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/formal.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/cookout.JPG" loading="lazy" alt="">
                    </div>
                    <div class="about-slide flex flex-col">
                        <img class="about-carousel-img" src="https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/join-guides-page/yellow.JPG" loading="lazy" alt="">
                    </div>
                </div>
            </div>
        </div>

        <!--College Container 2-->
        <div class="container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-5 pb-12">
            <!--third flex row-->
            <div class="flex flex-col lg:flex-row gap-5">
                <!--Image-->
                <div class="scrollElement relative group flex flex-col w-full lg:w-1/2 items-center justify-center">
                    <div class=" p-2 border-4 border-dotted border-dark-green">
                        <img
                            src="/join-guides-page/beingaguide_metthepicnic.jpg" 
                            class="object-cover w-full max-w-sm md:max-w-md lg:max-w-lg transition duration-400 group-hover:opacity-30"
                            loading="lazy"
                        >
                    </div>
                    <!-- Overlay Text -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 
                                items-center justify-center text-center 
                                text-black text-lg font-Roboto font-semibold max-w-7xl mx-auto opacity-0 transition duration-500 
                                group-hover:opacity-100">
                        Guides enjoy the sunset with a picnic on the lawn 
                    </div>
                </div>

                <!--Text-->
                <div class="scrollElement flex flex-col w-full lg:w-1/2 space-y-1 justify-center text-center lg:text-start">
                    <div class="p-10 text-white bg-royal-blue">
                        <h2 class="uppercase font-['Montserrat'] text-xl sm:text-2xl font-bold">
                            The Colonnades Ball
                        </h2>
                        <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                            Attend the unforgettable Colonnades Ball! Virginia Guides hosts the Colonnades Ball, a formal event for the University and Charlottesville community to raise money to support the community around us. The event is open for anyone to attend, but is a wonderful way for all the Guides to get together and dress up for a good cause.
                        </p>
                    </div>
                </div>
            </div>

            <!--fourth flex row-->
            <div class="flex flex-col lg:flex-row gap-x-5 pt-5">
                <!-- Manmayi and Mercy Image with Overlay -->
                <div class="scrollElement relative group flex flex-col w-full lg:w-[35%] justify-center items-center mb-5 lg:mb-0">
                    <!-- Image -->
                    <div class="p-3 border-4 border-UVA-orange ">
                        <img 
                            src="/join-guides-page/manmayiandmercy.JPEG" 
                            class="object-cover w-full max-w-xs md:max-w-sm lg:max-w-mdtransition duration-400 group-hover:opacity-30"
                            loading="lazy"
                        >

                        <!-- Overlay Text -->
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 
                                    items-center justify-center text-center 
                                    text-black text-lg font-Roboto font-semibold max-w-7xl mx-auto opacity-0 transition duration-500 
                                    group-hover:opacity-100">
                            Guides sharing a hug on top of Carter's Mountain
                        </div>
                    </div>
                </div>
                <!--Text-->
                <div class="scrollElement flex flex-col w-full lg:w-[30%] space-y-1 p-5 justify-center bg-UVA-orange text-white text-center lg:text-start">
                    <h2 class="uppercase font-['Montserrat'] text-xl sm:text-2xl font-bold">
                        Friendships Beyond Grounds
                    </h2>
                    <p class="font-Roboto text-base sm:text-lg leading-relaxed">
                        Develop friendships that last a lifetime. So many of our members have found best friends, mentors, roommates, or even just a friendly face in class. Virginia Guides feels like a family to us all and the relationships we make here last us for years beyond our time on Grounds.
                    </p>
                </div>
                <!-- Yukta and Sanjitha Image with Overlay -->
                <div class="scrollElement relative group flex flex-col w-full lg:w-[35%] justify-center items-center mt-5 lg:mt-0">
                    <!-- Image -->
                    <div class="p-3 border-4 border-UVA-orange ">
                        <img 
                            src="/join-guides-page/yuktaandsanjitha.jpeg" 
                            class="object-cover w-full max-w-xs md:max-w-sm lg:max-w-md transition duration-400 group-hover:opacity-30"
                            loading="lazy"
                        >
                    </div>

                    <!-- Overlay Text -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 
                                items-center justify-center text-center 
                                text-black text-lg font-Roboto font-semibold max-w-7xl mx-auto opacity-0 transition duration-500 
                                group-hover:opacity-100">
                        Guides enjoying each other's company
                    </div>
                </div>
            </div>
        </div>

        <!--Running Banner #2-->
        <div class="scrollElement running-text-container font-[Roboto] font-medium text-[#ECE9E9] pb-12">
            <!--First Copy-->
            <ul>
                <li>
                    <span class="uppercase running-text">Join a community that goes back decades and now eagerly awaits to welcome you too!&nbsp;</span>
                </li>
            </ul>
            <!--First Copy for seamless animation-->
            <ul aria-hidden="true">
                <li>
                    <span class="uppercase running-text">Join a community that goes back decades and now eagerly awaits to welcome you too!&nbsp;</span>
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
    }

    @keyframes text-scroll {
        to {
            transform: translateX(calc(-100% - var( --gap)));
        }
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