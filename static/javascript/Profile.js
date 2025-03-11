document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.querySelector('.click-btn');
    const saveButton = document.querySelector('.save-btn');
    const profileContent = document.querySelector('.profile-content');
    const profileCon = document.querySelector('.progile-con');

    editButton.addEventListener('click', function() {
        profileContent.style.display = 'block';
        profileCon.style.display = 'none';
    });

    saveButton.addEventListener('click', function(e) {
        // Не препятствуем отправке формы
        profileContent.style.display = 'none';
        profileCon.style.display = 'flex';
    });
});