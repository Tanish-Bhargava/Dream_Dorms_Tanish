'use strict';

/**
 * Element toggle function
 */
const toggleElement = function (elem) {
  elem.classList.toggle("active");
};

/**
 * Navbar toggle
 */
const navbar = document.querySelector("[data-navbar]");
const overlay = document.querySelector("[data-overlay]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");

const navElements = [overlay, navCloseBtn, navOpenBtn];

/**
 * Close navbar when clicking on any navbar link
 */
navbarLinks.forEach(link => navElements.push(link));

/**
 * Add event listeners for toggling navbar
 */
navElements.forEach(element => {
  element.addEventListener("click", function () {
    toggleElement(navbar);
    toggleElement(overlay);
  });
});

/**
 * Scroll to specific section when clicking on navbar link
 */
const contactLink = document.querySelector('[href="#contact"]');
if (contactLink) {
  contactLink.addEventListener("click", function (event) {
    event.preventDefault();
    const targetSection = document.getElementById("contact");
    if (targetSection) {
      targetSection.scrollIntoView({ behavior: "smooth" });
      toggleElement(navbar);
      toggleElement(overlay);
    }
  });
}

/**
 * Header active state
 */
const header = document.querySelector("[data-header]");
window.addEventListener("scroll", function () {
  window.scrollY >= 400 ? header.classList.add("active") : header.classList.remove("active");
});
