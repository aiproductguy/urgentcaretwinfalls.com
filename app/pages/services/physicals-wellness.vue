<template>
  <NuxtLayout>
    <ServicePage
      title="Physicals & Wellness Checkups at Twin Falls Urgent Care"
      description="Comprehensive physical examinations and wellness checkups for individuals, families, sports, and schools at Twin Falls Urgent Care."
      keywords="physical exam, wellness checkup, sports physical, school physical, medical examination"
      image="/images/physicals-wellness.jpg"
    >
      <p class="lead">
        Stay healthy and active with our comprehensive physical examinations and wellness checkups. 
        Our experienced medical team provides thorough evaluations to ensure your ongoing health and well-being.
      </p>

      <h2>Types of Physical Exams</h2>
      <ul>
        <li>
          <strong>Annual Physicals</strong>
          <ul>
            <li>Complete health assessment</li>
            <li>Vital signs monitoring</li>
            <li>Medical history review</li>
            <li>Preventive health screening</li>
          </ul>
        </li>

        <li>
          <strong>Sports Physicals</strong>
          <ul>
            <li>Athletic readiness assessment</li>
            <li>Musculoskeletal evaluation</li>
            <li>Cardiovascular screening</li>
            <li>Required documentation completion</li>
          </ul>
        </li>

        <li>
          <strong>School Physicals</strong>
          <ul>
            <li>Required health screenings</li>
            <li>Immunization review</li>
            <li>Growth and development check</li>
            <li>School form completion</li>
          </ul>
        </li>

        <li>
          <strong>Wellness Checkups</strong>
          <ul>
            <li>Preventive health screening</li>
            <li>Lifestyle assessment</li>
            <li>Health risk evaluation</li>
            <li>Wellness planning</li>
          </ul>
        </li>
      </ul>

      <h2>Our Examination Process</h2>
      <ol>
        <li>
          <strong>Health History Review</strong>
          <ul>
            <li>Medical history documentation</li>
            <li>Family health history</li>
            <li>Current medications review</li>
          </ul>
        </li>

        <li>
          <strong>Physical Examination</strong>
          <ul>
            <li>Vital signs measurement</li>
            <li>Body systems check</li>
            <li>Vision and hearing screening</li>
            <li>Physical fitness assessment</li>
          </ul>
        </li>

        <li>
          <strong>Health Assessment</strong>
          <ul>
            <li>Results discussion</li>
            <li>Preventive care recommendations</li>
            <li>Health goal setting</li>
            <li>Follow-up planning</li>
          </ul>
        </li>
      </ol>

      <h2>Additional Services</h2>
      <ul>
        <li>Immunization updates</li>
        <li>Lab testing when needed</li>
        <li>Health education resources</li>
        <li>Specialist referrals if required</li>
      </ul>

      <h2>What to Bring</h2>
      <ul>
        <li>Photo ID and insurance card</li>
        <li>Current medications list</li>
        <li>Medical history information</li>
        <li>Required forms (sports, school, etc.)</li>
        <li>Previous medical records (if available)</li>
      </ul>

      <h2>Insurance & Payment</h2>
      <p>
        We accept most major insurance plans and offer competitive self-pay rates. 
        Our staff will verify your coverage and explain any costs before your examination.
      </p>

      <h2>Schedule Your Physical</h2>
      <p>
        Stay on top of your health. Walk in today or call 
        <a :href="`tel:${contact.phone.replace(/\D/g, '')}`">{{ contact.phone }}</a> to schedule your physical. 
        Our team is ready to help you maintain optimal health and wellness.
      </p>
    </ServicePage>
  </NuxtLayout>
</template>

<script setup>
import ServicePage from '@/components/ServicePage.vue'

const { contact } = useClinicInfo()

definePageMeta({
  layout: 'default'
})
</script> 