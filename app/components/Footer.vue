<template>
  <footer class="bg-gray-100 dark:bg-gray-800 py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Contact Us</h3>
          <address class="not-italic text-gray-600 dark:text-gray-300">
            <p>260 Falls Avenue, Suite C</p>
            <p>Twin Falls, ID 83301</p>
            <p class="mt-2">
              <a href="tel:+12087336700" class="hover:text-primary-500">
                (208) 733-6700
              </a>
            </p>
            <p class="mt-2">
              <a href="mailto:info@urgentcaretwinfalls.com" class="hover:text-primary-500">
                info@urgentcaretwinfalls.com
              </a>
            </p>
          </address>
          <div class="mt-6">
            <h4 class="font-bold text-base mb-2 text-gray-900 dark:text-white">Hours</h4>
            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
              <li>Monday - Friday: 8:00 AM - 5:00 PM</li>
              <li class="text-sm italic">Closed on weekends and major holidays</li>
            </ul>
          </div>
        </div>
        <div>
          <h3 class="font-bold text-lg mb-4 text-gray-900 dark:text-white">Services</h3>
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li><NuxtLink to="/services/minor-injuries" class="hover:text-primary-500">Minor Injuries</NuxtLink></li>
            <li><NuxtLink to="/services/illness-treatment" class="hover:text-primary-500">Illness Treatment</NuxtLink></li>
            <li><NuxtLink to="/services/diagnostic" class="hover:text-primary-500">Diagnostic Services</NuxtLink></li>
            <li><NuxtLink to="/services/physicals" class="hover:text-primary-500">Physicals & Wellness</NuxtLink></li>
            <li><NuxtLink to="/services/xray" class="hover:text-primary-500">X-Ray & Imaging</NuxtLink></li>
            <li><NuxtLink to="/services/work-medical" class="hover:text-primary-500">Work-Related Medical</NuxtLink></li>
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
          <!-- Awards Section -->
          <div class="mt-8">
            <h4 class="font-bold text-base mb-4 text-gray-900 dark:text-white">Awards & Recognition</h4>
            <div class="flex justify-center md:justify-start">
              <img 
                src="/best-award-2023.png" 
                width="120" 
                height="120"
                alt="Idaho's Best 2023 Statewide Winner" 
                class="award-badge"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700 text-center text-gray-600 dark:text-gray-300">
        <div class="flex justify-center space-x-4 mb-4">
          <NuxtLink to="/privacy-policy" class="hover:text-primary-500">Privacy Policy</NuxtLink>
          <span>•</span>
          <NuxtLink to="/terms-of-service" class="hover:text-primary-500">Terms of Service</NuxtLink>
        </div>
        <p>&copy; {{ new Date().getFullYear() }} Urgent Care of Twin Falls. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'
</script>

<style scoped>
.award-badge {
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
  @apply transition-transform duration-300 hover:scale-110;
}
</style> 