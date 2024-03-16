console.log("JSOK");

// Add active class to the current button (highlight it)

const linksMenu = document.querySelectorAll(".link");
console.log(linksMenu);

linksMenu.forEach((element) => {
  element.addEventListener("click", function () {
    linksMenu.forEach((a) => a.classList.remove("active"));
    this.classList.add("active");
  });
});