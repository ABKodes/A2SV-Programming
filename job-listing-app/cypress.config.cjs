const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    // This is the url your vite server runs on
    baseUrl: 'http://localhost:5173', 
  },
});