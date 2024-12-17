<template>
  <div class="min-h-screen flex flex-col bg-gray-50 dark:bg-gray-900">
    <Header />
    
    <main class="flex-grow">
      <slot />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'

// Close mobile menu when route changes
watch(() => useRoute().fullPath, () => {
  isMenuOpen.value = false
})
</script> 