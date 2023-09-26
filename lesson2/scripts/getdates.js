// Get the current year
const currentYear = new Date().getFullYear();

// Update the copyright year in the footer's first paragraph
document.querySelector('footer p:first-child span#year').textContent = currentYear;

// Get the last modified date (in the native format)
const lastModified = document.lastModified;

// Update the second paragraph with the last modified date
document.querySelector('footer p.LastModified span#updated').textContent = `Last Updated: ${lastModified}`;
