# Job Listing App with Authentication (Task 8)

This project is a robust Job Listing Dashboard built with React and TypeScript. It features full user authentication (Signup, Email Verification, Login) integrated with a live backend API, along with a dynamic job feed managed by React Context.

## Features

- **User Authentication**:
  - **Sign Up**: Users can register a new account via the API.
  - **Email Verification**: Includes an OTP verification step immediately after signup.
  - **Login**: Secure login using JWT tokens stored in LocalStorage.
  - **Logout**: proper session clearing.
- **Job Dashboard**: Fetches and displays job opportunities from the Akil Backend API.
- **Global State Management**: Uses React Context API to manage authentication status across the app.
- **Form Handling**: Robust client-side validation using `react-hook-form`.
- **Responsive Design**: Professional UI styled with Tailwind CSS.

## Tech Stack

- **Frontend**: React (Vite), TypeScript
- **Styling**: Tailwind CSS
- **Routing**: React Router DOM
- **State Management**: React Context API
- **Forms**: React Hook Form

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd job-listing-app
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the App**
   ```bash
   npm run dev
   ```
   Access the app at `http://localhost:5173`.

## Project Structure

- **`src/pages/`**:
  - `Home.tsx`: Main dashboard showing the job list.
  - `Login.tsx`: Login form handling authentication tokens.
  - `Signup.tsx`: Two-step registration process (Sign up -> Verify OTP).
- **`src/context/AuthContext.tsx`**: Centralized logic for managing user sessions and tokens.
- **`src/components/JobCard.tsx`**: Reusable UI component for job items.
- **`src/App.tsx`**: Main router configuration.

## API Endpoints Used

- `POST /signup`: Register a new user.
- `POST /verify-email`: Verify the user via OTP.
- `POST /login`: Authenticate and receive an access token.
- `GET /opportunities/search`: Fetch the list of jobs.

## Screenshots

### Dashboard (Home)
![Home Page](./screenshots/home.png)

### Signup & Verification
![Signup Page](./screenshots/signup.png)

### Login
![Login Page](./screenshots/login.png)

## Author

- **ABKodes**