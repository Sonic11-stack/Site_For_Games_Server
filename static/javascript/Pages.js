document.addEventListener('DOMContentLoaded', function() {
    const textElements = document.querySelectorAll('.Text');
    textElements.forEach(element => {
        if (element.textContent.startsWith('/get_text/')) {
            const id = element.textContent.split('/').pop();
            fetch(`/get_text/${id}`)
                .then(response => response.json())
                .then(data => {
                    element.textContent = data.text;
                });
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const textElements = document.querySelectorAll('.Text');
    textElements.forEach(element => {
        if (element.textContent.startsWith('/get_text_engine/')) {
            const id = element.textContent.split('/').pop();
            fetch(`/get_text_engine/${id}`)
                .then(response => response.json())
                .then(data => {
                    element.textContent = data.text;
                });
        }
    });
});