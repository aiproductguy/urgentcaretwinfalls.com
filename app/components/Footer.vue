<template>
  <footer class="bg-gray-100 dark:bg-gray-800 py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <h3 class="font-bold text-lg mb-4">Contact Us</h3>
          <address class="not-italic">
            <p>1234 Main Street</p>
            <p>Twin Falls, ID 83301</p>
            <p class="mt-2">
              <a href="tel:+12085551234" class="hover:text-primary-500">
                (208) 555-1234
              </a>
            </p>
          </address>
        </div>
        <div>
          <h3 class="font-bold text-lg mb-4">Services</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="/services/minor-injuries">Minor Injuries</NuxtLink></li>
            <li><NuxtLink to="/services/illnesses">Illnesses</NuxtLink></li>
            <li><NuxtLink to="/services/physicals">Physicals & Wellness</NuxtLink></li>
            <li><NuxtLink to="/services/xray">X-Ray & Imaging</NuxtLink></li>
          </ul>
        </div>
        <div>
          <h3 class="font-bold text-lg mb-4">Hours</h3>
          <ul class="space-y-2">
            <li>Monday - Friday: 8am - 8pm</li>
            <li>Saturday: 9am - 6pm</li>
            <li>Sunday: 10am - 4pm</li>
          </ul>
        </div>
        <div>
          <h3 class="font-bold text-lg mb-4">Follow Us</h3>
          <div class="flex space-x-4">
            <a href="#" class="hover:text-primary-500">
              <Icon name="ion:logo-facebook" class="w-6 h-6" />
            </a>
            <a href="#" class="hover:text-primary-500">
              <Icon name="ion:logo-twitter" class="w-6 h-6" />
            </a>
            <a href="#" class="hover:text-primary-500">
              <Icon name="ion:logo-instagram" class="w-6 h-6" />
            </a>
          </div>
        </div>
      </div>
      <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700 text-center">
        <p>&copy; {{ new Date().getFullYear() }} Urgent Care of Twin Falls. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template> 