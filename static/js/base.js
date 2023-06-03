document.getElementById('theme-toggle').addEventListener('click', function(event) {
    event.preventDefault();
    var navbar = document.getElementById('navbar');
    var body = document.getElementById('body');
    if (navbar.classList.contains('navbar-dark')) {
        navbar.classList.remove('navbar-dark');
        navbar.classList.remove('bg-dark');
        navbar.classList.add('navbar-light');
        navbar.classList.add('bg-light');
        body.classList.remove('bg-dark-theme');
        body.classList.add('bg-light-theme');
        localStorage.setItem('theme', 'light');
    } else {
        navbar.classList.remove('navbar-light');
        navbar.classList.remove('bg-light');
        navbar.classList.add('navbar-dark');
        navbar.classList.add('bg-dark');
        body.classList.remove('bg-light-theme');
        body.classList.add('bg-dark-theme');
        localStorage.setItem('theme', 'dark');
    }
});

// When the page loads, check the theme in localStorage and update the page accordingly
window.onload = function() {
    var navbar = document.getElementById('navbar');
    var body = document.getElementById('body');
    var theme = localStorage.getItem('theme');
    if (theme === 'light') {
        navbar.classList.remove('navbar-dark');
        navbar.classList.remove('bg-dark');
        navbar.classList.add('navbar-light');
        navbar.classList.add('bg-light');
        body.classList.remove('bg-dark-theme');
        body.classList.add('bg-light-theme');
    } else if (theme === 'dark') {
        navbar.classList.remove('navbar-light');
        navbar.classList.remove('bg-light');
        navbar.classList.add('navbar-dark');
        navbar.classList.add('bg-dark');
        body.classList.remove('bg-light-theme');
        body.classList.add('bg-dark-theme');
    }

    setTimeout(function() {
        var messages = document.querySelectorAll('.alert');
        messages.forEach(function(message) {
            message.classList.add('hide-message');
        });
    }, 2000);  // 2 seconds
}