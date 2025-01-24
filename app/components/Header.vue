<template>
  <header class="py-6 bg-white dark:bg-gray-800 shadow-sm">
    <div class="container mx-auto px-4">
      <nav class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <NuxtLink to="/" class="flex items-center gap-2">
            <img 
              src="/images/light-logo.jpg" 
              alt="Urgent Care Twin Falls" 
              width="80" 
              height="64"
              @error="handleImageError"
              v-if="showLogo" 
              class="object-contain"
            />
            <div v-if="!showLogo" class="text-xl font-bold text-primary-500">
              Urgent Care Twin Falls
            </div>
          </NuxtLink>
          <DarkModeToggle />
          <a
            class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors inline-flex items-center"
            aria-label="Call clinic"
            :href="'tel:' + contact.phone.replace(/\D/g, '')"
          >
            <IconifyIcon 
              icon="mdi:phone" 
              class="w-5 h-5 text-gray-600 dark:text-gray-300"
            />
          </a>
          <a
            class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors inline-flex items-center"
            aria-label="Get directions"
            :href="'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(`${contact.address.street}, ${contact.address.city}, ${contact.address.state} ${contact.address.zip}`)"
            target="_blank"
            rel="noopener noreferrer"
          >
            <IconifyIcon 
              icon="mdi:map-marker" 
              class="w-5 h-5 text-gray-600 dark:text-gray-300"
            />
          </a>
        </div>
        
        <div class="hidden md:flex items-center gap-8">
          <NuxtLink 
            v-for="item in menuItems" 
            :key="item.to" 
            :to="item.to"
            class="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 transition-colors"
            :class="{ 'text-primary-500 dark:text-primary-400 font-medium': $route.path === item.to }"
          >
            {{ item.text }}
          </NuxtLink>
          
          <div class="relative group">
            <button 
              class="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 transition-colors inline-flex items-center gap-1"
              :class="{ 'text-primary-500 dark:text-primary-400 font-medium': $route.path.startsWith('/services') }"
            >
              Services
              <IconifyIcon icon="mdi:chevron-down" class="w-5 h-5 transition-transform group-hover:rotate-180" />
            </button>
            
            <div class="absolute left-0 mt-2 w-64 bg-white dark:bg-gray-800 rounded-md shadow-lg py-2 invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-200 z-50">
              <NuxtLink
                v-for="service in serviceItems"
                :key="service.to"
                :to="service.to"
                class="block px-4 py-2 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-primary-500 dark:hover:text-primary-400"
                :class="{ 'text-primary-500 dark:text-primary-400 font-medium': $route.path === service.to }"
              >
                {{ service.text }}
              </NuxtLink>
            </div>
          </div>

          <a
            :href="'tel:' + contact.phone.replace(/\D/g, '')"
            class="inline-flex items-center gap-2 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            <IconifyIcon icon="mdi:phone" class="w-5 h-5" />
            Call Now
          </a>
        </div>

        <button 
          class="md:hidden"
          @click="isMenuOpen = !isMenuOpen"
          aria-label="Toggle menu"
        >
          <IconifyIcon 
            :icon="isMenuOpen ? 'mdi:close' : 'mdi:menu'" 
            class="w-6 h-6 text-gray-600 dark:text-gray-300"
          />
        </button>
      </nav>

      <!-- Mobile menu -->
      <div 
        v-show="isMenuOpen"
        class="md:hidden mt-4 py-4 border-t border-gray-100 dark:border-gray-700"
      >
        <div class="flex flex-col gap-4">
          <NuxtLink 
            v-for="item in menuItems" 
            :key="item.to" 
            :to="item.to"
            class="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 transition-colors"
            :class="{ 'text-primary-500 dark:text-primary-400 font-medium': $route.path === item.to }"
            @click="isMenuOpen = false"
          >
            {{ item.text }}
          </NuxtLink>

          <div class="pl-4 border-l-2 border-gray-200 dark:border-gray-700">
            <div class="mb-2 text-gray-600 dark:text-gray-300 font-medium">Services</div>
            <div class="flex flex-col gap-2">
              <NuxtLink
                v-for="service in serviceItems"
                :key="service.to"
                :to="service.to"
                class="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 transition-colors"
                :class="{ 'text-primary-500 dark:text-primary-400 font-medium': $route.path === service.to }"
                @click="isMenuOpen = false"
              >
                {{ service.text }}
              </NuxtLink>
            </div>
          </div>

          <a
            :href="'tel:' + contact.phone.replace(/\D/g, '')"
            class="inline-flex items-center gap-2 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-500 hover:bg-primary-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            @click="isMenuOpen = false"
          >
            <IconifyIcon icon="mdi:phone" class="w-5 h-5" />
            Call Now
          </a>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Icon as IconifyIcon } from '@iconify/vue'
import DarkModeToggle from './DarkModeToggle.vue'
import { useClinicInfo } from '~/composables/useClinicInfo'

const isMenuOpen = ref(false)
const showLogo = ref(true)
const { contact } = useClinicInfo()

const handleImageError = () => {
  showLogo.value = false
}

const menuItems = [
  { to: '/', text: 'Home' },
  { to: '/about', text: 'About Us' },
  { to: '/location', text: 'Location' }
]

const serviceItems = [
  { to: '/services/minor-injuries', text: 'Minor Injuries' },
  { to: '/services/treating-illnesses', text: 'Illness Treatment' },
  { to: '/services/diagnostic-services', text: 'Diagnostic Services' },
  { to: '/services/physicals-wellness', text: 'Physicals & Wellness' },
  { to: '/services/xray-imaging', text: 'X-Ray & Imaging' },
  { to: '/services/work-related', text: 'Work-Related Medical' }
]
</script>

<style scoped>
.group:hover .group-hover\:visible {
  visibility: visible;
}
</style>