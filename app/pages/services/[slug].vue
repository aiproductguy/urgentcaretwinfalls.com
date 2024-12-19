<template>
  <main class="container mx-auto px-4 py-24">
    <!-- Loading state -->
    <div v-if="pending" class="flex justify-center">
      <div class="animate-spin h-8 w-8 border-4 border-blue-600 rounded-full border-t-transparent"></div>
    </div>

    <!-- Error state -->
    <div v-else-if="error" class="text-center text-red-600">
      <p>Sorry, this service could not be found.</p>
      <NuxtLink to="/services" class="mt-4 text-blue-600 hover:text-blue-700">
        Return to Services
      </NuxtLink>
    </div>

    <!-- Content state -->
    <div v-else-if="data" class="mx-auto max-w-4xl">
      <header class="mb-16 text-center">
        <NuxtLink to="/services" class="mb-8 inline-flex items-center text-blue-600 hover:text-blue-700">
          <Icon icon="mdi:arrow-left" class="mr-2" />
          Back to Services
        </NuxtLink>
        <h1 class="text-gradient mb-6 text-5xl font-bold">{{ data.title }}</h1>
        <p class="text-xl text-gray-600 dark:text-gray-300">{{ data.description }}</p>
      </header>

      <!-- Service Content -->
      <div class="prose prose-lg mx-auto dark:prose-invert">
        <ContentRenderer :value="data" />
      </div>

      <!-- Call to Action -->
      <div class="mt-16 text-center">
        <h3 class="mb-6 text-2xl font-semibold">Need Immediate Care?</h3>
        <div class="flex flex-col gap-4 sm:flex-row sm:justify-center">
          <a href="tel:2087336700" class="button primary inline-flex items-center justify-center">
            <Icon icon="mdi:phone" class="mr-2" />Call Now: (208) 733-6700
          </a>
          <NuxtLink to="/#location" class="button secondary inline-flex items-center justify-center">
            <Icon icon="mdi:map-marker" class="mr-2" />Get Directions
          </NuxtLink>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { Icon } from '@iconify/vue'

const route = useRoute()

// Fetch content using Nuxt Content module
const { data, pending, error } = await useAsyncData(
  `service-${route.params.slug}`,
  () => queryContent('services').where({ _path: `/services/${route.params.slug}` }).findOne()
)

// Set up meta tags using the content data
useHead(() => ({
  title: data.value ? `${data.value.title} | Twin Falls Urgent Care` : 'Service | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: data.value?.description || 'Medical services provided by Twin Falls Urgent Care'
    },
    {
      name: 'keywords',
      content: data.value?.keywords || ''
    }
  ]
}))
</script>

<style scoped>
.text-gradient {
  background: linear-gradient(315deg, var(--primary-200) 25%, var(--secondary-500));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.button {
  @apply px-6 py-3 rounded-lg font-medium transition-colors duration-200;
}

.button.primary {
  @apply bg-blue-600 text-white hover:bg-blue-700;
}

.button.secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600;
}
</style> 