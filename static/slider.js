const slider = document.getElementById("slider");
    noUiSlider.create(slider, {
      start: [2011, 2023],      
      connect: true,
      range: {
        min: 2011,
        max: 2023
      },
      step: 1,
      format: {
        to: value => Math.round(value),
        from: value => Number(value)
      },
      tooltips: true
    });
