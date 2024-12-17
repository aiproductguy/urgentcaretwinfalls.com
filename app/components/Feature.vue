<template>
  <div class="feature flex flex-col gap-4 relative p-8 rounded-xl bg-white dark:bg-gray-800 shadow-lg border-2 border-gray-100 dark:border-gray-700">
    <div class="icon-wrapper w-16 h-16 text-blue-600 dark:text-blue-400">
      <Icon :icon="icon" width="64" height="64" />
    </div>
    <div class="content">
      <h3 class="text-2xl font-semibold mb-2 text-gray-900 dark:text-white">{{ title }}</h3>
      <p class="text-gray-600 dark:text-gray-300">
        <slot></slot>
      </p>
    </div>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'

defineProps({
  icon: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.feature {
  transition: transform 0.2s ease-in-out;
}

.feature:hover {
  transform: translateY(-5px);
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style> 