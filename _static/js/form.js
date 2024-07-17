document.addEventListener('DOMContentLoaded', function () {
    var elements = Array.from(document.querySelectorAll('input, textarea, select'));
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].required) {
            elements[i].previousElementSibling.classList.add('label-required');
        }
    }
});

