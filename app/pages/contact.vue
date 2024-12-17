<template>
  <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-8">Contact Us</h1>
      <p class="text-xl text-gray-600 dark:text-gray-300 mb-12">
        We're here to help. Reach out to us with any questions or concerns.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Contact Information -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Get In Touch</h2>
        
        <div class="space-y-6">
          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
              <IconifyIcon icon="mdi:map-marker" class="text-xl text-primary-500" />Address
            </h3>
            <p class="mt-2 text-gray-600 dark:text-gray-300">
              260 Falls Avenue, Suite C<br />
              Twin Falls, ID 83301
            </p>
          </div>

          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
              <IconifyIcon icon="mdi:clock" class="text-xl text-primary-500" />Hours of Operation
            </h3>
            <div class="mt-2 text-gray-600 dark:text-gray-300">
              <p>Monday - Friday: 8:00 AM - 5:00 PM</p>
              <p class="text-sm italic">Closed on weekends and major holidays</p>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
              <IconifyIcon icon="mdi:phone" class="text-xl text-primary-500" />Contact
            </h3>
            <div class="mt-2 text-gray-600 dark:text-gray-300">
              <p>Phone: (208) 733-6700</p>
              <p class="flex items-center gap-2">
                <IconifyIcon icon="mdi:email" class="text-xl text-primary-500" />
                info@urgentcaretwinfalls.com
              </p>
            </div>
          </div>

          <div class="pt-6">
            <a
              href="tel:+12087336700"
              class="inline-flex items-center gap-2 px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              <IconifyIcon icon="mdi:phone" class="text-xl" />Call Now 📞
            </a>
          </div>
        </div>

        <!-- Social Media Links -->
        <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700">
          <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2 mb-4">
            <IconifyIcon icon="mdi:share-variant" class="text-xl text-primary-500" />Follow Us
          </h3>
          <div class="flex space-x-4">
            <a href="#" class="text-primary-500 hover:text-primary-600 transition-colors">
              <IconifyIcon icon="mdi:facebook" class="w-6 h-6" />
            </a>
            <a href="#" class="text-primary-500 hover:text-primary-600 transition-colors">
              <IconifyIcon icon="mdi:twitter" class="w-6 h-6" />
            </a>
            <a href="#" class="text-primary-500 hover:text-primary-600 transition-colors">
              <IconifyIcon icon="mdi:instagram" class="w-6 h-6" />
            </a>
          </div>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Send Us a Message</h2>
        <form class="space-y-6">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Name</label>
            <input
              type="text"
              name="name"
              id="name"
              class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm focus:border-blue-500 focus:ring-blue-500"
              required
            />
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email</label>
            <input
              type="email"
              name="email"
              id="email"
              class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm focus:border-blue-500 focus:ring-blue-500"
              required
            />
          </div>

          <div>
            <label for="phone" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Phone</label>
            <input
              type="tel"
              name="phone"
              id="phone"
              class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>

          <div>
            <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Message</label>
            <textarea
              name="message"
              id="message"
              rows="4"
              class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm focus:border-blue-500 focus:ring-blue-500"
              required
            ></textarea>
          </div>

          <div class="text-sm text-gray-600 dark:text-gray-400">
            <p>* For medical emergencies, please call 911</p>
          </div>

          <button
            type="submit"
            class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            Send Message
          </button>
        </form>
      </div>
    </div>

    <!-- Map -->
    <div class="mt-12 bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2937.9623927753546!2d-114.47637859999999!3d42.5773207!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54aca2457605db65%3A0x24920c41025270b7!2s260%20Falls%20Ave%2C%20Twin%20Falls%2C%20ID%2083301!5e0!3m2!1sen!2sus!4v1726347046896!5m2!1sen!2sus"
        width="100%"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'

useHead({
  title: 'Contact Us | Urgent Care of Twin Falls',
  meta: [
    {
      name: 'description',
      content: 'Contact Urgent Care of Twin Falls at (208) 733-6700 or visit us at 260 Falls Avenue, Suite C. Open Monday through Friday, 8:00 AM - 5:00 PM.'
    }
  ]
})
</script> 