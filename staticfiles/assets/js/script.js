// ===================== MOBILE MENU TOGGLE =====================

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});

// Close menu when a link is clicked (mobile UX polish)
document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("active");
    });
});


// ===================== NAVBAR SCROLL EFFECT =====================

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
        navbar.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
    } else {
        navbar.style.boxShadow = "none";
    }
});


// ===================== SCROLL REVEAL ANIMATION =====================

const sections = document.querySelectorAll(".section");

const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;

    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;

        if (sectionTop < triggerBottom) {
            section.style.opacity = "1";
            section.style.transform = "translateY(0)";
        }
    });
};

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);


// ===================== CONTACT FORM VALIDATION =====================

const contactForm = document.querySelector(".contact-form");

if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
        const name = contactForm.querySelector("input[type='text']");
        const email = contactForm.querySelector("input[type='email']");
        const message = contactForm.querySelector("textarea");

        if (!name.value.trim() || !email.value.trim() || !message.value.trim()) {
            e.preventDefault();
            alert("Please fill in all fields properly.");
            return;
        }

        // The form will now submit natively to the Django Backend!
    });
}

function studentLogin() {
    const user = document.getElementById("studentUser").value;
    const pass = document.getElementById("studentPass").value;

    if (user === "student" && pass === "1234") {
        document.getElementById("studentDashboard").style.display = "block";
        document.querySelector(".login-container").style.display = "none";
    } else {
        document.getElementById("studentMsg").innerText = "Invalid Login";
    }
}

function adminLogin() {
    const user = document.getElementById("adminUser").value;
    const pass = document.getElementById("adminPass").value;

    if (user === "admin" && pass === "admin123") {
        document.getElementById("adminDashboard").style.display = "block";
        document.querySelector(".login-container").style.display = "none";
    } else {
        document.getElementById("adminMsg").innerText = "Invalid Login";
    }
}