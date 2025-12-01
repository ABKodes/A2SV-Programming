# TypeScript Todo List (Console Application)

This is a simple console-based Todo List application created using TypeScript. It allows users to add, complete, remove, and view tasks directly in the terminal.

## Features

- **Add Tasks**: Create new tasks to be added to the list.
- **Complete Tasks**: Mark tasks as complete.
- **Remove Tasks**: Delete tasks from the list using their ID.
- **Display Tasks**: View all current tasks with their completion status.

## How to Run

### Prerequisites

You must have [Node.js](https://nodejs.org/) and [TypeScript](https://www.typescriptlang.org/download) installed on your machine.

You can install TypeScript globally by running:
```bash
npm install -g typescript
```

### Steps

1.  **Clone the Repository**: Clone this repository to your local machine.
2.  **Navigate to the Directory**: Open a terminal and move into the project's root directory.
    ```bash
    cd path/to/your/project
    ```
3.  **Compile TypeScript**: Compile the `todo.ts` file into JavaScript. The `tsconfig.json` file will place the output in a `dist` folder.
    ```bash
    tsc
    ```
4.  **Run the Application**: Execute the compiled JavaScript file using Node.js.
    ```bash
    node dist/todo.js
    ```

You will see the output directly in your console, showing the process of adding, completing, and removing to-do items.

## Screenshots

Here is a screenshot of the application running in the console. It shows the output from initializing the list, adding tasks, completing one, and displaying the final list.

**Console Output**
*A screenshot of the terminal output after running the application with `node dist/todo.js`.*
![Console output of the TypeScript Todo List application](path/to/your/screenshot.png)