# React Contact Form with useForm

This project is a responsive Contact Form application built with React, TypeScript, and the `react-hook-form` library. It demonstrates efficient form state management and validation without using heavy external UI libraries.

## Features

- **Form State Management**: Uses the `useForm` hook to handle inputs efficiently.
- **Validation**:
  - **Name**: Required, minimum 2 characters.
  - **Email**: Required, validates standard email format (Regex).
  - **Message**: Required, minimum 10 characters.
- **Error Handling**: Displays dynamic error messages below invalid fields.
- **Responsive UI**: Clean, modern design that works on mobile and desktop.

## Technologies Used

- **React**: Component-based UI library.
- **TypeScript**: For type safety.
- **React Hook Form**: Performance-focused library for form validation.
- **Vite**: Fast build tool.
- **CSS**: Custom styling.

## How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd contact-form
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the Development Server**
   ```bash
   npm run dev
   ```

4. **Access the App**
   Open your browser to `http://localhost:5173` (or the port shown in your terminal).

## Project Structure

- **`src/components/ContactForm.tsx`**: Contains the `useForm` logic and JSX structure.
- **`src/components/ContactForm.css`**: Styles specific to the form card.
- **`src/App.tsx`**: Main entry point rendering the form.

## Author

- **ABKodes**