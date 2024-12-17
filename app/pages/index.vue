<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
    <main class="container mx-auto px-4">
      <!-- Hero Section -->
      <section class="hero my-24">
        <div class="container">
          <div class="grid grid-cols-1 items-center gap-24 lg:grid-cols-2">
            <div class="flex flex-col items-center gap-8 md:items-start">
              <h1 class="text-center text-4xl md:text-left lg:text-8xl">
                <span class="text-gradient">Urgent Care</span> <span class="text-4xl">of</span> Twin Falls
              </h1>
              <p class="text-xl text-center md:text-left">
                Providing compassionate and efficient care when you need it most. Visit us today or call (208) 733-6700 for immediate assistance.
                <i>(Formerly Falls Avenue Immediate Care)</i>
              </p>
              <div class="flex flex-col gap-3 min-[500px]:flex-row">
                <a class="button primary flex items-center justify-center gap-2" href="tel:2087336700">
                  <Icon icon="mdi:phone" />Call Now
                </a>
                <a class="button secondary flex items-center justify-center gap-2" href="#location">
                  <Icon icon="mdi:map-marker" />Get Directions
                </a>
                <img class="floatingImg" src="/best-award-2023.png" width="150px" alt="Winners badge 2022 Idahos best Statewide winner">
              </div>
            </div>
            <img class="hidden lg:block" src="/location-front.png" alt="Urgent Care of Twin Falls Facility" decoding="async" />
          </div>
        </div>
      </section>

      <!-- Services Section -->
      <section class="my-64">
        <div class="container">
          <h2 class="mb-16 text-6xl">Our Services</h2>
          <div class="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-3">
            <Feature icon="mdi:hospital-building" title="Injuries">
              Ready to assist with sprains, fractures, burns, and more to help you recover quickly.
            </Feature>
            <Feature icon="mdi:thermometer-lines" title="Illness Treatment">
              Effective treatment for colds, flu, fevers, and more, ensuring your health is promptly restored.
            </Feature>
            <Feature icon="mdi:stethoscope" title="Diagnostic Services">
              In-house diagnostic tests for a quick and accurate understanding of your health concerns.
            </Feature>
            <Feature icon="mdi:clipboard-pulse" title="Physicals & Wellness Checkups">
              Stay protected with comprehensive physicals and regular wellness checkups for optimal health.
            </Feature>
            <Feature icon="mdi:radiology-box" title="X-ray & Imaging Services">
              Advanced X-ray and imaging services to provide detailed insights for accurate diagnoses.
            </Feature>
            <Feature icon="mdi:office-chair" title="Work-Related Medical">
              Occupational health services including pre-employment screenings and work injury treatment.
            </Feature>
          </div>
        </div>
      </section>

      <!-- Team Section -->
      <section class="my-64">
        <div class="container">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 class="text-4xl mb-8">Meet Our Caring Team</h2>
              <p class="text-2xl">
                Led by Dr. David Christensen and Chuck Davis, our team is dedicated to providing expert and compassionate care.
              </p>
            </div>
            <img src="/Dr-DC-with-Patient.png" alt="Dr. David Christensen with Patient" class="rounded-lg shadow-xl" />
          </div>
        </div>
      </section>

      <!-- Location Section -->
      <section id="location" class="my-64">
        <div class="container">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <img src="/location-front.png" alt="Urgent Care Twin Falls Location" class="rounded-lg shadow-xl order-2 lg:order-1" />
            <div class="order-1 lg:order-2">
              <h2 class="text-4xl mb-8">Where to Find Us</h2>
              <p class="text-2xl">
                Conveniently located at 260 Falls Avenue, Twin Falls, Idaho.<br>
                Open Monday through Friday, 8:00 am – 5:00 pm.
              </p>
              <iframe 
                class="w-full h-[400px] mt-8 rounded-lg"
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2937.9623927753546!2d-114.47637859999999!3d42.5773207!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54aca2457605db65%3A0x24920c41025270b7!2s260%20Falls%20Ave%2C%20Twin%20Falls%2C%20ID%2083301!5e0!3m2!1sen!2sus!4v1726347046896!5m2!1sen!2sus"
                style="border:0;"
                allowfullscreen=""
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
              ></iframe>
            </div>
          </div>
        </div>
      </section>

      <!-- Why Choose Us Section -->
      <section class="mb-32 mt-64">
        <div class="container">
          <h2 class="mb-16 text-6xl">Why Choose Us?</h2>
          <div class="grid grid-cols-1 gap-12 sm:grid-cols-2 md:grid-cols-4">
            <Counter count="15+" title="Years of Experience" sub="Trusted Healthcare" />
            <Counter count="Original" title="Local Legacy" sub="First Urgent Care in Twin Falls" />
            <Counter count="Mon-Fri" title="Availability" sub="8am-5pm Walk-ins & Appointments" />
            <Counter count="High" title="Satisfaction Rate" sub="Patient Feedback" />
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'
import Feature from '~/components/Feature.vue'
import Counter from '~/components/Counter.vue'

useHead({
  title: 'Twin Falls Urgent Care - Quick & Professional Medical Care',
  meta: [
    {
      name: 'description',
      content: 'Twin Falls Urgent Care provides immediate medical attention for non-emergency conditions. Walk-ins welcome, short wait times, and experienced medical staff.'
    },
    {
      name: 'keywords',
      content: 'urgent care twin falls, walk-in clinic, immediate care, medical services, twin falls healthcare'
    }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "MedicalOrganization",
        "name": "Twin Falls Urgent Care",
        "url": "https://urgentcaretwinfallscom.netlify.app",
        "telephone": "+1-208-733-6700",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "260 Falls Avenue",
          "addressLocality": "Twin Falls",
          "addressRegion": "ID",
          "postalCode": "83301",
          "addressCountry": "US"
        },
        "openingHours": "Mo,Tu,We,Th,Fr 08:00-17:00",
        "medicalSpecialty": ["Urgent Care", "Family Medicine"],
        "availableService": [
          "Minor Injuries Treatment",
          "Illness Care",
          "Physical Examinations",
          "Diagnostic Services",
          "X-ray Services"
        ]
      })
    }
  ]
})
</script>

<style>
.text-gradient {
  background: linear-gradient(315deg, var(--primary-200) 25%, var(--secondary-500));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.button {
  @apply px-6 py-3 rounded-lg font-medium transition-colors duration-200;
}

.button.primary {
  @apply bg-blue-600 text-white hover:bg-blue-700;
}

.button.secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600;
}

.floatingImg {
  @apply absolute -top-20 right-0 md:right-20 animate-bounce;
}

:root {
  --primary-200: #60a5fa;
  --secondary-500: #3b82f6;
  --secondary-400: #60a5fa;
}

.dark {
  --primary-200: #93c5fd;
  --secondary-400: #60a5fa;
}
</style> 