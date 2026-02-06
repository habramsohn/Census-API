const slider = document.getElementById("slider");
    noUiSlider.create(slider, {
      start: [2011, 2024],      
      connect: true,
      range: {
        min: 2011,
        max: 2024
      },
      step: 1,
      format: {
        to: value => Math.round(value),
        from: value => Number(value)
      },
      tooltips: true
    });
