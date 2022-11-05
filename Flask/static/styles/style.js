document.getElementById('input_img').addEventListener("change", function () {
    var fullPath = document.getElementById('input_img').value;
    if (fullPath) {
        var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        var image = fullPath.substring(startIndex);
        if (image.indexOf('\\') === 0 || image.indexOf('/') === 0) {
            image = image.substring(1);
        }
        document.getElementById("filename").innerHTML = image;
    }
});

var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    var input_cont = document.getElementById('inp');
    input_cont.classList.remove("flex");
    document.getElementById('inp').classList.add("hidden");
};