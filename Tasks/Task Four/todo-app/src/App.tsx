import { useState } from 'react';
import { TodoInput } from './components/TodoInput';
import { TodoItem } from './components/TodoItem';
import type { Todo } from '../types';
import './App.css';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);

  const addTodo = (text: string) => {
    const newTodo: Todo = {
      id: crypto.randomUUID(),
      text,
      isCompleted: false,
    };
    setTodos([...todos, newTodo]);
  };

  const toggleComplete = (id: string) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, isCompleted: !todo.isCompleted } : todo
    ));
  };

  const deleteTodo = (id: string) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const editTodo = (id: string, newText: string) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, text: newText } : todo
    ));
  };

  return (
    <div className="app-container">
      <header>
        <h1>Task Master</h1>
        <p>Manage your day effectively</p>
      </header>
      
      <div className="todo-wrapper">
        <TodoInput addTodo={addTodo} />
        
        <ul className="todo-list">
          {todos.length === 0 ? (
            <p className="empty-state">No tasks yet. Add one above!</p>
          ) : (
            todos.map(todo => (
              <TodoItem
                key={todo.id}
                todo={todo}
                toggleComplete={toggleComplete}
                deleteTodo={deleteTodo}
                editTodo={editTodo}
              />
            ))
          )}
        </ul>
      </div>
    </div>
  );
}

export default App;