<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
    <Header />
    
    <main class="flex-grow">
      <slot />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'
import { ref } from 'vue'
import Header from '~/components/Header.vue'
import Footer from '~/components/Footer.vue'

const isMenuOpen = ref(false)

// Close mobile menu when route changes
watch(() => useRoute().fullPath, () => {
  isMenuOpen.value = false
})

// Provide menu state to child components
provide('isMenuOpen', isMenuOpen)
</script>

<style>
.text-gradient {
  @apply bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-blue-800;
}
</style> 