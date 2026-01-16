const zipyear = document.getElementById('zipyear');
const viz = document.getElementById('viz');

zipyear.addEventListener('click', async function (e) { 
    e.preventDefault();
    var zipcode = document.getElementById("zipcode").value;
    var slider = document.getElementById("slider");
    var range = slider.noUiSlider.get();
    var minYear = range[0]
    var maxYear = range[1]

    var url = `/load/zip/${zipcode}/years/${minYear}-${maxYear}`;

    await fetch(url, { method: 'POST' });
})

viz.addEventListener('click', function (e) {
    e.preventDefault();
    var zipcode = document.getElementById("zipcode").value;
    var slider = document.getElementById("slider");
    var range = slider.noUiSlider.get();
    var minYear = range[0]
    var maxYear = range[1]
    var variable = document.getElementById("vars").value;

    var url = `/viz/zip/${zipcode}/years/${minYear}-${maxYear}/var/${variable}`;
    window.open(url, '_blank');
})
    