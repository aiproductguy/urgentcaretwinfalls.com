<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">{{ title }}</h2>
    
    <div class="space-y-6">
      <!-- Address Section -->
      <div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
          <IconifyIcon icon="mdi:map-marker" class="text-xl text-primary-500" />Address
        </h3>
        <p class="mt-2 text-gray-600 dark:text-gray-300">
          {{ contact.address.street }}<br />
          {{ contact.address.city }}, {{ contact.address.state }} {{ contact.address.zip }}
        </p>
      </div>

      <!-- Hours Section -->
      <div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
          <IconifyIcon icon="mdi:clock" class="text-xl text-primary-500" />Hours of Operation
        </h3>
        <div class="mt-2 text-gray-600 dark:text-gray-300">
          <template v-if="useShortSchedule">
            <p>{{ hours.shortSchedule }}</p>
          </template>
          <template v-else>
            <div v-for="schedule in hours.longSchedule" :key="schedule" class="mb-1">
              {{ schedule }}
            </div>
          </template>
          <p class="text-sm italic mt-2">{{ hours.holidays }}</p>
          <p class="text-sm mt-2" :class="isOpen() ? 'text-green-600' : 'text-red-600'">
            Currently {{ isOpen() ? 'Open' : 'Closed' }}
          </p>
        </div>
      </div>

      <!-- Contact Section -->
      <div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-white flex items-center gap-2">
          <IconifyIcon icon="mdi:phone" class="text-xl text-primary-500" />Contact
        </h3>
        <div class="mt-2 text-gray-600 dark:text-gray-300">
          <p>Phone: {{ contact.phone }}</p>
          <p class="flex items-center gap-2">
            <IconifyIcon icon="mdi:email" class="text-xl text-primary-500" />
            {{ contact.email }}
          </p>
        </div>
      </div>

      <!-- Call Button -->
      <div class="pt-6">
        <a
          :href="'tel:' + contact.phone.replace(/\D/g, '')"
          class="inline-flex items-center gap-2 px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
        >
          <IconifyIcon icon="mdi:phone" class="text-xl" />Call Now
        </a>
        <p class="mt-4 font-semibold">For medical emergencies, please call 911</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'

const props = defineProps({
  title: {
    type: String,
    default: 'Contact Information'
  },
  useShortSchedule: {
    type: Boolean,
    default: false
  }
})

const { contact, hours, isOpen } = useClinicInfo()
</script> 