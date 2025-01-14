<template>
  <NuxtLayout>
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <main class="container mx-auto px-4 py-24">
        <!-- Services Header -->
        <header class="mb-16 text-center">
          <h1 class="text-gradient mb-6 text-5xl font-bold md:text-6xl">Our Services</h1>
          <p class="mx-auto max-w-2xl text-xl text-gray-600 dark:text-gray-300">
            Comprehensive medical care when you need it most. Our experienced team provides
            a wide range of services to meet your healthcare needs.
          </p>
        </header>

        <!-- Services Grid -->
        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <NuxtLink
            v-for="service in services"
            :key="service.slug"
            :to="`/services/${service.slug}`"
            class="group relative overflow-hidden rounded-xl bg-white p-6 shadow-lg transition-all hover:shadow-xl dark:bg-gray-800"
          >
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-purple-600/10 opacity-0 transition-opacity group-hover:opacity-100"></div>
            <Icon :icon="service.icon" class="mb-4 h-12 w-12 text-blue-600" />
            <h3 class="mb-3 text-2xl font-semibold">{{ service.title }}</h3>
            <p class="text-gray-600 dark:text-gray-300">{{ service.description }}</p>
          </NuxtLink>
        </div>

        <!-- Why Choose Us Section -->
        <section class="mt-32">
          <WhyChooseUs />
        </section>

        <!-- Call to Action -->
        <section class="mt-16 text-center">
          <h3 class="mb-6 text-2xl font-semibold">Need Medical Care?</h3>
          <div class="flex flex-col gap-4 sm:flex-row sm:justify-center">
            <a href="tel:2087336700" class="button primary inline-flex items-center justify-center">
              <Icon icon="mdi:phone" class="mr-2" />Call Now: (208) 733-6700
            </a>
            <NuxtLink to="/#location" class="button secondary inline-flex items-center justify-center">
              <Icon icon="mdi:map-marker" class="mr-2" />Get Directions
            </NuxtLink>
          </div>
        </section>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { Icon } from '@iconify/vue'
import WhyChooseUs from '~/components/WhyChooseUs.vue'

const services = [
  {
    title: 'Minor Injuries',
    slug: 'minor-injuries',
    icon: 'mdi:hospital-building',
    description: 'Expert care for sprains, fractures, cuts, burns, and other non-life-threatening injuries.'
  },
  {
    title: 'Illness Treatment',
    slug: 'treating-illnesses',
    icon: 'mdi:thermometer-lines',
    description: 'Treatment for common illnesses including cold, flu, infections, and other acute conditions.'
  },
  {
    title: 'Diagnostic Services',
    slug: 'diagnostic-services',
    icon: 'mdi:stethoscope',
    description: 'Comprehensive diagnostic testing including lab work, strep tests, and more.'
  },
  {
    title: 'Physicals & Checkups',
    slug: 'physicals-wellness',
    icon: 'mdi:clipboard-pulse',
    description: 'School physicals, sports physicals, and general wellness checkups for all ages.'
  },
  {
    title: 'X-ray & Imaging',
    slug: 'xray-imaging',
    icon: 'mdi:radiology-box',
    description: 'On-site X-ray services and imaging for accurate diagnosis of injuries and conditions.'
  },
  {
    title: 'Work-Related Medical',
    slug: 'work-related',
    icon: 'mdi:office-chair',
    description: 'Work-related medical services including pre-employment screenings and injury care.'
  }
]

useHead({
  title: 'Our Services | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Explore our comprehensive medical services including injury care, illness treatment, diagnostics, physicals, X-rays, and occupational health services.'
    }
  ]
})

definePageMeta({
  layout: 'default'
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