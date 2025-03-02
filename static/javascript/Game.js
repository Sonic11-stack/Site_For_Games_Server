document.getElementById("star-icon").addEventListener("click", function() {
    fetch("/click_star", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.is_clicked) {
            document.getElementById("star-icon").src = "/static/icons/Full_Star.jpg";
        } else {
            document.getElementById("star-icon").src = "/static/icons/Star.jpg";
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при обновлении');
    });
});