<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
    <h2 class="text-3xl font-bold text-gray-900 dark:text-white mb-8">Why Choose Us?</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div v-for="(feature, index) in features" :key="index" class="flex items-start gap-4">
        <Icon :icon="feature.icon" class="w-8 h-8 text-blue-600 dark:text-blue-400 flex-shrink-0" />
        <div>
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">{{ feature.title }}</h3>
          <p class="text-gray-600 dark:text-gray-300">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'

const features = [
  {
    title: 'Short Wait Times',
    description: 'Most patients are seen within 30 minutes of arrival.',
    icon: 'mdi:timer-outline'
  },
  {
    title: 'Experienced Staff',
    description: 'Our medical professionals have years of emergency and urgent care experience.',
    icon: 'mdi:medical-bag'
  },
  {
    title: 'Modern Facility',
    description: 'State-of-the-art medical equipment and comfortable environment.',
    icon: 'mdi:hospital-building'
  },
  {
    title: 'Affordable Care',
    description: 'We accept most insurance plans and offer competitive self-pay rates.',
    icon: 'mdi:cash-multiple'
  }
]
</script> 