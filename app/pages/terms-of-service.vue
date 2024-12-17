<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
    <main class="container mx-auto px-4 py-16">
      <div class="prose prose-sm max-w-3xl mx-auto dark:prose-invert">
        <h1 class="text-gradient mb-4 text-4xl font-bold">Terms of Service</h1>

        <p class="my-2">Welcome to Twin Falls Urgent Care. By accessing and using our website, you agree to comply with and be bound by the following terms and conditions.</p>

        <h2 class="mt-6 mb-2 text-2xl">Agreement to Terms</h2>
        <p class="my-2">By accessing our website, you agree to be bound by these Terms of Service and to comply with all applicable laws and regulations. If you do not agree with any of these terms, you are prohibited from using or accessing this site.</p>

        <h2 class="mt-6 mb-2 text-2xl">Medical Disclaimer</h2>
        <p class="my-2">The content on this website is for informational purposes only and should not be considered medical advice. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.</p>

        <h2 class="mt-6 mb-2 text-2xl">Website Use</h2>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>The content of this website is for your general information and use only</li>
          <li>We reserve the right to modify or discontinue any aspect of our website at any time</li>
          <li>Your use of any information on this website is entirely at your own risk</li>
        </ul>

        <h2 class="mt-6 mb-2 text-2xl">Privacy Policy</h2>
        <p class="my-2">Your use of our website is also governed by our Privacy Policy. Please review our <NuxtLink to="/privacy-policy" class="text-blue-600 hover:text-blue-800">Privacy Policy</NuxtLink>, which also governs the Site and informs users of our data collection practices.</p>

        <h2 class="mt-6 mb-2 text-2xl">Accuracy of Information</h2>
        <p class="my-1">While we strive to provide accurate and up-to-date information:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>We make no representations about the completeness, accuracy, reliability, or suitability of the information provided</li>
          <li>Any reliance you place on such information is strictly at your own risk</li>
          <li>We reserve the right to correct any errors or omissions in any portion of the website</li>
        </ul>

        <h2 class="mt-6 mb-2 text-2xl">Intellectual Property</h2>
        <p class="my-2">Unless otherwise stated, we own the intellectual property rights for all material on this website. All intellectual property rights are reserved. You may view and/or print pages from the website for your own personal use subject to restrictions.</p>

        <h2 class="mt-6 mb-2 text-2xl">Limitations of Liability</h2>
        <p class="my-2">In no event shall Twin Falls Urgent Care be liable for any damages (including, without limitation, damages for loss of data or profit) arising out of the use or inability to use the materials on our website.</p>

        <h2 class="mt-6 mb-2 text-2xl">Changes to Terms</h2>
        <p class="my-2">We reserve the right to revise these terms of service at any time without notice. By using this website, you agree to be bound by the current version of these Terms of Service.</p>

        <h2 class="mt-6 mb-2 text-2xl">Contact Information</h2>
        <p class="my-1">If you have any questions about these Terms of Service, please contact us:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Phone: 208-244-0146</li>
          <li>Address: 260 Falls Avenue, Suite C, Twin Falls, ID 83301</li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script setup>
useHead({
  title: 'Terms of Service | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Terms of Service for Twin Falls Urgent Care - Understand our website usage terms, medical disclaimers, and service conditions.'
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
</style> 