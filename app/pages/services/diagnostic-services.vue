<template>
  <NuxtLayout>
    <ServicePage
      title="Diagnostic Services at Twin Falls Urgent Care"
      description="Comprehensive diagnostic testing and laboratory services for accurate medical diagnosis at Twin Falls Urgent Care."
      keywords="diagnostic testing, lab services, medical tests, blood work, urinalysis, rapid testing"
    >
      <div class="flex items-center gap-4 mb-6">
        <Icon icon="healthicons:diagnostic" class="h-12 w-12 text-blue-600" />
        <p class="lead">
          Get fast, accurate diagnostic results with our comprehensive testing services. 
          Our on-site laboratory and diagnostic capabilities help ensure quick diagnosis and treatment.
        </p>
      </div>

      <h2>Available Diagnostic Tests</h2>
      <ul>
        <li>
          <strong>Laboratory Services</strong>
          <ul>
            <li>Blood tests</li>
            <li>Urinalysis</li>
            <li>Strep testing</li>
            <li>Flu testing</li>
          </ul>
        </li>

        <li>
          <strong>Rapid Testing</strong>
          <ul>
            <li>COVID-19 testing</li>
            <li>Rapid strep tests</li>
            <li>Influenza testing</li>
            <li>Pregnancy testing</li>
          </ul>
        </li>

        <li>
          <strong>Specialized Tests</strong>
          <ul>
            <li>STD screening</li>
            <li>Mono testing</li>
            <li>Drug screening</li>
            <li>Allergy testing</li>
          </ul>
        </li>

        <li>
          <strong>Other Diagnostics</strong>
          <ul>
            <li>EKG/ECG</li>
            <li>Pulse oximetry</li>
            <li>Vision screening</li>
            <li>Hearing tests</li>
          </ul>
        </li>
      </ul>

      <h2>Our Diagnostic Process</h2>
      <ol>
        <li>
          <strong>Initial Consultation</strong>
          <ul>
            <li>Symptom evaluation</li>
            <li>Medical history review</li>
            <li>Test determination</li>
          </ul>
        </li>

        <li>
          <strong>Testing Procedure</strong>
          <ul>
            <li>Sample collection</li>
            <li>Professional handling</li>
            <li>Rapid processing</li>
            <li>Quality control measures</li>
          </ul>
        </li>

        <li>
          <strong>Results & Follow-up</strong>
          <ul>
            <li>Quick result turnaround</li>
            <li>Clear result explanation</li>
            <li>Treatment planning</li>
            <li>Specialist referral if needed</li>
          </ul>
        </li>
      </ol>

      <h2>Why Choose Our Diagnostic Services</h2>
      <ul>
        <li>Fast result turnaround</li>
        <li>Experienced lab technicians</li>
        <li>Comprehensive testing options</li>
        <li>Accurate, reliable results</li>
      </ul>

      <h2>Common Conditions We Diagnose</h2>
      <ul>
        <li>Infections and viruses</li>
        <li>Allergies and sensitivities</li>
        <li>Chronic conditions</li>
        <li>Hormonal imbalances</li>
        <li>Cardiovascular issues</li>
      </ul>

      <h2>Insurance & Payment</h2>
      <p>
        We accept most major insurance plans and offer competitive self-pay rates for diagnostic services. 
        Our staff will verify your coverage and explain any costs before testing.
      </p>

      <h2>Get Tested Today</h2>
      <p>
        Need diagnostic testing? Walk in today or call 
        <a :href="`tel:${contact.phone.replace(/\D/g, '')}`">{{ contact.phone }}</a> for immediate service. 
        Our diagnostic team is ready to provide you with fast, accurate results.
      </p>

      <div class="mt-8">
        <h3>Related Services</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <NuxtLink to="/services/minor-injuries" class="group p-4 border rounded-lg hover:bg-gray-50">
            <div class="flex items-center gap-2">
              <Icon icon="material-symbols:medical-services" class="h-6 w-6 text-blue-600" />
              <span>Minor Injuries Treatment</span>
            </div>
          </NuxtLink>
          <NuxtLink to="/services/treating-illnesses" class="group p-4 border rounded-lg hover:bg-gray-50">
            <div class="flex items-center gap-2">
              <Icon icon="healthicons:virus" class="h-6 w-6 text-blue-600" />
              <span>Illness Treatment</span>
            </div>
          </NuxtLink>
          <NuxtLink to="/services/xray-imaging" class="group p-4 border rounded-lg hover:bg-gray-50">
            <div class="flex items-center gap-2">
              <Icon icon="healthicons:radiology" class="h-6 w-6 text-blue-600" />
              <span>X-ray & Imaging</span>
            </div>
          </NuxtLink>
          <NuxtLink to="/services/physicals-wellness" class="group p-4 border rounded-lg hover:bg-gray-50">
            <div class="flex items-center gap-2">
              <Icon icon="healthicons:doctor" class="h-6 w-6 text-blue-600" />
              <span>Physicals & Wellness</span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </ServicePage>
  </NuxtLayout>
</template>

<script setup>
import { Icon } from '@iconify/vue'
import ServicePage from '@/components/ServicePage.vue'

const { contact } = useClinicInfo()

definePageMeta({
  layout: 'default'
})
</script> 