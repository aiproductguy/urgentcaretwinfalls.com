<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <main class="container mx-auto px-4 py-16">
        <ArticleTemplate
          title="Skin Rash Treatment Guide: When to Seek Urgent Care"
          description="Know when to seek urgent care for rashes and learn about common causes, treatments, and prevention."
          date="January 14, 2024"
          icon="mdi:bandage"
          :relatedArticles="[
            {
              path: '/articles/wound-care-laceration-treatment',
              title: 'Wound Care & Laceration Treatment',
              description: 'Professional wound care services and treatment guidelines.'
            },
            {
              path: '/articles/eye-injury-foreign-object-removal',
              title: 'Eye Injury & Foreign Object Removal',
              description: 'Expert care for eye injuries and foreign object removal.'
            },
            {
              path: '/articles/asthma-treatment-urgent-care',
              title: 'Asthma Treatment & Care',
              description: 'Get immediate relief with nebulizer treatments and expert care.'
            }
          ]"
        >
          <h2>Understanding Skin Rashes</h2>
          <p>Rashes can range from minor irritations to signs of serious health issues. Knowing when to seek urgent care is essential for preventing complications.</p>

          <h3>Common Causes of Rashes</h3>
          <p>Rashes can be caused by various factors, including:</p>
          <ul>
            <li>Allergic reactions</li>
            <li>Infections</li>
            <li>Contact with irritants</li>
            <li>Chronic skin conditions</li>
            <li>Heat and excessive sweating</li>
            <li>Conditions like hives, chickenpox, and eczema</li>
          </ul>

          <h3>When to Seek Urgent Care</h3>
          <p>Visit urgent care immediately if you experience any of these symptoms:</p>
          <ul>
            <li>Severe itching or discomfort that persists</li>
            <li>Blistering or oozing that may indicate infection</li>
            <li>Rapid spread of the rash</li>
            <li>Fever accompanying the rash</li>
            <li>Swelling or breathing difficulties</li>
            <li>Intense pain in the affected area</li>
          </ul>

          <h3>Treatment at Urgent Care Centers</h3>
          <p>Our urgent care center provides comprehensive rash treatment including:</p>
          <ul>
            <li>Quick assessment of symptoms</li>
            <li>Diagnostic testing when needed</li>
            <li>Prescription medications (antibiotics, antihistamines, steroid creams)</li>
            <li>Referrals to specialists if necessary</li>
          </ul>

          <h3>Preventive Measures and Home Care</h3>
          <p>For mild rashes, consider these home care strategies:</p>
          <ul>
            <li>Regular moisturizing, especially for eczema</li>
            <li>Avoiding known irritants and allergens</li>
            <li>Using cool compresses for itchy or inflamed skin</li>
            <li>Applying over-the-counter remedies as appropriate</li>
          </ul>

          <h3>When to See a Doctor</h3>
          <p>Don't hesitate to seek medical attention if your rash:</p>
          <ul>
            <li>Persists for more than a few days</li>
            <li>Shows signs of infection</li>
            <li>Spreads rapidly</li>
            <li>Is accompanied by other concerning symptoms</li>
          </ul>
        </ArticleTemplate>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
useHead({
  title: 'Skin Rash Treatment Guide | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Learn when to seek urgent care for rashes, understand common causes, and get expert treatment advice from Twin Falls Urgent Care professionals.'
    }
  ]
})
</script>

<style scoped>
:deep(.article-content) {
  @apply grid gap-8;

  h2 {
    @apply text-3xl font-bold mb-6 text-gray-900 dark:text-gray-100;
  }

  h3 {
    @apply text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100;
  }

  p {
    @apply text-lg text-gray-700 dark:text-gray-300 leading-relaxed;
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
</style> 