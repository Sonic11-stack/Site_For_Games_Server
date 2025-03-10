document.addEventListener("DOMContentLoaded", function() {
    const starIcon = document.getElementById("star-icon");
    if (starIcon) {
        starIcon.addEventListener("click", function() {
            const gameId = this.getAttribute('data-game-id');
            
            fetch("/click_star", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    save_game: gameId
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_clicked) {
                    this.src = "/static/icons/Full_Star.jpg";
                    this.nextElementSibling.textContent = "Сохранено";
                } else {
                    this.src = "/static/icons/Star.jpg";
                    this.nextElementSibling.textContent = "Сохранить в профиль";
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert('Произошла ошибка при обновлении');
            });
        });
    }
});