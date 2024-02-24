function checkPasswordStrength() {
    const passwordInput = document.getElementById('password');
    const passwordStrength = document.getElementById('password-strength');
    const requirementsList = document.querySelectorAll('.password-requirements li');

    // Reset styles
    passwordStrength.innerHTML = '';
    requirementsList.forEach(item => item.style.color = '');

    const password = passwordInput.value;

    // Check for minimum length
    if (password.length >= 8 && password.length <= 15) {
        requirementsList[0].style.color = 'green';
    } else {
        requirementsList[0].style.color = 'red';
    }

    // Check for at least one lowercase character
    if (/[a-z]/.test(password)) {
        requirementsList[1].style.color = 'green';
    } else {
        requirementsList[1].style.color = 'red';
    }

    // Check for at least one uppercase character
    if (/[A-Z]/.test(password)) {
        requirementsList[2].style.color = 'green';
    } else {
        requirementsList[2].style.color = 'red';
    }

    // Check for at least one number
    if (/\d/.test(password)) {
        requirementsList[3].style.color = 'green';
    } else {
        requirementsList[3].style.color = 'red';
    }

    // Check for at least one special character
    if (/[^a-zA-Z0-9]/.test(password)) {
        requirementsList[4].style.color = 'green';
    } else {
        requirementsList[4].style.color = 'red';
    }
}