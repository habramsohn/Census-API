const form = document.getElementById('form');
const plot = document.getElementById('plot')

form.addEventListener('submit', async function (e) { 
    e.preventDefault();
    const FormData = new FormData(form);

    var zipcode = FormData.get("zipcode");
    var minYear = $("#slider").rangeSlider("min");
    var maxYear = $("#slider").rangeSlider("max");

    var url = `/zip/${zipcode}/years/${minYear}-${maxYear}`;

    var response = await fetch(url)

    plot.innerHTML = response
})