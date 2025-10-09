document.addEventListener('DOMContentLoaded', function() {
    const scrollElements = document.querySelectorAll('.save-scroll');
    scrollElements.forEach(function(element) {
        element.addEventListener('click', function() {
            const position = window.scrollY;
            const currentUrl = window.location.pathname + window.location.search;
            sessionStorage.setItem('projectsScrollPosition', JSON.stringify({
                position: position,
                url: currentUrl
            }));
        });
    });

    const scrollData = sessionStorage.getItem('projectsScrollPosition');
    if (scrollData) {
        try {
            const { position, url } = JSON.parse(scrollData);
            const currentUrl = window.location.pathname + window.location.search;
            if (url === currentUrl) {
                window.scrollTo(0, parseInt(position));
                sessionStorage.removeItem('projectsScrollPosition');
            }
        } catch (e) {
            sessionStorage.removeItem('projectsScrollPosition');
        }
    }
});