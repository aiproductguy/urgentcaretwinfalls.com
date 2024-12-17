<template>
  <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-8">Our Location</h1>
      <p class="text-xl text-gray-600 dark:text-gray-300 mb-12">
        Conveniently located in Twin Falls, Idaho to serve you better
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Map Section -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
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

      <!-- Contact Information -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Contact Information</h2>
        
        <div class="space-y-6">
          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Address</h3>
            <p class="mt-2 text-gray-600 dark:text-gray-300">
              260 Falls Avenue<br />
              Twin Falls, ID 83301
            </p>
          </div>

          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Hours of Operation</h3>
            <div class="mt-2 text-gray-600 dark:text-gray-300">
              <p>Monday - Friday: 8:00 AM - 5:00 PM</p>
              <p class="text-sm italic">Closed on weekends and major holidays</p>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Contact</h3>
            <div class="mt-2 text-gray-600 dark:text-gray-300">
              <p>Phone: (208) 733-6700</p>
              <p>Email: info@urgentcaretwinfalls.com</p>
            </div>
          </div>

          <div class="pt-6">
            <a
              href="tel:+12087336700"
              class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              Call Now
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Additional Information -->
    <div class="mt-12 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Getting Here</h2>
      <div class="prose prose-blue dark:prose-invert max-w-none">
        <p class="text-gray-600 dark:text-gray-300">
          Our urgent care facility is conveniently located in the heart of Twin Falls,
          easily accessible from major roads and highways. We're situated near local
          pharmacies and medical facilities for your convenience.
        </p>
        <h3 class="text-gray-900 dark:text-white">Parking</h3>
        <p class="text-gray-600 dark:text-gray-300">
          Free parking is available in our dedicated lot right in front of the
          building. Handicap accessible spaces are located near the entrance.
        </p>
        <h3 class="text-gray-900 dark:text-white">Public Transportation</h3>
        <p class="text-gray-600 dark:text-gray-300">
          We're accessible via local bus routes with a stop directly in front of
          our facility. For detailed route information, please visit the Twin
          Falls public transportation website.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Location | Urgent Care of Twin Falls',
  meta: [
    {
      name: 'description',
      content: 'Visit us at 260 Falls Avenue, Twin Falls, Idaho. Open Monday through Friday, 8:00 AM - 5:00 PM. Call (208) 733-6700 for appointments or walk in today.'
    }
  ]
})
</script> 