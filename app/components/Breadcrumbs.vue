<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const breadcrumbs = computed(() => {
  const pathArray = route.path.split('/').filter(Boolean)
  return [
    { name: 'Home', path: '/' },
    ...pathArray.map((segment, index) => ({
      name: segment.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '),
      path: '/' + pathArray.slice(0, index + 1).join('/')
    }))
  ]
})
</script>

<template>
  <nav 
    aria-label="Breadcrumb" 
    class="py-3 px-4 md:px-6 border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800"
  >
    <div class="container mx-auto">
      <ol 
        class="flex flex-wrap items-center text-sm"
        vocab="https://schema.org/"
        typeof="BreadcrumbList"
      >
        <li 
          v-for="(crumb, index) in breadcrumbs" 
          :key="crumb.path"
          property="itemListElement"
          typeof="ListItem"
          class="flex items-center"
        >
          <meta property="position" :content="(index + 1).toString()" />
          <NuxtLink
            :to="crumb.path"
            :class="[
              'transition-colors duration-200',
              index === breadcrumbs.length - 1 
                ? 'text-primary-600 dark:text-primary-400 font-medium' 
                : 'text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400'
            ]"
            property="item"
            typeof="WebPage"
          >
            <span property="name">{{ crumb.name }}</span>
          </NuxtLink>
          <span 
            v-if="index < breadcrumbs.length - 1" 
            class="mx-3 text-gray-400 dark:text-gray-600"
            aria-hidden="true"
          >
            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
              <path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" />
            </svg>
          </span>
        </li>
      </ol>
    </div>
  </nav>
</template> 