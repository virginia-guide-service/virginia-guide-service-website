// https://nuxt.com/docs/api/configuration/nuxt-config

import tailwindcss from "@tailwindcss/vite";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['../assets/css/main.css'],
  modules: ['@nuxt/image', '@nuxt/fonts'],
  // backend settings for django
  runtimeConfig: {
    public: {
      // allow api to work on the product and development sites -- env variables can be found in vercel
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000'
      // apiBase: process.env.NUXT_PUBLIC_API_BASE // use for production only 
      // apiBase: 'http://127.0.0.1:8000' // use for local development only (development branch)
    }
  },
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  tailwindcss: {
    config: {
      theme: {
        extend: {
          fontFamily: {
            montserrat: ['Montserrat', 'sans-serif'],
          }
        }
      }
    }
  },
  app: {
    head: {
      link: [
        {
          // Favicon is the browser tab icon
          // If you want to change it, upload a new image in AWS and repalce the href link with the new object URL
          rel: 'icon',
          type: 'image/png',
          href: 'https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/favicon.png'
        },
        {
          // Importing fonts used throughout the website (Roboto, Playfair Display, Montserrat)
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:wght@300;400;500;600;700;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap'
        }
      ],
  
      meta: [
        // Basic meta
        // The meta section is relevant for sending links of the website 
        {
          name: 'description',
          content: 'Student-led historical tours of the University of Virginia.'
        },
  
        // Open Graph (for Facebook, iMessage, Discord, Slack, LinkedIn)
        // e.g. sending a link through iMessage shows the title "Virginia Guides", cover image that's given under the image property, sends users 
        // to the url given under the url property, and categorizes the link as a website
        {
          property: 'og:title',
          content: 'Virginia Guides'
        },
        {
          property: 'og:description',
          content: 'Student-led historical tours of the University of Virginia.'
        },
        {
          property: 'og:image',
          content: 'https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/thumbnail.PNG'
        },
        {
          property: 'og:url',
          content: 'https://virginiaguides.org'
        },
        {
          property: 'og:type',
          content: 'website'
        },
  
        // Twitter / X
        {
          name: 'twitter:card',
          content: 'summary_large_image'
        },
        {
          name: 'twitter:title',
          content: 'Virginia Guides'
        },
        {
          name: 'twitter:description',
          content: 'Student-led historical tours of the University of Virginia.'
        },
        {
          name: 'twitter:image',
          content: 'https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/thumbnail.PNG'
        }
      ]
    }
  }  
})
