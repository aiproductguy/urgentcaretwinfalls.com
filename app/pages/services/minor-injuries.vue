<template>
  <NuxtLayout>
    <ServicePage
      title="Minor Injury Treatment at Twin Falls Urgent Care"
      description="Expert treatment for non-emergency injuries including sprains, cuts, burns, and minor fractures at Twin Falls Urgent Care."
      keywords="minor injuries, sprains, cuts, burns, fractures, urgent care treatment"
      image="/images/minor-injuries.jpg"
    >
      <p class="lead">
        When you experience a non-life-threatening injury, our skilled medical team is here to provide prompt, professional care. 
        We treat a wide range of minor injuries with the attention and expertise you deserve.
      </p>

      <h2>Common Injuries We Treat</h2>
      <ul>
        <li>
          <strong>Sprains & Strains</strong>
          <ul>
            <li>Ankle sprains</li>
            <li>Wrist injuries</li>
            <li>Muscle strains</li>
            <li>Sports-related injuries</li>
          </ul>
        </li>

        <li>
          <strong>Cuts & Wounds</strong>
          <ul>
            <li>Lacerations requiring stitches</li>
            <li>Minor cuts and scrapes</li>
            <li>Wound cleaning and dressing</li>
            <li>Tetanus shots when needed</li>
          </ul>
        </li>

        <li>
          <strong>Burns & Abrasions</strong>
          <ul>
            <li>First-degree burns</li>
            <li>Minor second-degree burns</li>
            <li>Road rash</li>
            <li>Skin abrasions</li>
          </ul>
        </li>

        <li>
          <strong>Minor Fractures & Breaks</strong>
          <ul>
            <li>Simple bone fractures</li>
            <li>Stress fractures</li>
            <li>X-ray diagnostics on-site</li>
            <li>Splinting and casting</li>
          </ul>
        </li>
      </ul>

      <h2>Our Treatment Approach</h2>
      <ol>
        <li>
          <strong>Quick Assessment</strong>
          <ul>
            <li>Immediate evaluation of your injury</li>
            <li>Pain management when needed</li>
            <li>Thorough examination by experienced providers</li>
          </ul>
        </li>

        <li>
          <strong>Advanced Care</strong>
          <ul>
            <li>State-of-the-art treatment facilities</li>
            <li>On-site X-ray capabilities</li>
            <li>Modern wound care techniques</li>
            <li>Professional splinting and casting</li>
          </ul>
        </li>

        <li>
          <strong>Follow-up Care</strong>
          <ul>
            <li>Detailed aftercare instructions</li>
            <li>Wound care guidance</li>
            <li>Recovery recommendations</li>
            <li>Follow-up scheduling if needed</li>
          </ul>
        </li>
      </ol>

      <h2>When to Choose Urgent Care</h2>
      <p>Visit us for minor injuries when:</p>
      <ul>
        <li>You need immediate care but it's not life-threatening</li>
        <li>Your primary care physician isn't available</li>
        <li>You want to avoid expensive emergency room visits</li>
        <li>You need after-hours care for injuries</li>
      </ul>

      <h2>When to Seek Emergency Care</h2>
      <p>Call 911 or visit the emergency room for:</p>
      <ul>
        <li>Severe bleeding that won't stop</li>
        <li>Deep wounds or amputations</li>
        <li>Suspected head, neck, or spine injuries</li>
        <li>Severe burns</li>
        <li>Broken bones protruding through skin</li>
      </ul>

      <h2>Insurance & Payment</h2>
      <p>
        We accept most major insurance plans and offer competitive self-pay rates. 
        Our staff can verify your coverage and explain any out-of-pocket costs before treatment.
      </p>

      <h2>Get Care Now</h2>
      <p>
        Don't let minor injuries become major problems. Walk in today or call 
        <a href="tel:+12087336700">(208) 733-6700</a> for immediate assistance. 
        Our experienced team is ready to help you recover quickly and safely.
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