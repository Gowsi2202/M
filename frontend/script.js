document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registrationForm = document.getElementById('registrationForm');

    // Login form submission
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://127.0.0.1:8000/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password })
                });

                const result = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', result.token);  // Store token in local storage
                    alert('Login successful');
                    // Redirect based on user role
                    if (result.role === 'admin') {
                        window.location.href = '/frontend/admin.html';  // Redirect to admin page
                    } else {
                        window.location.href = '/frontend/user.html';   // Redirect to user page
                    }
                } else {
                    alert('Login failed: ' + result.detail);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while logging in. Please try again.');
            }
        });
    }

    // Registration form submission
    if (registrationForm) {
        registrationForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const aadhar = document.getElementById('aadhar').value;

            try {
                const response = await fetch('http://127.0.0.1:8000/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password, aadhar })
                });

                const result = await response.json();
                if (response.ok) {
                    alert('Registration successful');
                    window.location.href = '/frontend/index.html';  // Redirect to login page
                } else {
                    alert('Registration failed: ' + result.detail);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during registration. Please try again.');
            }
        });
    }
});

// Display username after login
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    if (token) {
        try {
            const decoded = jwt_decode(token);
            const username = decoded.sub;
            document.getElementById('username').textContent = username;
        } catch (error) {
            console.error('Invalid token:', error);
        }
    } else {
        console.error('No token found');
    }
});
