import React, { useState } from 'react';

interface TodoInputProps {
  addTodo: (text: string) => void;
}

export const TodoInput: React.FC<TodoInputProps> = ({ addTodo }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      addTodo(input);
      setInput('');
    }
  };

  return (
    <form className="todo-input-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="What needs to be done?"
        className="todo-input"
      />
      <button type="submit" className="add-btn">
        Add Task
      </button>
    </form>
  );
};