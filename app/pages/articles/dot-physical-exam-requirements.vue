<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50/80 to-white dark:from-gray-900 dark:to-gray-800/90">
      <main class="container mx-auto px-4 py-20">
        <ArticleTemplate
          title="DOT Physical Exam Requirements & Certification Guide"
          description="Everything you need to know about DOT physicals, requirements, and certification process."
          date="January 13, 2024"
          icon="mdi:clipboard-text-clock"
          :relatedArticles="[
            {
              path: '/articles/work-injury-treatment',
              title: 'Work Injury Treatment Guide',
              description: 'Learn about workplace injury treatment options and workers\' compensation processes.'
            },
            {
              path: '/articles/physical-exam-basics',
              title: 'Physical Exam Basics',
              description: 'Understanding what to expect during a standard physical examination.'
            },
            {
              path: '/articles/occupational-health-services',
              title: 'Occupational Health Services',
              description: 'Comprehensive guide to our occupational health services and programs.'
            }
          ]"
        >
          <h2>Understanding DOT Physical Requirements</h2>
          <p>A Department of Transportation (DOT) physical is required for individuals who drive commercial vehicles to ensure they are physically, mentally, and emotionally fit. The Federal Motor Carrier Safety Administration (FMCSA) mandates this exam to ensure public safety.</p>

          <h3>Who Needs a DOT Physical?</h3>
          <p>DOT physicals are required for drivers of:</p>
          <ul>
            <li>Vehicles carrying over 15 people</li>
            <li>Vehicles designed to carry over 8 people for pay</li>
            <li>Vehicles carrying hazardous materials that need a placard</li>
            <li>Vehicles weighing 10,000 pounds or more</li>
          </ul>

          <h3>What Does a DOT Physical Include?</h3>
          <p>The comprehensive examination includes:</p>
          <ul>
            <li>Height and weight measurements</li>
            <li>Blood pressure check</li>
            <li>Vision and hearing tests</li>
            <li>Heart and lung examination</li>
            <li>Abdominal check</li>
            <li>Urinalysis for health screening</li>
            <li>Additional tests based on symptoms or conditions</li>
          </ul>

          <h3>Medical Certification Requirements</h3>
          <p>After passing the DOT physical, you'll receive:</p>
          <ul>
            <li>Medical Examiner's Certificate (MEC)</li>
            <li>2-year certification (standard)</li>
            <li>Annual certification for certain conditions</li>
          </ul>

          <h3>How to Prepare for Your DOT Physical</h3>
          <p>To ensure a successful examination:</p>
          <ul>
            <li>Maintain good overall health</li>
            <li>Keep medications current and documented</li>
            <li>Ensure vision correction is up-to-date</li>
            <li>Avoid alcohol and smoking before the exam</li>
            <li>Manage weight and blood pressure</li>
          </ul>

          <h3>Required Documentation</h3>
          <p>Bring the following to your appointment:</p>
          <ul>
            <li>Complete medical history</li>
            <li>List of current medications</li>
            <li>Contact information for healthcare providers</li>
            <li>Previous DOT physical results</li>
            <li>Any relevant medical records</li>
          </ul>

          <h3>Disqualifying Conditions</h3>
          <p>Certain conditions may disqualify drivers:</p>
          <ul>
            <li>Uncontrolled heart disease</li>
            <li>Epilepsy or seizure disorders</li>
            <li>Unmanaged diabetes</li>
            <li>Severe vision or hearing loss</li>
          </ul>
          <p>Some conditions may be reconsidered with proper management and documentation.</p>

          <h3>Cost and Insurance</h3>
          <p>DOT physicals typically cost between $85-$150. Some employers may cover this expense. Contact us for current pricing and insurance information.</p>
        </ArticleTemplate>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
useHead({
  title: 'DOT Physical Exam Requirements & Certification | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Complete guide to DOT physical requirements, certification process, and medical examinations at Twin Falls Urgent Care. Learn what to expect and how to prepare.'
    }
  ]
})
</script>

<style scoped>
.btn-primary {
  @apply inline-flex items-center justify-center px-6 py-3 rounded-xl font-semibold
         bg-blue-600 text-white hover:bg-blue-700 
         transition-all duration-200 shadow-sm hover:shadow-md;
}

.btn-secondary {
  @apply inline-flex items-center justify-center px-6 py-3 rounded-xl font-semibold
         bg-gray-100 text-gray-900 hover:bg-gray-200 
         dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700
         transition-all duration-200 shadow-sm hover:shadow-md;
}

:deep(.article-content) {
  @apply grid gap-6;

  h2 {
    @apply text-3xl font-bold mt-12 mb-6 bg-gradient-to-r from-blue-600 via-blue-500 to-gray-500 bg-clip-text text-transparent;
  }

  h3 {
    @apply text-2xl font-bold text-gray-800 dark:text-gray-100 mt-8 mb-4;
  }

  p {
    @apply text-gray-700 dark:text-gray-300 leading-relaxed mb-4;
  }

  ul {
    @apply space-y-2 ml-6;

    li {
      @apply text-gray-700 dark:text-gray-300 relative pl-6;
      &::before {
        content: "•";
        @apply absolute left-0 text-blue-500 dark:text-blue-400;
      }
    }
  }
}
</style>