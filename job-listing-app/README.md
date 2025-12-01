# Job Listing Dashboard (Task 6)

A responsive React Job Listing application styled with Tailwind CSS. This dashboard displays a list of available job opportunities with detailed cards including company logos, tags, and descriptions.

## Features

- **Responsive Job Cards**: Custom-designed components using Flexbox and Grid.
- **Dynamic Data**: Renders job lists from a JSON source (`jobs.json`).
- **Tailwind Styling**: Uses utility classes for hover states, typography, and layout (no external CSS files).
- **Avatar Integration**: Displays company logos/avatars dynamically.
- **Modern UI**: Includes badges, bookmark icons, and applicant counters.

## Tech Stack

- **React (Vite)**: Frontend framework.
- **TypeScript**: For static typing and safety.
- **Tailwind CSS**: Utility-first CSS framework for styling.

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

## Project Structure

- `src/components/JobCard.tsx`: The reusable card component displaying individual job details.
- `src/assets/jobs.json`: The dummy data source mimicking an API response.
- `src/types.ts`: TypeScript interfaces defining the shape of the Job data.
- `src/App.tsx`: The main dashboard layout containing the header and the grid of job cards.

## Screenshot

![Dashboard Screenshot](./screenshot.png)

*(Note: This project includes a `screenshot.png` file in the root directory demonstrating the running application.)*

## Author

- **ABKodes**