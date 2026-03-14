<template>
  <div class="review-carousel-container bg-white py-16">
    <div class="review-slider">
      <div class="review-slide-track">
        
        <div v-for="n in 2" :key="n" class="review-group">
          
          <div v-for="(review, index) in reviews" :key="index" class="review-card">
            
            <div class="review-card-header">
              <span class="review-date">{{ review.date }}</span>
            </div>
            
            <span class="layered-quote">“</span>
            
            <div class="review-content">
              <p class="review-body">
                {{ review.text }}
              </p>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
    /**
     * ADD REVIEW SECTION
     * You can add as much text as you want. 
     * The cards will automatically expand to fit the longest review.
     */
    const reviews = [
    { 
        date: "Jan 2024", 
        text: "[Guide name]—he was so well informed and thoughtful in explaining the historical relationship to history and the importance of understanding it in the present." 
    },
    { 
        date: "Feb 2024", 
        text: "Well researched presentation. She did a great job putting various events onto a timeline, which in turned helped to explain the contemporary mindset. She also communicated her love of the university."
    },
    { 
        date: "Feb 2024", 
        text: "I was very impressed with how well the event was organized. I reached out in January when most students were still on break and got a response within 2 days! It was a real pleasure to see such professionalism coming from young people! Bravo and thank you for all you do."
    },
    { 
        date: "Feb 2024", 
        text: "Our tour guide, [guide], was incredibly knowledgeable and engaging. We learned a lot about UVA, Charlottesville, and Virginia through her fantastic storytelling." 
    },
    { 
        date: "Feb 2024", 
        text: "[Guide], the tour guide, was knowledgeable, enthusiastic, and articulate. The tour itself was well-balanced and managed, in a well-structured way, to cover a variety of interesting subjects."
    },
    { 
        date: "Oct 2025", 
        text: "This critical/complicated understanding and connection to the institutions we come from are so essential to figuring out how we move forward." 
    },
    { 
        date: "Oct 2025", 
        text: "Going to Monticello after UVa was really important and looking back at the Rotunda from Monticello to see how the organization of the house is related to the institution, citizenship, and the nation which makes you really question how these spaces normalized what they stood for."
    },
    { 
        date: "Oct 2025", 
        text: "Thank you for your outstanding tour and extraordinarily generous hospitality. I think our students got a chance to see through your example what an exemplary UVa student sounds like. You also allowed me to reconnect with where I come from. So I can't thank you enough."
    }
    ];
</script>

<style scoped>
    .review-carousel-container {
        width: 100%;
        overflow: hidden;
    }

    .review-slider {
        width: 100%;
        display: flex;
        /* Align cards to the top of the container */
        align-items: flex-start; 
    }

    .review-slide-track {
        display: flex;
        width: max-content;
        /* 60s is slower than before to allow reading full text */
        animation: scroll-review 60s linear infinite;
    }

    .review-slide-track:hover {
        animation-play-state: paused;
    }

    .review-group {
        display: flex;
        /* stretch makes all cards in a row the same height as the tallest one */
        align-items: stretch;
        gap: 1.5rem;
        padding-right: 1.5rem;
    }

    .review-card {
        width: 400px;
        min-height: 250px;
        background: #ffffff;
        padding: 2.5rem;
        position: relative; 
        display: flex;
        flex-direction: column;
        border: 1px solid #f0f0f0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }

    .review-card:hover {
        border-color: #E57200;
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }

    .review-card-header {
        display: flex;
        justify-content: flex-end; 
        margin-bottom: 1rem;
    }

    .review-date {
        font-family: 'Montserrat', sans-serif;
        font-size: .95rem;
        font-weight: 700;
        color: #999;
        text-transform: uppercase;
        z-index: 2;
    }

    .layered-quote {
        position: absolute;
        top: 15px;
        left: 10px;
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        color: #E57200;
        opacity: 0.75;
        line-height: 1;
        pointer-events: none;
        z-index: 1; 
    }

    .review-body {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        line-height: 1.8; /* Increased line-height for better readability of long text */
        color: #333;
        position: relative;
        z-index: 2;
    }

    /* === Responsive overrides === */
    /* Tablet (640px – 1023px) */
    @media (max-width: 1023px) {
        .review-card { width: 320px; padding: 2rem; }
    }
    /* Mobile (< 640px) */
    @media (max-width: 639px) {
        .review-card { 
            width: 280px; 
            min-height: 200px; 
            padding: 1.5rem; 
        }
        .review-body { font-size: 0.9rem; line-height: 1.6; }
        .layered-quote { font-size: 4rem; top: 10px; }
    }

    @keyframes scroll-review {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
</style>
