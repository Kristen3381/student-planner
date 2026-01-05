async function sendTaskToServer() {
    // Gets values from the User Interphase
    const name = document.getElementById('taskName').value;
    const time = document.getElementById('taskTime').value;
    const type = document.getElementById('taskType').value;

    const taskData = { name, time, type };

    // Sends the values to python(Backend)
    const response = await fetch('/save-task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData)
    });

    const result = await response.json();
    
    if (result.status === "success") {
        alert("Task added to Python's memory!");
        // Clear inputs
        document.getElementById('taskName').value = '';
    }
}
async function loadSchedule() {
    const response = await fetch('/get-schedule');
    const schedule = await response.json();
    
    const display = document.getElementById('displayArea');
    display.innerHTML = ''; // Clear the old list

    schedule.forEach(item => {
        const card = document.createElement('div');
        
        // Tailwind Trick: Change color based on type!
        const color = item.type === 'fixed' ? 'bg-red-100 border-red-500' : 'bg-green-100 border-green-500';
        
        card.className = `p-4 border-l-4 rounded shadow-sm ${color} flex justify-between`;
        card.innerHTML = `
            <div>
                <p class="font-bold">${item.name}</p>
                <p class="text-sm text-gray-600">${item.type.toUpperCase()}</p>
            </div>
            <div class="text-lg font-mono">${item.time}</div>
        `;
        display.appendChild(card);
    });
}