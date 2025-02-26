document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById("loginBtn");
    const logoutBtn = document.getElementById("logoutBtn");

    if (loginBtn) {
        loginBtn.addEventListener("click", async function(event) {
            event.preventDefault();
            
            const response = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" }
            });

            if (response.ok) {
                document.cookie = "auth=true; path=/"; 
                location.reload();
            } else {
                alert("Ошибка входа");
            }
        });
    }

    if (logoutBtn) {
        logoutBtn.addEventListener("click", async function(event) {
            event.preventDefault();

            const response = await fetch("/logout", {
                method: "POST",
                headers: { "Content-Type": "application/json" }
            });

            if (response.ok) {
                document.cookie = "auth=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"; 
                location.reload();
            } else {
                alert("Ошибка выхода");
            }
        });
    }
});