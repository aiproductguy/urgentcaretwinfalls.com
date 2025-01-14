<template>
  <NuxtLayout>
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
      <div class="text-center">
        <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-8">About Us</h1>
        <p class="text-xl text-gray-600 dark:text-gray-300 mb-12">
          Your Trusted Partner in Health – Urgent Care of Twin Falls
        </p>
      </div>

      <!-- Mission Statement -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Our Mission</h2>
        <div class="prose prose-blue dark:prose-invert max-w-none">
          <p class="text-lg text-gray-600 dark:text-gray-300">
            At Urgent Care of Twin Falls, we know that when life throws you a curveball with sudden illness or injury, 
            quick and reliable care makes all the difference. That's why we're here to provide the high-quality, 
            compassionate care you deserve, right here in your community.
          </p>
          <p class="text-lg mt-4 text-gray-600 dark:text-gray-300">
            Whether it's a minor injury, seasonal illness, or the need for an urgent vaccination, our team of 
            experienced healthcare professionals is dedicated to helping you get back on your feet as quickly as possible.
          </p>
        </div>
      </div>

      <!-- Meet Our Team -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Meet Our Caring Team</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="space-y-4">
            <NuxtImg 
              src="/Dr-DC-with-Patient.png" 
              alt="Dr. David Christensen with Patient" 
              class="rounded-lg shadow-xl w-full h-auto"
            />
            <h3 class="text-xl font-bold text-gray-900 dark:text-white">Dr. David Christensen, MD</h3>
            <p class="text-gray-600 dark:text-gray-300">
              A native of Idaho, Dr. Christensen completed his medical doctorate from the University of Washington 
              School of Medicine. With extensive experience in family and urgent care, he leads our team with a 
              deep commitment to patient-centered care.
            </p>
          </div>
          <div class="space-y-4">
            <div class="bg-gray-100 dark:bg-gray-700 rounded-lg aspect-video flex items-center justify-center">
              <Icon icon="mdi:account-group" class="w-24 h-24 text-gray-400 dark:text-gray-500" />
            </div>
            <h3 class="text-xl font-bold text-gray-900 dark:text-white">Our Medical Team</h3>
            <p class="text-gray-600 dark:text-gray-300">
              Our dedicated healthcare professionals bring years of experience in urgent care 
              and patient service. Their commitment to providing excellent care makes them invaluable members 
              of our team.
            </p>
          </div>
        </div>
      </div>

      <!-- Why Choose Us -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Why Choose Us?</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">15+</div>
            <div class="font-semibold text-gray-900 dark:text-white">Years of Experience</div>
            <div class="text-sm text-gray-600 dark:text-gray-300">Trusted Healthcare</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">Original</div>
            <div class="font-semibold text-gray-900 dark:text-white">Local Legacy</div>
            <div class="text-sm text-gray-600 dark:text-gray-300">First Urgent Care in Twin Falls</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">Mon-Fri</div>
            <div class="font-semibold text-gray-900 dark:text-white">Availability</div>
            <div class="text-sm text-gray-600 dark:text-gray-300">8am-5pm Walk-ins & Appointments</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">High</div>
            <div class="font-semibold text-gray-900 dark:text-white">Satisfaction Rate</div>
            <div class="text-sm text-gray-600 dark:text-gray-300">Patient Feedback</div>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { Icon } from '@iconify/vue'

useHead({
  title: 'About Us | Urgent Care of Twin Falls',
  meta: [
    {
      name: 'description',
      content: 'Learn about our experienced medical team at Urgent Care of Twin Falls. Led by Dr. David Christensen, we provide compassionate, expert care when you need it most.'
    }
  ]
})

definePageMeta({
  layout: 'default'
})
</script> 