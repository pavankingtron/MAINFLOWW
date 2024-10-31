function validateForm() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  // Simple form validation
  if (name.trim() === "") {
    alert("Please enter your name.");
    return false;
  }
  if (email.trim() === "" || !validateEmail(email)) {
    alert("Please enter a valid email address.");
    return false;
  }
  alert("Form submitted successfully!");
  return true;
}

// Email validation function
function validateEmail(email) {
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  return emailPattern.test(email);
}
function navigate(section) {
  const content = document.getElementById("content");

  switch (section) {
    case 'home':
      content.innerHTML = "<h1>Home</h1><p>Welcome to the homepage!</p>";
      break;
    case 'about':
      content.innerHTML = "<h1>About Us</h1><p>Learn more about us here.</p>";
      break;
    case 'contact':
      content.innerHTML = "<h1>Contact Us</h1><p>Reach out through the form below.</p>";
      break;
    default:
      content.innerHTML = "<h1>Welcome to Our Site</h1><p>Click on the menu items to explore more!</p>";
  }
}
function sanitizeInput(input) {
  const tempElement = document.createElement("div");
  tempElement.textContent = input;
  return tempElement.innerHTML;
}

// Use sanitizeInput() on any user input before displaying it
