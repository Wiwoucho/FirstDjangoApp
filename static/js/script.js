function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "none" || dropdown.style.display === "") {
        dropdown.style.display = "block";
        setTimeout(function() {
            dropdown.style.opacity = "1";
            dropdown.style.transform = "translateY(0)";
        }, 10); // Delay for smoother animation
    } else {
        dropdown.style.opacity = "0";
        dropdown.style.transform = "translateY(-10px)";
        setTimeout(function() {
            dropdown.style.display = "none";
        }, 300); // Delay to match transition duration
    }
}
