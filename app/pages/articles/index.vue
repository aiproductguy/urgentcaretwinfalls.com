<template>
  <NuxtLayout>
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <main class="container mx-auto px-4 py-24">
        <!-- Articles Header -->
        <header class="mb-16 text-center">
          <h1 class="text-gradient mb-6 text-5xl font-bold md:text-6xl">Health & Wellness Articles</h1>
          <p class="mx-auto max-w-2xl text-xl text-gray-600 dark:text-gray-300">
            Stay informed with expert medical advice, health tips, and insights from our experienced healthcare team.
          </p>
        </header>
        
        <!-- Articles List -->
        <div class="max-w-4xl mx-auto space-y-8">
          <article 
            v-for="article in articles" 
            :key="article.slug" 
            class="group bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-all"
          >
            <NuxtLink :to="'/articles/' + article.slug" class="flex items-start p-6 gap-6">
              <div class="flex-shrink-0 w-12 h-12 flex items-center justify-center rounded-full bg-primary-100 dark:bg-primary-900">
                <Icon :icon="article.icon" class="w-6 h-6 text-primary-600 dark:text-primary-300" />
              </div>
              <div class="flex-1 min-w-0">
                <h2 class="text-xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-primary-500">
                  {{ article.title }}
                </h2>
                <p class="text-gray-600 dark:text-gray-300 mb-3 line-clamp-2">{{ article.excerpt }}</p>
                <div class="flex items-center text-sm text-gray-500 dark:text-gray-400">
                  <Icon icon="mdi:calendar" class="w-4 h-4 mr-2" />
                  <span>{{ article.date }}</span>
                  <span class="mx-2">•</span>
                  <span class="text-primary-500 group-hover:text-primary-600">Read More →</span>
                </div>
              </div>
            </NuxtLink>
          </article>
        </div>

        <!-- Call to Action -->
        <section class="mt-16 text-center">
          <h3 class="mb-6 text-2xl font-semibold">Have Questions About Your Health?</h3>
          <div class="flex flex-col gap-4 sm:flex-row sm:justify-center">
            <a :href="`tel:${contact.phone.replace(/\D/g, '')}`" class="button primary inline-flex items-center justify-center">
              <Icon icon="mdi:phone" class="mr-2" />Call Now: {{ contact.phone }}
            </a>
            <NuxtLink to="/contact" class="button secondary inline-flex items-center justify-center">
              <Icon icon="mdi:message" class="mr-2" />Contact Us
            </NuxtLink>
          </div>
        </section>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { Icon } from '@iconify/vue'
const { contact } = useClinicInfo()

const articles = [
  {
    slug: 'wound-care-laceration-treatment',
    title: 'Wound Care & Laceration Treatment at Urgent Care',
    excerpt: 'Learn about our professional wound care services, from assessment to treatment and aftercare instructions.',
    icon: 'mdi:medical-bag',
    date: 'January 15, 2024'
  },
  {
    slug: 'skin-rash-treatment-guide',
    title: 'Skin Rash Treatment Guide: When to Seek Urgent Care',
    excerpt: 'Know when to seek urgent care for rashes and learn about common causes, treatments, and prevention.',
    icon: 'mdi:bandage',
    date: 'January 14, 2024'
  },
  {
    slug: 'dot-physical-exam-requirements',
    title: 'DOT Physical Exam Requirements & Certification Guide',
    excerpt: 'Everything you need to know about DOT physicals, requirements, and certification process.',
    icon: 'mdi:clipboard-text-clock',
    date: 'January 13, 2024'
  },
  {
    slug: 'asthma-treatment-urgent-care',
    title: 'Asthma Treatment & Nebulizer Care at Urgent Care',
    excerpt: 'Get immediate relief with nebulizer treatments and expert care for asthma symptoms.',
    icon: 'mdi:lungs',
    date: 'January 12, 2024'
  },
  {
    slug: 'ingrown-toenail-treatment-guide',
    title: 'Ingrown Toenail Treatment & Prevention Guide',
    excerpt: 'Understanding causes, treatment options, and when to seek medical care for ingrown toenails.',
    icon: 'mdi:foot-print',
    date: 'January 11, 2024'
  },
  {
    slug: 'std-testing-treatment-guide',
    title: 'STD Testing & Treatment: Complete Guide',
    excerpt: 'Confidential STD testing and treatment services with quick results and comprehensive care.',
    icon: 'mdi:test-tube',
    date: 'January 10, 2024'
  },
  {
    slug: 'eye-injury-foreign-object-removal',
    title: 'Eye Injury & Foreign Object Removal Guide',
    excerpt: 'Expert care for eye injuries and foreign object removal with state-of-the-art equipment.',
    icon: 'mdi:eye-plus',
    date: 'January 9, 2024'
  }
]

useHead({
  title: 'Health & Wellness Articles | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Expert medical advice, health tips, and insights from Twin Falls Urgent Care. Learn about when to visit, common conditions, treatments, and preventive care.'
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