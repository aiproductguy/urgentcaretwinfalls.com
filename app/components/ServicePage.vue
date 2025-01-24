<template>
  <div class="service-page">
    <Head>
      <title>{{ title }}</title>
      <meta name="description" :content="description" />
      <meta name="keywords" :content="keywords" />
    </Head>

    <main class="container mx-auto px-4 py-12">
      <div class="mx-auto max-w-3xl">
        <!-- Header -->
        <header class="mb-8 text-center">
          <NuxtLink to="/services" class="mb-4 inline-flex items-center text-blue-600 hover:text-blue-700">
            <Icon icon="mdi:arrow-left" class="mr-2" />
            Back to Services
          </NuxtLink>
          <h1 class="text-gradient mb-4 text-4xl font-bold">{{ title }}</h1>
          <p class="text-lg text-gray-600 dark:text-gray-300">{{ description }}</p>
        </header>

        <!-- Content Section -->
        <div class="prose prose-base mx-auto dark:prose-invert">
          <slot></slot>
        </div>

        <!-- Call to Action -->
        <div class="mt-8 text-center">
          <h3 class="mb-4 text-xl font-semibold">Need Immediate Care?</h3>
          <div class="flex flex-col gap-3 sm:flex-row sm:justify-center">
            <a :href="`tel:${contact.phone.replace(/\D/g, '')}`" class="button primary inline-flex items-center justify-center">
              <Icon icon="mdi:phone" class="mr-2" />Call Now: {{ contact.phone }}
            </a>
            <NuxtLink to="/location" class="button secondary inline-flex items-center justify-center">
              <Icon icon="mdi:map-marker" class="mr-2" />Get Directions
            </NuxtLink>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'

const { contact } = useClinicInfo()

defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  keywords: {
    type: String,
    required: true
  }
})
</script>
<style scoped>
.text-gradient {
  background: linear-gradient(315deg, var(--primary-200) 25%, var(--secondary-500));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.button {
  @apply px-4 py-2 rounded-lg font-medium transition-colors duration-200 text-sm;
}

.button.primary {
  @apply bg-blue-600 text-white hover:bg-blue-700;
}

.button.secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600;
}

.prose {
  @apply max-w-none;
}

.prose h2 {
  @apply text-xl font-semibold text-gray-900 mt-5 mb-2 dark:text-gray-100;
}

.prose p {
  @apply text-gray-600 mb-3 dark:text-gray-300;
}

.prose ul {
  @apply space-y-0.5 mb-3;
}

.prose ol {
  @apply space-y-1 mb-3;
}

.prose li {
  @apply text-gray-600 dark:text-gray-300;
}

.prose li > ul {
  @apply mt-0.5 mb-0.5;
}

.prose strong {
  @apply text-gray-900 font-semibold dark:text-gray-100;
}

.prose a {
  @apply text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300;
}

.prose ul ul, .prose ol ul {
  @apply mt-0.5 ml-3 space-y-0.5;
}

.prose .lead {
  @apply text-lg text-gray-600 mb-4 dark:text-gray-300;
}
</style>
