// https://nuxt.com/docs/api/configuration/nuxt-config

import tailwindcss from "@tailwindcss/vite";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['../assets/css/main.css'],
  modules: ['@nuxt/image', '@nuxt/fonts'],
  // backend: django
  runtimeConfig: {
    public: {
      // http://127.0.0.1:8000
      // https://guides-website-backend-1.onrender.com
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000'
      // apiBase: process.env.NUXT_PUBLIC_API_BASE
      // apiBase: 'http://127.0.0.1:8000' // USE THIS FOR LOCAL DEV !!!!
    }
  },
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  app: {
    head: {
      link: [
        { rel: 'icon', type: 'image/png', href: 'https://virginia-guides-website-images.s3.us-east-2.amazonaws.com/public/favicon.png' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;600;700;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap' }
      ]
    }
  }  
})
