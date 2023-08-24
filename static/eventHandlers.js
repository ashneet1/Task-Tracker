
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

    deleteTaskIcons.forEach(icon => {
        icon.addEventListener('click', function(event) {
            event.preventDefault();
            const habitIndex = icon.getAttribute('href').split('/').pop();
            fetch(`/delete/${habitIndex}`, { method: 'GET' })
                .then(response => {
                    if (response.ok) {
                        window.location.reload();
                    }
                });
        });
    });
});
