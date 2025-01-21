/*const API_KEY = '41fdca3dce1b4153af488de676486592'; 
const GAME_NAME = 'The Last of Us'; 

async function fetchMetacriticScore(gameName) {
  try {
    const response = await fetch(`https://api.rawg.io/api/games?search=${encodeURIComponent(gameName)}&key=${API_KEY}`);
    const data = await response.json();

    if (data.results && data.results.length > 0) {
      const game = data.results[0];
      document.getElementById('score-placeholder').textContent = game.metacritic || 'Нет данных';
    } else {
      document.getElementById('score-placeholder').textContent = 'Игра не найдена';
    }
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
    document.getElementById('score-placeholder').textContent = 'Ошибка загрузки';
  }
}

fetchMetacriticScore(GAME_NAME); */


const addCommentBtn = document.getElementById('add-comment-btn');
const commentField = document.getElementById('comment-field');
const submitCommentBtn = document.getElementById('submit-comment-btn');
const commentsList = document.getElementById('comments-list');
const commentText = document.getElementById('comment-text');

addCommentBtn.addEventListener('click', () => {
    commentField.style.display = 'block';
});

submitCommentBtn.addEventListener('click', () => {
    const text = commentText.value.trim();

    if (text) {
        // Отправляем комментарий на сервер
        fetch('/add_comment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ comment: text }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Добавляем комментарий в список на странице
                const newComment = document.createElement('p');
                newComment.textContent = text;
                newComment.style.borderBottom = '1px solid #ccc';
                newComment.style.padding = '10px 0';
                commentsList.appendChild(newComment);

                commentText.value = '';
                commentField.style.display = 'none';
            } else {
                alert('Не удалось добавить комментарий. Попробуйте еще раз.');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при добавлении комментария.');
        });
    } else {
        alert('Пожалуйста, введите текст комментария!');
    }
});

