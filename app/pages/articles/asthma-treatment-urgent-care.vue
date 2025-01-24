<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900 dark:to-gray-800/50">
      <main class="container mx-auto px-4 py-16 sm:py-24">
        <ArticleTemplate
          title="Asthma Treatment & Nebulizer Care at Urgent Care"
          description="Get immediate relief with nebulizer treatments and expert care for asthma symptoms."
          date="January 12, 2024"
          icon="mdi:lungs"
          :relatedArticles="[
            {
              path: '/articles/std-testing-treatment-guide',
              title: 'STD Testing & Treatment',
              description: 'Comprehensive testing and treatment services for STDs.'
            },
            {
              path: '/articles/skin-rash-treatment-guide',
              title: 'Skin Rash Treatment Guide',
              description: 'Expert care for various types of skin rashes.'
            },
            {
              path: '/articles/dot-physical-exam-requirements',
              title: 'DOT Physical Exam Guide',
              description: 'Complete guide to DOT physical requirements and process.'
            }
          ]"
        >
          <h2>Immediate Asthma Care at Urgent Care</h2>
          <p>An urgent care can help with nebulizer (neb) treatments for asthma by providing immediate access to a medical professional who can assess your symptoms, administer a nebulizer treatment with a medication like albuterol to quickly open your airways, and manage your asthma attack if necessary.</p>

          <h3>Quick Relief Through Nebulizer Treatment</h3>
          <p>Nebulizer treatments offer several advantages:</p>
          <ul>
            <li>Fast-acting medication delivery directly to your lungs</li>
            <li>Effective relief during severe symptoms</li>
            <li>Professional administration when you can't effectively use an inhaler</li>
            <li>Immediate improvement in breathing within minutes</li>
          </ul>

          <h3>Professional Care and Monitoring</h3>
          <p>Our healthcare providers ensure comprehensive care through:</p>
          <ul>
            <li>Expert assessment of asthma symptoms</li>
            <li>Proper medication dosage determination</li>
            <li>Monitoring of vital signs during treatment</li>
            <li>Oxygen level assessment before and after treatment</li>
          </ul>

          <h3>When to Seek Urgent Care for Asthma</h3>
          <ul>
            <li>Severe wheezing or shortness of breath</li>
            <li>Inhaler not providing sufficient relief</li>
            <li>Difficulty speaking due to breathing problems</li>
            <li>Increased use of rescue inhaler</li>
            <li>Nighttime asthma symptoms</li>
          </ul>

          <h3>Follow-up Care and Prevention</h3>
          <p>After your urgent care visit, we may provide:</p>
          <ul>
            <li>Prescription medications including oral steroids</li>
            <li>Asthma action plan updates</li>
            <li>Referral to asthma specialists if needed</li>
            <li>Recommendations for preventing future attacks</li>
            <li>Instructions for home nebulizer use if prescribed</li>
          </ul>

          <h3>Long-term Asthma Management</h3>
          <p>We'll help you develop strategies for:</p>
          <ul>
            <li>Identifying and avoiding asthma triggers</li>
            <li>Proper use of maintenance medications</li>
            <li>Regular peak flow monitoring</li>
            <li>Emergency action plan development</li>
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
  title: 'Asthma Treatment & Nebulizer Care | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Get immediate relief from asthma symptoms with professional nebulizer treatments at Twin Falls Urgent Care. Expert care and monitoring for asthma flare-ups.'
    }
  ]
})
</script>

<style scoped>
.article-content {
  @apply space-y-8;
}

.article-content h2 {
  @apply text-3xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-gray-500 dark:from-blue-400 dark:to-gray-400 bg-clip-text text-transparent;
}

.article-content h3 {
  @apply text-2xl font-semibold mb-4 text-gray-900 dark:text-white;
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