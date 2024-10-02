document.addEventListener("DOMContentLoaded", function () {
    const toggleMoreButton = document.getElementById("toggle-more");
    const moreInfo = document.getElementById("more-info");

    toggleMoreButton.addEventListener("click", function () {
      if (moreInfo.style.display === "none") {
        moreInfo.style.display = "block";
        toggleMoreButton.textContent = "Скрыть";
      } else {
        moreInfo.style.display = "none";
        toggleMoreButton.textContent = "Показать больше";
      }
    });


    const themeSwitcher = document.getElementById("btn-theme-switcher");

        themeSwitcher.addEventListener("click", function () {
        document.body.classList.toggle("dark-theme");
        localStorage.setItem(
            "theme",
            document.body.classList.contains("dark-theme") ? "dark" : "light"
        );
    });


    if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-theme");
    }

    const images = ["proj1.png", "proj2.png", "proj2.png"];
    let currentImageIndex = 0;


    const sliderImage = document.getElementById("slider-image");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");


    function updateSlider() {
        sliderImage.src = images[currentImageIndex];
    }


    prevButton.addEventListener("click", function () {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        updateSlider();
    });


    nextButton.addEventListener("click", function () {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        updateSlider();
    });
});