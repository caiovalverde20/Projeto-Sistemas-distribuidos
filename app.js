function sendEvent(data) {
    console.log("Sending data:", data);
    console.log("Size of data (bytes):", new TextEncoder().encode(JSON.stringify(data)).length);

    fetch(`http://localhost:3000/produce`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }).then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error sending event:', error));
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    sendEvent({
        message: `Login attempt for ${username}`,
        password: password
    });
}

function simulateError() {
    try {
        throw new Error('Simulated Error');
    } catch (e) {
        sendEvent({ message: `Error occurred: ${e.message}` });
    }
}

function handleClickEvent(eventDescription) {
    sendEvent({ message: eventDescription });
}
