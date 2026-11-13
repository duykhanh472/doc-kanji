// Get the current year
var currentYear = new Date().getFullYear();

// Set the copyright information dynamically (the footer is optional)
var copyrightElement = document.getElementById("copyright");

if (copyrightElement) {
    copyrightElement.innerHTML = "Copyrights &#169; " + currentYear + " Osha Permadi. All Rights Reserved.";
}
