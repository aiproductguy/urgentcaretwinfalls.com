<template>
  <div class="counter text-center p-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg border-2 border-gray-100 dark:border-gray-700">
    <div class="text-4xl font-bold text-blue-600 dark:text-blue-400 mb-2">{{ count }}</div>
    <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-1">{{ title }}</h3>
    <p class="text-gray-600 dark:text-gray-300">{{ sub }}</p>
  </div>
</template>

<script setup>
defineProps({
  count: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  sub: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.counter {
  transition: transform 0.2s ease-in-out;
}

.counter:hover {
  transform: scale(1.05);
}
</style> 