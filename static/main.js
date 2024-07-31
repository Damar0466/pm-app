
function toggleForm() {
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");
    if (loginForm.style.display === "none") {
      loginForm.style.display = "block";
      registerForm.style.display = "none";
    } else {
      loginForm.style.display = "none";
      registerForm.style.display = "block";
    }
  }

  function register() {
    const username = document.getElementById("registerUsername").value;
    const password = document.getElementById("registerPassword").value;

    if (username && password) {
      // Set the registration date
      const registrationDate = new Date();
      localStorage.setItem("username", username);
      localStorage.setItem("password", password);
      localStorage.setItem(
        "registrationDate",
        registrationDate.toISOString()
      );
      alert("Registrasi berhasil! Silakan login.");
      toggleForm();
    } else {
      alert("Mohon isi semua field.");
    }
  }

  function login() {
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    const storedUsername = localStorage.getItem("username");
    const storedPassword = localStorage.getItem("password");
    const registrationDate = localStorage.getItem("registrationDate");

    if (!storedUsername || !storedPassword || !registrationDate) {
      alert("Akun tidak ditemukan atau sudah kedaluwarsa.");
      return;
    }

    const currentDate = new Date();
    const registeredDate = new Date(registrationDate);
    const daysElapsed = Math.floor(
      (currentDate - registeredDate) / (1000 * 60 * 60 * 24)
    );

    if (daysElapsed > 30) {
      alert("Masa aktif akun telah berakhir. Akun Anda telah dihapus.");
      localStorage.removeItem("username");
      localStorage.removeItem("password");
      localStorage.removeItem("registrationDate");
      return;
    }

    if (username === storedUsername && password === storedPassword) {
      alert("Login berhasil!");
      localStorage.setItem("isLoggedIn", "true");
      window.location.href = "home.html"; // Arahkan ke halaman home
    } else {
      alert("Username atau password salah.");
    }
  }