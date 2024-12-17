<template>
  <NuxtLink :to="link" class="service-card block">
    <div class="h-full p-8 bg-white dark:bg-gray-800 rounded-xl shadow-lg border-2 border-gray-100 dark:border-gray-700 transition-all duration-200 hover:shadow-xl hover:-translate-y-1">
      <Icon :name="icon" class="w-12 h-12 text-blue-600 dark:text-blue-400 mb-4" />
      <h3 class="text-2xl font-semibold text-gray-900 dark:text-white mb-4">{{ title }}</h3>
      <p class="text-gray-600 dark:text-gray-300">{{ description }}</p>
      <div class="mt-6 flex items-center text-blue-600 dark:text-blue-400 font-medium">
        Learn more
        <Icon name="mdi:arrow-right" class="w-5 h-5 ml-2" />
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
import { Icon } from '@iconify/vue'

defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  },
  link: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.service-card {
  text-decoration: none;
}
</style> 