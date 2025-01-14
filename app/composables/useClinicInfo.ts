import type { RuntimeConfig } from 'nuxt/schema'

interface Address {
  street: string
  city: string
  state: string
  zip: string
}

interface Contact {
  address: Address
  phone: string
  email: string
  googleMapsUrl: string
}

interface Hours {
  weekdays: {
    open: string
    close: string
  }
  weekend: string
  holidays: string
  shortSchedule: string
  longSchedule: string[]
}

interface PublicRuntimeConfig {
  contact: Contact
  hours: Hours
  baseURL: string
}

export const useClinicInfo = () => {
  const config = useRuntimeConfig()
  
  const formatAddress = () => {
    const contact = config.public.contact as Contact
    const { street, city, state, zip } = contact.address
    return `${street}, ${city}, ${state} ${zip}`
  }

  const isOpen = () => {
    const now = new Date()
    const day = now.getDay()
    const hour = now.getHours()
    const minutes = now.getMinutes()
    const currentTime = hour * 60 + minutes

    // Weekend check
    if (day === 0 || day === 6) return false

    // Weekday hours check (8:00 AM - 5:00 PM)
    const openTime = 8 * 60  // 8:00 AM in minutes
    const closeTime = 17 * 60 // 5:00 PM in minutes

    return currentTime >= openTime && currentTime < closeTime
  }

  return {
    contact: config.public.contact as Contact,
    hours: config.public.hours as Hours,
    formatAddress,
    isOpen,
    googleMapsUrl: (config.public.contact as Contact).googleMapsUrl
  }
} 