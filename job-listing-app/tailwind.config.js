/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#4640DE',
        secondary: '#E5E6EC',
        accent: '#FFB836',
        slate: {
          800: '#25324B',
          600: '#515B6F',
          50: '#F8F9FC'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}