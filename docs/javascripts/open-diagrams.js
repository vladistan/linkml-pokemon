// Make main Class Diagram and ERD Diagram clickable to open in new tab
document.addEventListener("DOMContentLoaded", function () {
  var targets = ["class_diagram.svg", "erd_diagram.svg"];
  document.querySelectorAll(".md-content img").forEach(function (img) {
    if (targets.some(function (t) { return img.src.endsWith(t); })) {
      var link = document.createElement("a");
      link.href = img.src;
      link.target = "_blank";
      link.title = "Open diagram in new tab";
      img.style.cursor = "pointer";
      img.parentNode.insertBefore(link, img);
      link.appendChild(img);
    }
  });
});
