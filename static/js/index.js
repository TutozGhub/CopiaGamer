var swiper = new Swiper(".mySwiper", {
    slidesPerView: 'auto',
    spaceBetween: 25,
    centeredSlides: true,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});