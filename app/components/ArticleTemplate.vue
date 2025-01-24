<template>
  <article class="prose prose-lg dark:prose-invert mx-auto" style="width: 860px; max-width: 100%;">
    <!-- Article Header -->
    <header class="mb-12">
      <div class="flex items-center gap-6 mb-6">
        <div class="w-16 h-16 flex-shrink-0 flex items-center justify-center rounded-full bg-blue-100 dark:bg-blue-900/30 shadow-lg">
          <Icon :icon="icon" class="w-8 h-8 text-blue-600 dark:text-blue-400" />
        </div>
        <h1 class="bg-gradient-to-r from-blue-600 to-gray-500 dark:from-blue-400 dark:to-gray-400 bg-clip-text text-transparent text-4xl font-bold md:text-5xl">
          {{ title }}
        </h1>
      </div>
      <p class="text-xl text-gray-600 dark:text-gray-300">
        {{ description }}
      </p>
      <div class="mt-6 flex flex-wrap items-center gap-6 text-sm text-gray-500 dark:text-gray-400">
        <div class="flex items-center">
          <Icon icon="mdi:account" class="w-4 h-4 mr-2" />
          {{ author }}
        </div>
        <div class="flex items-center">
          <Icon icon="mdi:calendar" class="w-4 h-4 mr-2" />
          {{ date }}
        </div>
      </div>
    </header>

    <!-- Article Content -->
    <div class="article-content">
      <slot></slot>
    </div>

    <!-- Call to Action -->
    <section class="mt-16 text-center not-prose bg-blue-50/50 dark:bg-blue-900/20 rounded-2xl p-8 shadow-sm">
      <h3 class="mb-6 text-2xl font-semibold bg-gradient-to-r from-blue-600 to-gray-500 dark:from-blue-400 dark:to-gray-400 bg-clip-text text-transparent">Need Medical Attention?</h3>
      <div class="flex flex-col gap-4 sm:flex-row sm:justify-center">
        <a :href="`tel:${contact.phone.replace(/\D/g, '')}`" class="px-6 py-3 rounded-lg font-medium bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white inline-flex items-center justify-center shadow-md hover:shadow-lg transition-all duration-200">
          <Icon icon="mdi:phone" class="mr-2" />Call Now: {{ contact.phone }}
        </a>
        <NuxtLink to="/location" class="px-6 py-3 rounded-lg font-medium bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-800 dark:text-gray-100 inline-flex items-center justify-center shadow-md hover:shadow-lg transition-all duration-200">
          <Icon icon="mdi:map-marker" class="mr-2" />Find Our Location
        </NuxtLink>
      </div>
    </section>

    <!-- Related Articles -->
    <section class="mt-16 not-prose">
      <h3 class="text-2xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-gray-500 dark:from-blue-400 dark:to-gray-400 bg-clip-text text-transparent">Related Articles</h3>
      <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <li v-for="article in relatedArticles" :key="article.path">
          <NuxtLink :to="article.path" class="block p-6 rounded-xl bg-gray-50 dark:bg-gray-800/50 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
            <h4 class="font-semibold text-gray-900 dark:text-white mb-2">{{ article.title }}</h4>
            <p class="text-sm text-gray-600 dark:text-gray-300">{{ article.description }}</p>
          </NuxtLink>
        </li>
      </ul>
    </section>
  </article>
</template>

<script setup>
import { Icon } from '@iconify/vue'
const { contact } = useClinicInfo()

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  author: {
    type: String,
    default: 'Chuck Fuller, PA'
  },
  date: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  },
  relatedArticles: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.article-content {
  @apply space-y-8;
}

.article-content :deep(h2) {
  @apply text-3xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-gray-500 dark:from-blue-400 dark:to-gray-400 bg-clip-text text-transparent;
}

.article-content :deep(h3) {
  @apply text-2xl font-semibold mb-4 text-gray-900 dark:text-white;
}

.article-content :deep(p) {
  @apply text-gray-700 dark:text-gray-300 leading-relaxed;
}

.article-content :deep(ul) {
  @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 my-2;
}

.article-content :deep(li) {
  @apply flex items-start text-gray-700 dark:text-gray-300;
  &::before {
    content: "•";
    @apply text-blue-500 font-bold mr-1;
  }
}

:deep(.prose) {
  @apply max-w-none;
}
</style> 