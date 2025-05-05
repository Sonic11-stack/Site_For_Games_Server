const API_KEY = '41fdca3dce1b4153af488de676486592'; 
const GAME_NAME = document.querySelector('[data-game-name]').dataset.gameName;

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

fetchMetacriticScore(GAME_NAME); 


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
    const gameId = window.location.pathname.split('/').pop();

    if (text) {
        fetch(`/stay_comment/${gameId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ comment: text }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                const newComment = document.createElement('div');
                newComment.className = 'comment';
                newComment.setAttribute('data-comment-id', data.comment_id);
                newComment.innerHTML = `
                    <p class="comment-text">${data.comment}</p>
                    <small>Автор: ${data.author}</small>
                    <hr>
                `;
                
                const commentsContainer = document.getElementById('comments-list');
                const firstComment = commentsContainer.querySelector('.comment');
                if (firstComment) {
                    commentsContainer.insertBefore(newComment, firstComment);
                } else {
                    commentsContainer.appendChild(newComment);
                }
                
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
