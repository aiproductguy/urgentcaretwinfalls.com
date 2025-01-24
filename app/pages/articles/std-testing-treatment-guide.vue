<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50/80 to-white dark:from-gray-900 dark:to-gray-800/90">
      <main class="container mx-auto px-4 py-20">
        <ArticleTemplate
          title="STD Testing & Treatment: Your Guide to Sexual Health"
          description="Comprehensive information about STD testing, treatment options, and when to seek urgent care for sexual health concerns."
          date="January 14, 2024"
          icon="mdi:test-tube"
          :relatedArticles="[
            {
              path: '/articles/womens-health-services',
              title: 'Women\'s Health Services',
              description: 'Comprehensive women\'s health services and screenings.'
            },
            {
              path: '/articles/mens-health-guide',
              title: 'Men\'s Health Guide',
              description: 'Essential health information for men\'s wellness.'
            },
            {
              path: '/articles/sexual-health-guide',
              title: 'Sexual Health Guide',
              description: 'Complete guide to maintaining sexual health and wellness.'
            }
          ]"
        >
          <h2>Understanding STD Testing</h2>
          <p>Regular STD testing is an essential part of maintaining sexual health. Our urgent care center provides confidential, comprehensive testing services.</p>

          <h3>Available STD Tests</h3>
          <p>We offer testing for various sexually transmitted diseases, including:</p>
          <ul>
            <li>Chlamydia and Gonorrhea</li>
            <li>HIV and AIDS</li>
            <li>Syphilis</li>
            <li>Hepatitis B and C</li>
            <li>Herpes (HSV-1 and HSV-2)</li>
            <li>Human Papillomavirus (HPV)</li>
          </ul>

          <h3>When to Get Tested</h3>
          <p>Consider getting tested if you:</p>
          <ul>
            <li>Have new or multiple sexual partners</li>
            <li>Experience symptoms of an STD</li>
            <li>Have had unprotected sexual contact</li>
            <li>Are starting a new relationship</li>
            <li>Are pregnant or planning to become pregnant</li>
          </ul>

          <h3>Common STD Symptoms</h3>
          <p>Watch for these common symptoms that may indicate an STD:</p>
          <ul>
            <li>Unusual discharge or bleeding</li>
            <li>Pain or burning during urination</li>
            <li>Sores, bumps, or rashes in the genital area</li>
            <li>Itching or irritation</li>
            <li>Pelvic or abdominal pain</li>
            <li>Fever or flu-like symptoms</li>
          </ul>

          <h3>Treatment Options</h3>
          <p>Our treatment approach includes:</p>
          <ul>
            <li>Prescription antibiotics for bacterial infections</li>
            <li>Antiviral medications for viral infections</li>
            <li>Counseling and education</li>
            <li>Partner notification assistance</li>
            <li>Follow-up care and monitoring</li>
          </ul>

          <h3>Prevention and Education</h3>
          <p>Protect yourself by:</p>
          <ul>
            <li>Using protection during sexual activity</li>
            <li>Getting regular screenings</li>
            <li>Discussing sexual health with partners</li>
            <li>Staying informed about STD prevention</li>
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
  title: 'STD Testing & Treatment | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Get confidential STD testing and treatment at Twin Falls Urgent Care. Learn about available tests, symptoms, and treatment options for various sexually transmitted diseases.'
    }
  ]
})
</script>

<style scoped>
.article-content {
  @apply space-y-8;

  h2 {
    @apply text-3xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-400 bg-clip-text text-transparent;
  }

  h3 {
    @apply text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100;
  }

  p {
    @apply text-gray-700 dark:text-gray-300 leading-relaxed;
  }

  ul {
    @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 mt-2;
  }

  li {
    @apply flex items-start text-gray-700 dark:text-gray-300;
    &::before {
      content: "•";
      @apply text-blue-500 font-bold mr-1;
    }
  }
}

:deep(.prose) {
  @apply max-w-none;
}
</style>