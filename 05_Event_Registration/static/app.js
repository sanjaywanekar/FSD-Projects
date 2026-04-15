async function submitRegistration(eventData) {
    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(eventData)
        });
        
        const result = await response.json();
        
        if(result.status === "success") {
            alert("Registration Confirmed at MIT CSN!");
        } else {
            alert("Error: " + result.message);
        }
    } catch (error) {
        console.error("Backend unreachable:", error);
    }
}