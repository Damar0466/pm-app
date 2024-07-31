function scrollToBottom() {
  const content = document.querySelector(".content");
  content.scrollTop = content.scrollHeight;
}

window.addEventListener("load", scrollToBottom);

window.addEventListener("load", () => {
  setTimeout(scrollToBottom, 1000);
});

window.onload = function () {
  const isLoggedIn = localStorage.getItem("isLoggedIn");
  if (isLoggedIn !== "true") {
    alert("Anda harus login terlebih dahulu!");
    window.location.href = "/";
  }
};
