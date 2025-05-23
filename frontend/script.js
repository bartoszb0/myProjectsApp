const contentDiv = document.querySelector('.contentDiv')

window.addEventListener('keyup', function(e) {
    if (e.key === ' ') {
        contentDiv.classList.toggle('expandedContent');
    }
})