document.getElementById('exit-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default anchor behavior
    window.open('', '_blank'); // Open a new blank tab
    window.close(); // Attempt to close the current tab
});