document.addEventListener('DOMContentLoaded', function () {
    const textElements = document.querySelectorAll('.Text');

    textElements.forEach(element => {
        const url = element.dataset.url;

        if (url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    element.textContent = data.text;
                })
                .catch(error => {
                    console.error('Ошибка загрузки:', error);
                    element.textContent = 'Ошибка загрузки';
                });
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const textElements = document.querySelectorAll('.Text');
    
    textElements.forEach(element => {
        const path = element.textContent;
        fetch(path)
            .then(response => response.json())
            .then(data => {
                element.textContent = data.text;
            })
            .catch(error => console.error('Error:', error));
    });
});