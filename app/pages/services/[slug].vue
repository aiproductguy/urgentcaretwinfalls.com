<template>
  <main class="container mx-auto px-4 py-24">
    <div v-if="service" class="mx-auto max-w-4xl">
      <!-- Service Header -->
      <header class="mb-16 text-center">
        <NuxtLink to="/services" class="mb-8 inline-flex items-center text-blue-600 hover:text-blue-700">
          <Icon icon="mdi:arrow-left" class="mr-2" />
          Back to Services
        </NuxtLink>
        <h1 class="text-gradient mb-6 text-5xl font-bold">{{ service.title }}</h1>
        <p class="text-xl text-gray-600 dark:text-gray-300">{{ service.description }}</p>
      </header>

      <!-- Service Content -->
      <div class="prose prose-lg mx-auto dark:prose-invert">
        <ContentDoc :path="`/services/${route.params.slug}`" />
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
const services = {
  'minor-injuries': {
    title: 'Minor Injuries',
    description: 'Expert care for sprains, fractures, cuts, burns, and other non-life-threatening injuries.'
  },
  'illness-treatment': {
    title: 'Illness Treatment',
    description: 'Treatment for common illnesses including cold, flu, infections, and other acute conditions.'
  },
  diagnostic: {
    title: 'Diagnostic Services',
    description: 'Comprehensive diagnostic testing including lab work, strep tests, and more.'
  },
  physicals: {
    title: 'Physicals & Checkups',
    description: 'School physicals, sports physicals, and general wellness checkups for all ages.'
  },
  xray: {
    title: 'X-ray & Imaging',
    description: 'On-site X-ray services and imaging for accurate diagnosis of injuries and conditions.'
  },
  'work-medical': {
    title: 'Work-Related Medical',
    description: 'Work-related medical services including pre-employment screenings and injury care.'
  }
}

const service = services[route.params.slug]

useHead({
  title: `${service?.title || 'Service'} | Twin Falls Urgent Care`,
  meta: [
    {
      name: 'description',
      content: service?.description || 'Medical services provided by Twin Falls Urgent Care'
    }
  ]
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
  @apply px-6 py-3 rounded-lg font-medium transition-colors duration-200;
}

.button.primary {
  @apply bg-blue-600 text-white hover:bg-blue-700;
}

.button.secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600;
}
</style> 