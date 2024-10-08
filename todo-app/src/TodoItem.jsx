// src/components/TodoItem.jsx
import React from 'react';

function TodoItem({ todo, toggleTodo, deleteTodo }) {
    return (
    <div class="line">
        <div class="item-content">
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
            />
            <span>
                {todo.title}
            </span>
        </div>
        <button class="button" onClick={() => deleteTodo(todo.id)}>Удалить</button>
    </div>
    );
}

export default TodoItem;