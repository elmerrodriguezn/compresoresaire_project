var getYear;
(getYear = function () {
    const date = new Date();
    document.querySelector('.year').innerHTML = date.getFullYear();
})();

var menuIcon;
(menuIcon = function (x) {
    if (x) {
        x.classList.toggle("change");
    }

})();
