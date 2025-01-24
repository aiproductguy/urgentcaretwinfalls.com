<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <main class="container mx-auto px-4 py-24">
        <ArticleTemplate
          title="Wound Care & Laceration Treatment at Urgent Care"
          description="Learn about our professional wound care services, from assessment to treatment and aftercare instructions."
          date="January 15, 2024"
          icon="mdi:medical-bag"
          :relatedArticles="[
            {
              path: '/articles/eye-injury-foreign-object-removal',
              title: 'Eye Injury Treatment',
              description: 'Expert care for eye injuries and foreign object removal.'
            },
            {
              path: '/articles/skin-rash-treatment-guide',
              title: 'Skin Rash Treatment',
              description: 'Expert care for various types of skin conditions.'
            },
            {
              path: '/articles/std-testing-treatment-guide',
              title: 'STD Testing & Treatment',
              description: 'Comprehensive testing and treatment services.'
            }
          ]"
        >
          <h2>Professional Wound Care Services</h2>
          <p>When seeking laceration repair at an urgent care, expect the medical professional to thoroughly examine the wound, clean it thoroughly, and depending on the severity, close it with sutures, staples, or skin adhesive, while also providing local anesthetic for pain relief.</p>
          
          <h3>Assessment Process</h3>
          <ul>
            <li>Thorough wound examination</li>
            <li>Evaluation of depth and severity</li>
            <li>Assessment of underlying structure damage</li>
          </ul>

          <h3>Treatment Methods</h3>
          <ul>
            <li>Wound cleaning with sterile solutions</li>
            <li>Local anesthetic administration</li>
            <li>Appropriate closure method selection</li>
            <li>Sutures, staples, or skin adhesive application</li>
          </ul>

          <h3>When to Seek Urgent Care</h3>
          <ul>
            <li>Deep or gaping cuts</li>
            <li>Profusely bleeding wounds</li>
            <li>Lacerations over joints</li>
            <li>Facial or hand injuries</li>
          </ul>

          <h3>Aftercare Instructions</h3>
          <p>You will receive detailed instructions on:</p>
          <ul>
            <li>Wound cleaning and care</li>
            <li>Dressing changes</li>
            <li>Signs of infection to watch for</li>
            <li>Follow-up appointment scheduling</li>
          </ul>
        </ArticleTemplate>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { Icon } from '@iconify/vue'
const { contact } = useClinicInfo()

useHead({
  title: 'Wound Care & Laceration Treatment | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Learn about our professional wound care services at Twin Falls Urgent Care, from assessment and treatment to aftercare instructions for lacerations and wounds.'
    }
  ]
})
</script>

<style scoped>
.article-content {
  @apply space-y-8;
}

.article-content h2 {
  @apply text-3xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 bg-clip-text text-transparent;
}

.article-content h3 {
  @apply text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100;
}

.article-content p {
  @apply text-gray-700 dark:text-gray-300 leading-relaxed;
}

.article-content ul {
  @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 my-2;
}

.article-content li {
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