<template>
  <div class="min-h-screen flex flex-col bg-gray-50 dark:bg-gray-900">
    <Header />
    
    <main class="flex-grow">
      <slot />
    </main>

    <footer class="bg-gray-100 dark:bg-gray-800 py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Contact Us</h3>
            <address class="not-italic text-gray-600 dark:text-gray-300">
              <p>1234 Main Street</p>
              <p>Twin Falls, ID 83301</p>
              <p class="mt-2">
                <a href="tel:+1234567890" class="hover:text-primary-500">
                  (123) 456-7890
                </a>
              </p>
            </address>
          </div>
          <div>
            <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Services</h3>
            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
              <li><NuxtLink to="/services/minor-injuries" class="hover:text-primary-500">Minor Injuries</NuxtLink></li>
              <li><NuxtLink to="/services/illnesses" class="hover:text-primary-500">Illnesses</NuxtLink></li>
              <li><NuxtLink to="/services/physicals" class="hover:text-primary-500">Physicals & Wellness</NuxtLink></li>
              <li><NuxtLink to="/services/xray" class="hover:text-primary-500">X-Ray & Imaging</NuxtLink></li>
            </ul>
          </div>
          <div>
            <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Hours</h3>
            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
              <li>Monday - Friday: 8am - 8pm</li>
              <li>Saturday: 9am - 6pm</li>
              <li>Sunday: 10am - 4pm</li>
            </ul>
          </div>
          <div>
            <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Follow Us</h3>
            <div class="flex space-x-4">
              <a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary-500">
                <IconifyIcon icon="mdi:facebook" class="w-6 h-6" />
              </a>
              <a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary-500">
                <IconifyIcon icon="mdi:twitter" class="w-6 h-6" />
              </a>
              <a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary-500">
                <IconifyIcon icon="mdi:instagram" class="w-6 h-6" />
              </a>
            </div>
          </div>
        </div>
        <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700 text-center text-gray-600 dark:text-gray-300">
          <p>&copy; {{ new Date().getFullYear() }} Urgent Care of Twin Falls. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'

// Close mobile menu when route changes
watch(() => useRoute().fullPath, () => {
  isMenuOpen.value = false
})
</script> 