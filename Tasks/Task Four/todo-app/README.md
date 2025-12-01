# React TypeScript Todo App

A modern, functional Todo List application built with React and TypeScript. This project demonstrates the use of functional components, React Hooks (useState), and custom styling to create a fully interactive task manager.

## Features

- **Add Tasks**: Users can input new tasks to the list.
- **Edit Tasks**: Existing tasks can be updated in place with a seamless edit mode.
- **Delete Tasks**: Remove unwanted tasks from the list.
- **Toggle Completion**: Mark tasks as done/undone with visual feedback (strikethrough).
- **Responsive Design**: Clean, modern UI that works on different screen sizes.
- **Local State Management**: Uses React's `useState` to manage the application data.

## Technologies Used

- **React 18**: JavaScript library for building user interfaces.
- **TypeScript**: For type safety and better developer experience.
- **Vite**: Next Generation Frontend Tooling for fast development.
- **CSS3**: Custom styling using CSS variables and animations (no external UI libraries).

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Node.js (v14 or higher)
- npm (Node Package Manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ABKodes/react-ts-todo.git
   cd todo-app
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the Development Server**
   ```bash
   npm run dev
   ```

4. **Open in Browser**
   Click the link shown in your terminal (usually `http://localhost:5173`) to view the app.

## Project Structure

- **`src/components`**: Contains reusable UI components (`TodoInput`, `TodoItem`).
- **`src/types.ts`**: Defines the TypeScript interfaces (e.g., the `Todo` type).
- **`src/App.tsx`**: The main controller component that manages state and logic.
- **`src/App.css`**: Global styles and component-specific CSS.

## Usage

1. Type a task into the input field and press "Add Task" or hit Enter.
2. Click the checkbox to mark a task as completed.
3. Click "Edit" to modify the text of an existing task, then click "Save".
4. Click "Delete" to remove a task permanently.

## Author

- **ABKodes** - [GitHub Profile](https://github.com/ABKodes)