<template>
  <NuxtPage />
</template>

<script setup>
useHead({
  titleTemplate: '%s | Urgent Care Twin Falls',
  meta: [
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { 
      name: 'description', 
      content: 'Urgent Care Twin Falls offers prompt, compassionate medical care for non-life-threatening illnesses and injuries in Twin Falls, Idaho.'
    }
  ],
  link: [
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap'
    }
  ]
})
</script>
