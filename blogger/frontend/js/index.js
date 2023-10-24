const loginForm = document.getElementById("loginForm");

if (document.body.contains(loginForm)) {
    document.getElementById('loginButton').addEventListener('click', event => {
        event.preventDefault();

        const formMessage = document.getElementById('loginError');

        if (loginForm.checkValidity() === false) {
            loginForm.classList.add('was-validated');
            formMessage.textContent = "Please fill out all fields";
            formMessage.style.display = "block";
            return;
        }

        loginForm.classList.remove('was-validated');
        formMessage.textContent = "";
        formMessage.style.display = "none";

        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        const data = {
            username,
            password
        };

        fetch('http://localhost:8000/user/authenticate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        }).then(response => {
            if (response.ok) {
                response.json().then(data => {
                    let userId = data["id"];
                    console.log(userId);
                    localStorage.setItem("username", username);
                    localStorage.setItem("userId", userId);
                    console.log("User authenticated successfully");
                    window.location.replace("http://localhost:8080/blogs.html");
                });
            } else {
                // Login failed
                console.error('User authentication failed.');
                response.json().then(data => {
                    formMessage.textContent = data["detail"];
                    formMessage.style.display = "block";
                });
            }
        }).catch(error => {
            console.error('An error occurred: ', error);
        });
    });

    document.getElementById('registerButton').addEventListener('click', function (event) {
        event.preventDefault();

        const username = document.getElementById('regUsername');
        const email = document.getElementById('regEmail');
        const password = document.getElementById('regPassword');
        const confirmPassword = document.getElementById('regConfirmPassword');
        const formMessage = document.getElementById('registrationError');

        // Reset the form's validation
        username.classList.remove('is-invalid');
        email.classList.remove('is-invalid');
        password.classList.remove('is-invalid');
        confirmPassword.classList.remove('is-invalid');
        formMessage.textContent = '';
        formMessage.style.display = 'none';

        // Validate the form fields
        if (username.value.trim() === '' || email.value.trim() === '' || password.value.trim() === '' || confirmPassword.value.trim() === '') {
            username.classList.add('is-invalid');
            email.classList.add('is-invalid');
            password.classList.add('is-invalid');
            confirmPassword.classList.add('is-invalid');
            formMessage.textContent = 'Please fill out all fields';
            formMessage.style.display = 'block';
            return;
        }

        // Validate the email address
        if (!email.checkValidity()) {
            email.classList.add('is-invalid');
            formMessage.textContent = 'Please enter a valid email address';
            formMessage.style.display = 'block';
            return;
        }

        // Validate the password
        if (password.value !== confirmPassword.value) {
            password.classList.add('is-invalid');
            confirmPassword.classList.add('is-invalid');
            formMessage.textContent = 'Passwords do not match';
            formMessage.style.display = 'block';
            return;
        }

        const data = {
            username: username.value,
            password: password.value,
            email: email.value
        };

        // Send a POST request
        fetch('http://localhost:8000/user/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        }).then(response => {
            if (response.ok) {
                // Registration was successful
                console.log('User registered successfully.');
                window.location.replace('http://localhost:8080/');
            } else {
                console.error('User registration failed.');
                username.classList.add('is-invalid');
                formMessage.textContent = 'Username already exists';
                formMessage.style.display = 'block';
            }
        }).catch(error => {
            console.error('An error occurred: ', error);
        });
    });
}
