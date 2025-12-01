// Define the structure of a to-do item
interface ToDo {
    id: number;
    task: string;
    completed: boolean;
}

// A class to manage the list of to-do items
class ToDoList {
    private todos: ToDo[] = [];
    private nextId: number = 1;

    // Add a new to-do item
    add(task: string): ToDo {
        const newToDo: ToDo = {
            id: this.nextId++,
            task: task,
            completed: false,
        };
        this.todos.push(newToDo);
        console.log(`Added: "${task}"`);
        return newToDo;
    }

    // Mark a to-do item as completed
    complete(id: number): ToDo | undefined {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.completed = true;
            console.log(`Completed: "${todo.task}"`);
        } else {
            console.log(`Error: To-do with ID ${id} not found.`);
        }
        return todo;
    }

    // Remove a to-do item by its ID
    remove(id: number): boolean {
        const index = this.todos.findIndex(t => t.id === id);
        if (index > -1) {
            const removed = this.todos.splice(index, 1);
            console.log(`Removed: "${removed[0].task}"`);
            return true;
        }
        console.log(`Error: To-do with ID ${id} not found.`);
        return false;
    }

    // Display all to-do items
    display(): void {
        console.log("\n--- To-Do List ---");
        if (this.todos.length === 0) {
            console.log("The list is empty.");
        } else {
            this.todos.forEach(todo => {
                console.log(
                    `[${todo.completed ? 'x' : ' '}] ID: ${todo.id}, Task: ${todo.task}`
                );
            });
        }
        console.log("------------------\n");
    }
}

// --- Test the application in the console ---
function runApp() {
    console.log("Initializing To-Do List Application...");
    const myList = new ToDoList();

    // Display initial empty list
    myList.display();

    // Add some items
    myList.add("Learn TypeScript");
    const item2 = myList.add("Build a project");
    myList.add("Write a README file");

    // Display the list after adding items
    myList.display();

    // Complete an item
    myList.complete(item2.id);

    // Try to complete an item that doesn't exist
    myList.complete(99);

    // Display the list again
    myList.display();

    // Remove an item
    myList.remove(1);

    // Display the final list
    myList.display();
}

// Run the application
runApp();