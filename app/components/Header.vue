<template>
  <header class="py-6 bg-white dark:bg-gray-800 shadow-sm">
    <div class="container mx-auto px-4">
      <nav class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <NuxtLink to="/" class="flex items-center gap-2">
            <img src="/images/logo-heart.svg" alt="Urgent Care of Twin Falls" width="47" height="37" />
            <span class="text-xl font-bold text-primary-500">Urgent Care</span>
            <span class="text-gray-600 dark:text-gray-300">of Twin Falls</span>
          </NuxtLink>
          <DarkModeToggle />
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
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Icon as IconifyIcon } from '@iconify/vue'
import DarkModeToggle from './DarkModeToggle.vue'

const isMenuOpen = ref(false)

const menuItems = [
  { to: '/', text: 'Home' },
  { to: '/services', text: 'Services' },
  { to: '/location', text: 'Location' },
  { to: '/about', text: 'About' },
  { to: '/contact', text: 'Contact' }
]
</script> 