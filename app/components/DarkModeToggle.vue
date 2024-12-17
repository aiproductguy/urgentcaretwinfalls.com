<template>
  <button 
    @click="toggleDark()" 
    class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
    aria-label="Toggle dark mode"
  >
    <IconifyIcon
      :icon="isDark ? 'ph:sun-bold' : 'ph:moon-bold'"
      class="w-5 h-5 text-gray-600 dark:text-gray-300"
    />
  </button>
</template>

<script setup lang="ts">
import { Icon as IconifyIcon } from '@iconify/vue'

const isDark = useDark({
  selector: 'html',
  attribute: 'class',
  valueDark: 'dark',
  valueLight: ''
})
const toggleDark = useToggle(isDark)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style> 