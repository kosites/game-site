document.getElementById('exit-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default anchor behavior
    window.open('https://www.example.com', '_blank'); // Open a new tab
    window.close(); // Attempt to close the current tab
});
