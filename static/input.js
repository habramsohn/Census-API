const zipBtn = document.getElementById('zipyear');
const zipInputElement = document.getElementById('zipcode');
const export_csv = document.getElementById('export_csv');
const vars = document.getElementById('vars');
const viz = document.getElementById('viz');
const loading = document.getElementById('loading');

zipBtn.addEventListener('click', function (e) { 
    e.preventDefault();
    execute();
});

zipInputElement.addEventListener('keyup', function (e) {
    if (e.key === "Enter") {
        e.preventDefault();
        execute();
    }
});

async function execute() {
    try {
        var zipValue = zipInputElement.value; 

        const zipRegex = /^\d{5}$/; 
        if (!zipRegex.test(zipValue)) {
            alert("Please enter a valid 5-digit zipcode.");
            return;
        }

        var slider = document.getElementById("slider");
        var range = slider.noUiSlider.get();
        var minYear = Math.round(range[0]);
        var maxYear = Math.round(range[1]);
        
        var url = `/load/zip/${zipValue}/years/${minYear}-${maxYear}`;

        loading.hidden = false;
        await fetch(url, { method: 'POST' });
        loading.hidden = true;

        vars.hidden = false;
        export_csv.hidden = false;
        viz.hidden = false;

        slider.noUiSlider.on('slide', () => {
            vars.hidden = true;
            export_csv.hidden = true;
            viz.hidden = true;
        })

        export_csv.addEventListener('click', async function (e) {
            e.preventDefault();

            var url = `/export/zip/${zipValue}/years/${minYear}-${maxYear}`;

            window.location.href = url;
        })

        viz.addEventListener('click', function (e) {
            e.preventDefault();
            var slider = document.getElementById("slider");
            var range = slider.noUiSlider.get();
            var minYear = range[0]
            var maxYear = range[1]
            var variable = document.getElementById("vars").value;

            var url = `/viz/zip/${zipValue}/years/${minYear}-${maxYear}/var/${variable}`;
            window.open(url, '_blank');
        })

    } catch (error) {
        alert(error.message);
    }
}