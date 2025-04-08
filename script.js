document.addEventListener("DOMContentLoaded", () => {
    alert("Welcome to Kain Energy's Website!");
});
document.getElementById("contactForm").addEventListener("submit", (event) => {
    event.preventDefault(); // Prevents page refresh
    
    // Get form values
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    if (name && email && message) {
        alert("Thank you, " + name + "! Your message has been received.");
    } else {
        alert("Please fill out all fields.");
    }
});




