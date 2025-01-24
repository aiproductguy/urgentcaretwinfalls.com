<template>
  <NuxtLayout name="default">
    <div class="min-h-screen bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900 dark:to-gray-800/50">
      <main class="container mx-auto px-4 py-24">
        <ArticleTemplate
          title="Eye Injury & Foreign Object Removal Guide"
          description="Learn about eye injury first aid, when to seek urgent care, and professional foreign object removal."
          date="January 14, 2024"
          icon="mdi:eye-plus"
          :relatedArticles="[
            {
              path: '/articles/first-aid-basics',
              title: 'First Aid Basics',
              description: 'Essential first aid knowledge for common emergencies'
            },
            {
              path: '/articles/workplace-safety',
              title: 'Workplace Safety Guide',
              description: 'Preventing workplace injuries and maintaining safety'
            },
            {
              path: '/articles/emergency-care',
              title: 'Emergency Care Tips',
              description: 'When and how to seek emergency medical attention'
            }
          ]"
        >
          <h2>Types of Eye Injuries</h2>
          <p>Eye injuries can range from minor irritations to serious medical emergencies. Common types include:</p>
          <ul>
            <li>Foreign objects in the eye</li>
            <li>Chemical exposure</li>
            <li>Scratches or abrasions</li>
            <li>Blunt trauma</li>
            <li>Burns from UV exposure</li>
          </ul>

          <h3>Immediate First Aid Steps</h3>
          <p>If you experience an eye injury, follow these steps:</p>
          <ul>
            <li>Do not rub or touch the injured eye</li>
            <li>Blink repeatedly to help remove small particles</li>
            <li>Flush with clean water for chemical exposure</li>
            <li>Keep both eyes closed if possible</li>
            <li>Seek immediate medical attention</li>
          </ul>

          <h3>When to Seek Urgent Care</h3>
          <p>Visit our urgent care immediately if you experience:</p>
          <ul>
            <li>Persistent foreign body sensation</li>
            <li>Severe pain or discomfort</li>
            <li>Vision changes or blurriness</li>
            <li>Chemical burns or exposure</li>
            <li>Bleeding or discharge from the eye</li>
            <li>Difficulty opening or closing the eye</li>
          </ul>

          <h3>Professional Treatment Options</h3>
          <p>Our medical team provides comprehensive eye care including:</p>
          <ul>
            <li>Foreign object removal</li>
            <li>Treatment for corneal abrasions</li>
            <li>Chemical exposure treatment</li>
            <li>Prescription eye medications</li>
            <li>Referral to specialists when needed</li>
          </ul>

          <h3>Foreign Object Removal</h3>
          <p>Our professional removal process includes:</p>
          <ul>
            <li>Thorough eye examination</li>
            <li>Safe removal techniques</li>
            <li>Post-removal care</li>
            <li>Prevention of infection</li>
            <li>Follow-up instructions</li>
          </ul>

          <h3>Prevention Tips</h3>
          <p>Protect your eyes by:</p>
          <ul>
            <li>Wearing appropriate eye protection</li>
            <li>Using proper safety equipment at work</li>
            <li>Avoiding rubbing your eyes</li>
            <li>Regular eye check-ups</li>
            <li>Being aware of environmental hazards</li>
          </ul>

          <h3>After-Care Instructions</h3>
          <p>Follow these guidelines after treatment:</p>
          <ul>
            <li>Use prescribed medications as directed</li>
            <li>Avoid touching or rubbing the eye</li>
            <li>Wear protective eyewear if recommended</li>
            <li>Attend follow-up appointments</li>
            <li>Monitor for signs of infection</li>
          </ul>
        </ArticleTemplate>
      </main>
    </div>
  </NuxtLayout>
</template>

<script setup>
useHead({
  title: 'Eye Injury & Foreign Object Removal | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Get immediate care for eye injuries and foreign object removal at Twin Falls Urgent Care. Learn about first aid steps, treatment options, and prevention.'
    }
  ]
})
</script>