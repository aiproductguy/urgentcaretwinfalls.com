<template>
  <NuxtLayout>
    <ServicePage
      title="Illness Treatment at Twin Falls Urgent Care"
      description="Comprehensive treatment for common illnesses and infections with experienced medical professionals at Twin Falls Urgent Care."
      keywords="illness treatment, infections, cold, flu, urgent care, medical care"
      image="/images/treating-illnesses.jpg"
    >
      <p class="lead">
        When illness strikes, you need prompt, professional care. Our experienced medical team provides 
        comprehensive treatment for a wide range of common illnesses and infections.
      </p>

      <h2>Common Illnesses We Treat</h2>
      <ul>
        <li>
          <strong>Respiratory Infections</strong>
          <ul>
            <li>Common cold</li>
            <li>Flu and influenza</li>
            <li>Bronchitis</li>
            <li>Sinus infections</li>
          </ul>
        </li>

        <li>
          <strong>Digestive Issues</strong>
          <ul>
            <li>Food poisoning</li>
            <li>Stomach viruses</li>
            <li>Nausea and vomiting</li>
            <li>Dehydration</li>
          </ul>
        </li>

        <li>
          <strong>Common Infections</strong>
          <ul>
            <li>Ear infections</li>
            <li>Urinary tract infections</li>
            <li>Strep throat</li>
            <li>Eye infections</li>
          </ul>
        </li>

        <li>
          <strong>Skin Conditions</strong>
          <ul>
            <li>Rashes</li>
            <li>Allergic reactions</li>
            <li>Minor infections</li>
            <li>Insect bites</li>
          </ul>
        </li>
      </ul>

      <h2>Our Treatment Approach</h2>
      <ol>
        <li>
          <strong>Thorough Evaluation</strong>
          <ul>
            <li>Comprehensive symptom assessment</li>
            <li>Medical history review</li>
            <li>Physical examination</li>
          </ul>
        </li>

        <li>
          <strong>Diagnostic Testing</strong>
          <ul>
            <li>Rapid strep tests</li>
            <li>Flu testing</li>
            <li>Lab work when needed</li>
            <li>Urinalysis</li>
          </ul>
        </li>

        <li>
          <strong>Treatment Plan</strong>
          <ul>
            <li>Prescription medications when needed</li>
            <li>Symptom management</li>
            <li>Recovery guidance</li>
            <li>Follow-up care recommendations</li>
          </ul>
        </li>
      </ol>

      <h2>When to Visit Us</h2>
      <p>Come to our urgent care when:</p>
      <ul>
        <li>Your symptoms are severe but not life-threatening</li>
        <li>You can't get an appointment with your regular doctor</li>
        <li>You need same-day treatment</li>
        <li>You want to avoid expensive ER visits</li>
      </ul>

      <h2>When to Seek Emergency Care</h2>
      <p>Visit the emergency room if you experience:</p>
      <ul>
        <li>Difficulty breathing</li>
        <li>Severe chest pain</li>
        <li>High fever with severe symptoms</li>
        <li>Signs of severe dehydration</li>
        <li>Loss of consciousness</li>
      </ul>

      <h2>Insurance & Payment</h2>
      <p>
        We accept most major insurance plans and offer affordable self-pay options. 
        Our staff will verify your coverage and explain any costs before treatment.
      </p>

      <h2>Get Treatment Today</h2>
      <p>
        Don't let illness keep you down. Walk in today or call 
        <a href="tel:+12087336700">(208) 733-6700</a> for immediate care. 
        Our team is ready to help you feel better fast.
      </p>
    </ServicePage>
  </NuxtLayout>
</template>

<script setup>
import ServicePage from '@/components/ServicePage.vue'

definePageMeta({
  layout: 'default'
})
</script> 