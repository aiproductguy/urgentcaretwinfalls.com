<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
    <main class="container mx-auto px-4 py-16">
      <div class="prose prose-sm max-w-3xl mx-auto dark:prose-invert">
        <h1 class="text-gradient mb-4 text-4xl font-bold">Privacy Policy</h1>

        <p class="my-2">We are committed to protecting your privacy and providing a safe online experience. This Privacy Statement applies to our Practice's website and governs our data collection and usage practices. By using this website, you consent to the data practices described herein.</p>

        <h2 class="mt-6 mb-2 text-2xl">Collection of Personal Information</h2>

        <h3 class="mt-4 mb-1 text-xl">Information You Provide</h3>
        <p class="my-1">We collect personally identifiable information that you voluntarily provide, such as:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Email address</li>
          <li>Name</li>
          <li>Home or work address</li>
          <li>Telephone number</li>
        </ul>

        <h3 class="mt-4 mb-1 text-xl">Automatically Collected Information</h3>
        <p class="my-1">We also collect:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Anonymous demographic information (e.g., ZIP code, age, preferences)</li>
          <li>Computer hardware and software information (e.g., IP address, browser type, domain names, access times, referring website addresses)</li>
        </ul>

        <h2 class="mt-6 mb-2 text-2xl">Use of Personal Information</h2>
        <p class="my-1">We use your personal information to:</p>
        <ol class="my-1 list-decimal pl-6 space-y-0">
          <li>Operate our website and deliver requested services</li>
          <li>Inform you about other products or services from our Practice and affiliates</li>
          <li>Conduct research surveys about our services</li>
        </ol>

        <h3 class="mt-4 mb-1 text-xl">Third-Party Sharing</h3>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>We do not sell, rent, or lease customer lists to third parties</li>
          <li>We may share data with trusted partners for specific purposes (e.g., statistical analysis, email/postal mail, customer support, deliveries)</li>
          <li>All third parties are prohibited from using your personal information except to provide these services and must maintain confidentiality</li>
        </ul>

        <h3 class="mt-4 mb-1 text-xl">Legal Compliance and HIPAA</h3>
        <p class="my-2">We will disclose your personal information, without notice, only if required to do so by law. As a healthcare provider, we are subject to the Health Insurance Portability and Accountability Act (HIPAA) and comply with its requirements for lawful disclosures of protected health information (PHI).</p>

        <h2 class="mt-6 mb-2 text-2xl">Use of Cookies</h2>
        <p class="my-1">Our website may use "cookies" to personalize your online experience. Cookies are:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Text files placed on your hard disk by a webpage server</li>
          <li>Uniquely assigned to you</li>
          <li>Can only be read by a web server in the domain that issued the cookie</li>
        </ul>

        <h2 class="mt-6 mb-2 text-2xl">Security Measures</h2>
        <p class="my-1">We secure your personal information from unauthorized access, use, or disclosure by:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Storing personally identifiable information on computer servers in a controlled, secure environment</li>
          <li>Protecting transmitted sensitive information (e.g., credit card numbers) through encryption protocols like SSL</li>
        </ul>

        <h2 class="mt-6 mb-2 text-2xl">Updates to This Statement</h2>
        <p class="my-2">We occasionally update this Privacy Statement to reflect company and customer feedback. We encourage you to periodically review this statement to stay informed about how we protect your information.</p>

        <h2 class="mt-6 mb-2 text-2xl">Contact Information</h2>
        <p class="my-1">For questions or concerns, please contact us:</p>
        <ul class="my-1 list-disc pl-6 space-y-0">
          <li>Phone: 208-244-0146</li>
          <li>Mail: 260 Falls Avenue, Suite C, Twin Falls, ID 83301</li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script setup>
useHead({
  title: 'Privacy Policy | Twin Falls Urgent Care',
  meta: [
    {
      name: 'description',
      content: 'Privacy Policy for Twin Falls Urgent Care - Learn about how we protect your personal information and comply with HIPAA regulations.'
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