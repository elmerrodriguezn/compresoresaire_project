///const date = new Date();
//document.querySelector('.year').innerHTML = date.getFullYear();

///setTimeout(function () {
///$('#message').fadeOut('slow');
///}, 10000);

function showImage() {
    var id = document.getElementById('img')
    img.onclick = function () {
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }
}