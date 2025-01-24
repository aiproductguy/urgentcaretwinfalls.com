<template>
  <footer class="bg-gray-100 dark:bg-gray-800 py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">
            <NuxtLink to="/contact" class="hover:text-primary-500">Contact Us</NuxtLink>
          </h3>
          <p class="mt-2">
            <a :href="'tel:' + contact.phone.replace(/\D/g, '')" class="hover:text-primary-500 inline-flex items-center gap-2">
              <IconifyIcon icon="mdi:phone" class="w-5 h-5" />
              {{ contact.phone }}
            </a>
          </p>
          <address class="not-italic text-gray-600 dark:text-gray-300">
            <NuxtLink to="/location" class="hover:text-primary-500 inline-flex gap-2">
              <IconifyIcon icon="mdi:map-marker" class="w-5 h-5 flex-shrink-0 mt-1" />
              <div>
                <p>{{ contact.address.street }}</p>
                <p>{{ contact.address.city }}, {{ contact.address.state }} {{ contact.address.zip }}</p>
              </div>
            </NuxtLink>
          </address>
          
          <div class="mt-6">
            <h4 class="font-bold text-base mb-2 text-gray-900 dark:text-white">Hours</h4>
            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
              <li>{{ hours.shortSchedule }}</li>
              <li class="text-sm italic">{{ hours.holidays }}</li>
              <li class="text-sm" :class="isOpen() ? 'text-green-600' : 'text-red-600'">
                Currently {{ isOpen() ? 'Open' : 'Closed' }}
              </li>
            </ul>
          </div>
          <!--
          <div class="mt-6">
            <h4 class="font-bold text-base mb-2 text-gray-900 dark:text-white">Follow Us</h4>
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
          -->
        </div>

        <div>
          <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">
            <NuxtLink to="/services" class="hover:text-primary-500">Services</NuxtLink>
          </h3>
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li><NuxtLink to="/services/minor-injuries" class="hover:text-primary-500">Minor Injuries</NuxtLink></li>
            <li><NuxtLink to="/services/treating-illnesses" class="hover:text-primary-500">Illness Treatment</NuxtLink></li>
            <li><NuxtLink to="/services/diagnostic-services" class="hover:text-primary-500">Diagnostic Services</NuxtLink></li>
            <li><NuxtLink to="/services/physicals-wellness" class="hover:text-primary-500">Physicals & Wellness</NuxtLink></li>
            <li><NuxtLink to="/services/xray-imaging" class="hover:text-primary-500">X-Ray & Imaging</NuxtLink></li>
            <li><NuxtLink to="/services/work-related" class="hover:text-primary-500">Work-Related Medical</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h3 class="font-bold text-lg mb-2 text-gray-900 dark:text-white">
            <NuxtLink to="/articles" class="hover:text-primary-500">Articles</NuxtLink>
          </h3>
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li><NuxtLink to="/articles/wound-care-laceration-treatment" class="hover:text-primary-500">Wound Care & Laceration Treatment</NuxtLink></li>
            <li><NuxtLink to="/articles/skin-rash-treatment-guide" class="hover:text-primary-500">Skin Rash Treatment Guide</NuxtLink></li>
            <li><NuxtLink to="/articles/dot-physical-exam-requirements" class="hover:text-primary-500">DOT Physical Requirements</NuxtLink></li>
            <li><NuxtLink to="/articles/asthma-treatment-urgent-care" class="hover:text-primary-500">Asthma & Nebulizer Treatment</NuxtLink></li>
            <li><NuxtLink to="/articles/ingrown-toenail-treatment-guide" class="hover:text-primary-500">Ingrown Toenail Guide</NuxtLink></li>
            <li><NuxtLink to="/articles/std-testing-treatment-guide" class="hover:text-primary-500">STD Testing & Treatment</NuxtLink></li>
            <li><NuxtLink to="/articles/eye-injury-foreign-object-removal" class="hover:text-primary-500">Eye Injury & Foreign Objects</NuxtLink></li>
          </ul>
        </div>
      </div>

      <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700 text-center text-gray-600 dark:text-gray-300">
        <div class="flex justify-between items-center">
          <div class="flex-1">
            <div class="flex justify-center space-x-4 mb-4">
              <NuxtLink to="/privacy-policy" class="hover:text-primary-500">Privacy Policy</NuxtLink>
              <span>•</span>
              <NuxtLink to="/terms-of-service" class="hover:text-primary-500">Terms of Service</NuxtLink>
            </div>
            <p>&copy; {{ new Date().getFullYear() }} Urgent Care Twin Falls. All rights reserved.</p>
          </div>
          <div class="flex-shrink-0">
            <img 
              src="/REG-Central-IdahosBest2022-1280w.png" 
              width="100" 
              height="100"
              alt="Idaho's Best Award Winner" 
              class="award-badge"
            />
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { Icon as IconifyIcon } from '@iconify/vue'

const { contact, hours, isOpen } = useClinicInfo()
</script>

<style scoped>
.award-badge {
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
  @apply transition-transform duration-300 hover:scale-110;
}
</style> 