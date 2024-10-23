document.addEventListener("DOMContentLoaded", function() {
    const toggleIcon = document.getElementById('toggle-dark-mode');
    const body = document.body;
  
    // Add smooth transition
    body.style.transition = "background-color 0.5s ease, color 0.5s ease";
  
    toggleIcon.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
      body.classList.toggle('light-mode');
  
      if (body.classList.contains('dark-mode')) {
        toggleIcon.classList.remove('fa-moon');
        toggleIcon.classList.add('fa-sun');
      } else {
        toggleIcon.classList.remove('fa-sun');
        toggleIcon.classList.add('fa-moon');
      }
    });
  });
  
  