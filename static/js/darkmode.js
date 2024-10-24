document.addEventListener("DOMContentLoaded", function () {
  const toggleIcon = document.getElementById("toggle-dark-mode");
  const body = document.body;

  toggleIcon.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    body.classList.toggle("light-mode");

    if (body.classList.contains("dark-mode")) {
      toggleIcon.classList.remove("fa-moon");
      toggleIcon.classList.add("fa-sun");
    } else {
      toggleIcon.classList.remove("fa-sun");
      toggleIcon.classList.add("fa-moon");
    }
  });
});
