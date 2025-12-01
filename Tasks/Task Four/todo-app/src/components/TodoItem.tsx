import React, { useState } from 'react';
import type { Todo } from '../types';

interface TodoItemProps {
  todo: Todo;
  toggleComplete: (id: string) => void;
  deleteTodo: (id: string) => void;
  editTodo: (id: string, newText: string) => void;
}

export const TodoItem: React.FC<TodoItemProps> = ({ todo, toggleComplete, deleteTodo, editTodo }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(todo.text);

  const handleEdit = () => {
    if (isEditing && editText.trim()) {
      editTodo(todo.id, editText);
    }
    setIsEditing(!isEditing);
  };

  return (
    <li className={`todo-item ${todo.isCompleted ? 'completed' : ''}`}>
      <div className="todo-content">
        <input
          type="checkbox"
          checked={todo.isCompleted}
          onChange={() => toggleComplete(todo.id)}
          className="checkbox"
        />
        
        {isEditing ? (
          <input
            type="text"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
            className="edit-input"
            autoFocus
          />
        ) : (
          <span className="todo-text" onClick={() => toggleComplete(todo.id)}>
            {todo.text}
          </span>
        )}
      </div>

      <div className="actions">
        <button onClick={handleEdit} className="edit-btn">
          {isEditing ? 'Save' : 'Edit'}
        </button>
        <button onClick={() => deleteTodo(todo.id)} className="delete-btn">
          Delete
        </button>
      </div>
    </li>
  );
};