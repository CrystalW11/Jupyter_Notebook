// script.js

// Function to send a request to the server (Python backend)
function fetchDataFromPython() {
    // Assuming you have a Python server running at this URL
    fetch('http://localhost:5000/data')  // Adjust the URL as needed
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Log the data returned by the server
            document.getElementById("pythonResponse").innerText = data.message;  // Display the data on the page
        })
        .catch(error => console.error("Error fetching data:", error));
}

// This function can be triggered by a button or another event
document.getElementById("fetchDataButton").addEventListener("click", fetchDataFromPython);

document.getElementById("themeToggleButton").addEventListener("click", function () {
    document.body.classList.toggle("dark-theme");
});
