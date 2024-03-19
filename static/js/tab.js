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