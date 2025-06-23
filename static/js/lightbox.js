function initImageZoom() {
    const postDetail = document.querySelector('.post-detail');
    if (!postDetail) return;

    const modal = document.querySelector('.global-modal');
    const modalImg = document.getElementById('modalImage');
    const closeBtn = modal.querySelector('.modal-close');

    const images = postDetail.querySelectorAll('img');
    images.forEach(img => {
        img.style.cursor = 'zoom-in';

        img.addEventListener('click', function() {
            document.body.style.overflow = 'hidden';
            document.documentElement.style.overflow = 'hidden';

            modal.style.display = 'flex';
            modalImg.src = this.src;
            modalImg.alt = this.alt || '';

            const imgRatio = this.naturalWidth / this.naturalHeight;
            const windowRatio = window.innerWidth / window.innerHeight;

            if (imgRatio > windowRatio) {
                modalImg.style.width = '90vw';
                modalImg.style.height = 'auto';
            } else {
                modalImg.style.width = 'auto';
                modalImg.style.height = '90vh';
            }
        });
    });

    function closeModal() {
        modal.style.display = 'none';
        document.body.style.overflow = '';
        document.documentElement.style.overflow = '';
    }

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            closeModal();
        }
    });
}

document.addEventListener('DOMContentLoaded', initImageZoom);