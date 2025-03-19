document.addEventListener("DOMContentLoaded", function() {
    const starIcon = document.getElementById("star-icon");
    if (starIcon) {
        starIcon.addEventListener("click", function() {
            const gameId = this.getAttribute('data-new-id');
            
            fetch("/click_star_new", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    save_new: gameId
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
        fetch(`/stay_comment_new/${gameId}`, {
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