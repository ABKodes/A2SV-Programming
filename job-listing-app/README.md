# Job Listing App (Final Task)

A comprehensive Job Listing Dashboard built with React, TypeScript, and Tailwind CSS. This project features full user authentication, real-time API data fetching, bookmarking functionality, and a robust testing suite.

## Features

- **User Authentication**:
  - Sign Up with Email Verification (OTP).
  - Secure Login with JWT handling.
  - Auto-logout and session management.
- **Job Dashboard**:
  - Browse job opportunities fetched from a live backend.
  - Dynamic routing and error handling.
- **Bookmarking System**:
  - Authenticated users can bookmark/unbookmark jobs.
  - Bookmarks persist across sessions via the API.
- **Testing**:
  - **Unit Tests**: Component testing using Jest & React Testing Library.
  - **E2E Tests**: Full user flow testing using Cypress.

## Tech Stack

- **Frontend**: React, Vite, TypeScript
- **Styling**: Tailwind CSS
- **State**: React Context API
- **Testing**: Jest, Cypress

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd job-listing-app
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the Application**
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`.

## How to Run Tests

### 1. Unit Tests (Jest)
Tests the rendering and logic of individual components (e.g., `JobCard`).
```bash
npm test
```

### 2. End-to-End Tests (Cypress)
Tests the complete user flow: Login -> View Jobs -> Bookmark a Job.
*Make sure the app is running (`npm run dev`) in a separate terminal before starting Cypress.*
```bash
npx cypress open
```
Select **E2E Testing** -> **Chrome** -> Click **`bookmark.cy.ts`**.

## Screenshots

### 1. Dashboard (Home)
*(Add a screenshot of the home page showing job cards)*
![Home Page](./screenshots/home.png)

### 2. Login & Signup
*(Add a screenshot of the login form)*
![Login Page](./screenshots/login.png)

### 3. Bookmarked State
*(Add a screenshot showing a job card with the filled bookmark icon)*
![Bookmark Example](./screenshots/bookmark.png)

### 4. Test Results
*(Add a screenshot of your passing Jest or Cypress terminal)*
![Tests](./screenshots/tests.png)

## Author

- **ABKodes**