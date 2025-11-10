document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('task-input');
    const addTaskBtn = document.getElementById('add-task-btn');
    const taskList = document.getElementById('task-list');

    // Function to add a new task
    const addTask = () => {
        const taskText = taskInput.value.trim();
        if (taskText === '') {
            alert('Please enter a task.');
            return;
        }

        const li = document.createElement('li');

        const taskSpan = document.createElement('span');
        taskSpan.className = 'task-text';
        taskSpan.textContent = taskText;

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons';

        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        editBtn.textContent = 'Edit';

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Delete';

        buttonsDiv.appendChild(editBtn);
        buttonsDiv.appendChild(deleteBtn);

        li.appendChild(taskSpan);
        li.appendChild(buttonsDiv);

        taskList.appendChild(li);

        taskInput.value = '';

        // Add event listeners for new buttons
        deleteBtn.addEventListener('click', () => {
            taskList.removeChild(li);
        });

        editBtn.addEventListener('click', () => {
            editTask(li, taskSpan, editBtn);
        });
    };

    // Function to edit a task
    const editTask = (li, taskSpan, editBtn) => {
        const currentText = taskSpan.textContent;
        const editInput = document.createElement('input');
        editInput.type = 'text';
        editInput.className = 'edit-input';
        editInput.value = currentText;

        const saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';
        saveBtn.textContent = 'Save';

        li.replaceChild(editInput, taskSpan);
        editBtn.style.display = 'none';
        
        const buttonsDiv = li.querySelector('.buttons');
        const deleteBtn = buttonsDiv.querySelector('.delete-btn');
        buttonsDiv.insertBefore(saveBtn, deleteBtn);


        saveBtn.addEventListener('click', () => {
            const newText = editInput.value.trim();
            if (newText === '') {
                alert('Task cannot be empty.');
                return;
            }
            taskSpan.textContent = newText;
            li.replaceChild(taskSpan, editInput);
            buttonsDiv.removeChild(saveBtn);
            editBtn.style.display = 'inline-block';
        });
    };

    addTaskBtn.addEventListener('click', addTask);

    taskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addTask();
        }
    });
});