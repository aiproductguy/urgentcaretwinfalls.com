<template>
  <NuxtLayout>
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
            :src="googleMapsUrl"
            width="100%"
            height="450"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>

        <!-- Contact Information -->
        <ContactCard title="Contact Information" :use-short-schedule="true" />
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
  </NuxtLayout>
</template>

<script setup>
const { contact, googleMapsUrl } = useClinicInfo()

useHead({
  title: 'Location | Urgent Care Twin Falls',
  meta: [
    {
      name: 'description',
      content: `Visit us at 260 Falls Avenue Suite D, Twin Falls, Idaho. Open Monday through Friday, 8:00 AM - 5:00 PM. Call ${contact.phone} for appointments or walk in today.`
    }
  ]
})

definePageMeta({
  layout: 'default'
})
</script> 