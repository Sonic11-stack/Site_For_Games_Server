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
        profileContent.style.display = 'none';
        profileCon.style.display = 'flex';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const createNewsButton = document.querySelector('.click-btn-1');
    const profileContent1 = document.querySelector('.profile-content-1');
    const profileCon1 = document.querySelector('.progile-con-1');
    const saveButton1 = document.querySelector('.save-btn');

    createNewsButton.addEventListener('click', function() {
        profileContent1.style.display = 'block'; 
        profileCon1.style.display = 'none';
    });

    saveButton1.addEventListener('click', function() {
        profileContent1.style.display = 'none'; 
        profileCon1.style.display = 'flex';
    });
});