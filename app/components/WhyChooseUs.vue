<template>
  <div class="container">
    <h2 class="mb-16 text-6xl">Why Choose Us?</h2>
    
    <!-- Features Grid -->
    <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:account-group" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">50+ Years Experience</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Over five decades of combined experience in emergency and urgent care services.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:medal" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">First Provider in Twin Falls</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">The original and most trusted urgent care facility in Twin Falls, serving our community first.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:bone" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">Best Bone & Joint Care</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Specialized orthopedic care with direct access to bone and joint treatment experts.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:clock-fast" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">Short Wait Times</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Most patients are seen within 15 minutes of arrival or less.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:calendar-check" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">Walk-ins & Appointments</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Flexible scheduling options - walk in anytime or schedule your visit in advance.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:currency-usd" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">Affordable Care</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">We don't charge an arm and a leg, we fix them. Get urgent care at standard visit rates.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:map-marker" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">Convenient Location</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Easily accessible in Twin Falls with ample parking and a central location.</p>
      </div>

      <div class="feature-card">
        <div class="flex items-center gap-4 mb-2">
          <Icon icon="mdi:thumb-up" class="h-8 w-8 text-blue-600 flex-shrink-0" />
          <h3 class="text-xl font-semibold">High Satisfaction Rate</h3>
        </div>
        <p class="text-gray-600 dark:text-gray-300">Consistently rated highly by our patients for quality care and service excellence.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'
import Counter from '~/components/Counter.vue'
</script>

<style scoped>
.feature-card {
  @apply bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg transition-all hover:shadow-xl;
}
</style> 