<template>
    <!--Footer Section-->
    <section>
        <div class="relative overflow-hidden">

            <!-- Background Image -->
            <NuxtImg 
            src="https://virginia-guides-website-images.s3.amazonaws.com/public/Header_PageFooters.jpg"
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
                        <button class="font-['Roboto'] border-1 border-gray-300 text-white hover:text-royal-blue bg-[rgba(0,0,0,0.30)] hover:bg-gray-100 hover:scale-105 rounded-full py-3 px-10 cursor-pointer transition-all duration-300 ease-in-out">
                            TAKE A TOUR
                        </button>
                    </a>
                    <a href="/donate">
                        <button class="font-['Roboto'] border-1 border-gray-300 text-white hover:text-royal-blue bg-[rgba(0,0,0,0.30)] hover:bg-gray-100 hover:scale-105 rounded-full py-3 px-15 cursor-pointer transition-all duration-300 ease-in-out">
                            DONATE
                        </button>
                    </a>
                </div>

                <!-- Description -->
                <p class="scrollElement mt-20 font-['Roboto'] text-white text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
                    The Virginia Guide Service at UVA is an entirely student-run independent volunteer organization. 
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
                        <a href="your-visit#frequently-asked-questions">
                            <li class="cursor-pointer">Directions + FAQ</li>
                        </a>
                        <a href="about-tours#about-tours">
                            <li class="cursor-pointer">History Tours</li>
                        </a>
                        <a href="/about-tours#specialty-tours">
                            <li class="cursor-pointer">Specialty Tours</li>
                        </a>
                        <a href="/your-visit#times-and-registration">
                            <li class="cursor-pointer">Tour Request</li>
                        </a>
                    </ul>

                    <!-- Column 2 -->
                    <ul class="flex flex-col gap-2 min-w-[100px]">
                        <li class="font-['Playfair_Display'] italic underline text-white text-lg">About Us</li>
                        <a href="/join-guides">
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
                        <a href="/">
                            <li class="cursor-pointer">Home Page</li>
                        </a>
                    </ul>
                </div>

                <!-- Right Side Footer -->
                <div class="scrollElement basis-1/2 flex flex-col gap-3 text-zinc-400 text-sm md:text-base font-light">
                    <div class="flex items-start gap-4 font-['Roboto']">
                        <img class="h-12 w-12 obSject-contain" loading="lazy" src="https://virginia-guides-website-images.s3.amazonaws.com/public/guides-logo.png" alt="Virginia Guides Logo" />
                        <p>
                            The Virginia Guide Service continues 75 years of guiding visitors through UVA in Charlottesville VA. The Guides Service is a 
                            student-run organization independent of the University of Virginia, carrying forward tradition while bringing a more complete light to the past.
                        </p>
                    </div>

                    <div class="flex justify-center md:justify-end">
                        <a href="/contact-us">
                            <button class="border-1 border-gray-300 text-white rounded-full px-6 py-2 font-['Montserrat'] hover:bg-gray-100 hover:scale-105 hover:text-royal-blue transition-all duration-300 ease-in-out cursor-pointer">
                                CONTACT US
                            </button>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>
</template>