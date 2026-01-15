const form = document.getElementById('submit');

form.addEventListener('click', async function (e) { 
    e.preventDefault();
    var zipcode = document.getElementById("zipcode").value;
    var slider = document.getElementById("slider");
    var range = slider.noUiSlider.get();
    var minYear = range[0]
    var maxYear = range[1]

    var url = `/zip/${zipcode}/years/${minYear}-${maxYear}`;
    window.open(url, '_blank');
})