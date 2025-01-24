<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <main class="container mx-auto px-4 py-16">
        <ArticleTemplate
          title="Ingrown Toenail Treatment: Relief and Care Guide"
          description="Expert guidance on treating ingrown toenails, prevention tips, and when to seek professional care."
          date="January 14, 2024"
          icon="mdi:foot-print"
          :relatedArticles="[
            {
              path: '/articles/foot-pain-guide',
              title: 'Foot Pain Guide',
              description: 'Understanding and treating different types of foot pain'
            },
            {
              path: '/articles/wound-care-guide',
              title: 'Wound Care Guide',
              description: 'Essential tips for proper wound treatment and healing'
            },
            {
              path: '/articles/diabetes-foot-care',
              title: 'Diabetes Foot Care',
              description: 'Special considerations for diabetic foot health'
            }
          ]"
        >
          <h2>Understanding Ingrown Toenails</h2>
          <p>An ingrown toenail occurs when the edge of the nail grows into the surrounding skin, causing pain, swelling, and potential infection.</p>

          <h3>Common Causes</h3>
          <p>Ingrown toenails can be caused by various factors:</p>
          <ul>
            <li>Improper nail trimming techniques</li>
            <li>Tight or ill-fitting shoes</li>
            <li>Injury to the toe</li>
            <li>Genetic predisposition</li>
            <li>Poor foot hygiene</li>
          </ul>

          <h3>Symptoms to Watch For</h3>
          <p>Common symptoms include:</p>
          <ul>
            <li>Pain and tenderness along the nail edges</li>
            <li>Redness around the toenail</li>
            <li>Swelling of the toe</li>
            <li>Warmth in the affected area</li>
            <li>Pus or drainage if infected</li>
          </ul>

          <h3>When to Seek Medical Care</h3>
          <p>Visit our urgent care if you experience:</p>
          <ul>
            <li>Severe pain that limits daily activities</li>
            <li>Signs of infection (pus, warmth, fever)</li>
            <li>Redness spreading beyond the toe</li>
            <li>Diabetes or poor circulation</li>
            <li>Failed home treatment attempts</li>
          </ul>

          <h3>Professional Treatment Options</h3>
          <p>Our medical team provides several treatment options:</p>
          <ul>
            <li>Partial nail removal for immediate relief</li>
            <li>Antibiotics for infections</li>
            <li>Professional nail trimming</li>
            <li>Chemical or surgical matrixectomy</li>
            <li>Preventive care education</li>
          </ul>

          <h3>Prevention Tips</h3>
          <p>Prevent future ingrown toenails by:</p>
          <ul>
            <li>Trimming nails straight across</li>
            <li>Wearing properly fitted shoes</li>
            <li>Keeping feet clean and dry</li>
            <li>Protecting toes from injury</li>
            <li>Regular foot care and inspection</li>
          </ul>

          <h3>Home Care Measures</h3>
          <p>For mild cases, try these home remedies:</p>
          <ul>
            <li>Warm water soaks</li>
            <li>Over-the-counter pain relievers</li>
            <li>Wearing open-toed shoes</li>
            <li>Gentle massage of the affected area</li>
            <li>Proper hygiene maintenance</li>
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
  title: 'Ingrown Toenail Treatment | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Get expert treatment for ingrown toenails at Twin Falls Urgent Care. Learn about causes, symptoms, prevention, and when to seek professional care.'
    }
  ]
})
</script>

<style scoped>
.article-content {
  @apply grid gap-8;

  h2 {
    @apply text-3xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-gray-600 bg-clip-text text-transparent;
  }

  h3 {
    @apply text-2xl font-bold mb-4 text-gray-900 dark:text-white;
  }

  ul {
    @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 my-2;
    
    @media (max-width: 768px) {
      grid-template-columns: repeat(2, 1fr);
    }
    
    @media (max-width: 640px) {
      grid-template-columns: 1fr;
    }
  }

  li {
    @apply flex items-start text-gray-700 dark:text-gray-300;
    &::before {
      content: "•";
      @apply text-blue-500 font-bold mr-1;
    }
  }
}
</style>