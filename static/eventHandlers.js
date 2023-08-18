
document.addEventListener('DOMContentLoaded', function () {
    const createTaskButton = document.getElementById('createTaskButton');
    const taskFormContainer = document.getElementById('taskFormContainer');
    const cancelTaskButton = document.getElementById('cancelTaskButton');

    createTaskButton.addEventListener('click', () => {
        taskFormContainer.style.display = 'block';
    });

    cancelTaskButton.addEventListener('click', () => {
        taskFormContainer.style.display = 'none';
    });
});
