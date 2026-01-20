const zipyear = document.getElementById('zipyear');
const export_csv = document.getElementById('export_csv');
const viz = document.getElementById('viz');
const loading = document.getElementById('loading')

zipyear.addEventListener('click', async function (e) { 
    e.preventDefault();

    try{
        var zipcode = document.getElementById("zipcode").value;

        const zipRegex = /^\d{5}$/; 
        if (!zipRegex.test(zipcode)) {
            alert("Please enter a valid 5-digit zipcode.");
            return;
        }

        var slider = document.getElementById("slider");
        var range = slider.noUiSlider.get();
        var minYear = range[0];
        var maxYear = range[1];
        var url = `/load/zip/${zipcode}/years/${minYear}-${maxYear}`;

        loading.hidden = false
        await fetch(url, { method: 'POST' });
        loading.hidden = true

        export_csv.hidden = false;
        viz.hidden = false;

        export_csv.addEventListener('click', async function (e) {
            e.preventDefault();

            var url = `/load/zip/${zipcode}/years/${minYear}-${maxYear}/export`;

            window.location.href = url;
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

    } catch (error) {
        alert(error.message)
    }
})


    