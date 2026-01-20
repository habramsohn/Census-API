const slider = document.getElementById("slider");
    noUiSlider.create(slider, {
      start: [2011, 2023],      
      connect: true,
      range: {
        min: 2011,
        max: 2023
      },
      step: 1,
      pips: {
        mode: 'steps',
        density: -1,
        filter: function(value, type) {
            return 1;
        },
      },
      format: {
        to: value => Math.round(value),
        from: value => Number(value)
        }
    });
