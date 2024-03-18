console.log("JSOK");

// Add active class to the current button (highlight it)

const linksMenu = document.querySelectorAll(".nav-link");
console.log(linksMenu);

linksMenu.forEach((element) => {
  element.addEventListener("click", function () {
    linksMenu.forEach((a) => a.classList.remove("active"));
    this.classList.add("active");
  });
});


function openTab(tabName) {
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
  }
  document.getElementById(tabName + "Tab").style.display = "block";
}
// Display the view profile tab by default
openTab('view');