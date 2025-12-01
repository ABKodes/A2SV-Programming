# Job Finder Dashboard (Task 7)

A dynamic Job Listing application that fetches real-time data from the Akil Backend API. This project demonstrates proficiency in React Hooks (`useEffect`, `useState`), API integration, error handling, and modern UI styling with Tailwind CSS.

## Features

- **Live Data Integration**: Fetches job opportunities from `https://akil-backend.onrender.com/`.
- **Loading States**: Displays a spinner while data is being fetched.
- **Error Handling**: Gracefully handles network errors or API failures with user feedback.
- **Dynamic Rendering**: Maps API data to reusable `JobCard` components.
- **Responsive Design**: Fully responsive layout optimized for all devices.

## API Endpoint Used

- **GET** `/opportunities/search`: Retrieves the list of available job opportunities.

## Tech Stack

- **React (Vite)**: Frontend framework.
- **TypeScript**: For strict typing of API responses.
- **Tailwind CSS**: Styling framework.
- **Fetch API**: Native browser API for network requests.

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd job-listing-app
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the Development Server**
   ```bash
   npm run dev
   ```
   Open your browser to `http://localhost:5173`.

## Screenshots

### Dashboard with API Data
![Dashboard Screenshot](./screenshot.png)

## Author

- **ABKodes**