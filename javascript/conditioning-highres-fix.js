
(function(){

var titles = {
  "Conditioning Highres.fix strength (for sd-v1-5-inpainting)": "Automatically changes 'Inpainting conditioning mask strength' setting according to your 'Denoising strength' for better img2img/highres.fix results; disabling 'Upscale latent space image when doing hires. fix' is recommended",
  "Cond.fix: Disabled (none)": "Do not rewrite conditioning mask value",
  "Cond.fix: Empty": "Set conditioning mask value to (1.0)",
  "Cond.fix: Lowest": "Set conditioning mask value to (1.0-Denoising/4)",
  "Cond.fix: Low": "Set conditioning mask value to (1.0-Denoising/2)",
  "Cond.fix: Medium": "Set conditioning mask value to (0.5)",
  "Cond.fix: High (recommended)": "Set conditioning mask value to (0.0+Denoising/2)",
  "Cond.fix: Highest": "Set conditioning mask value to (0.0+Denoising/4)",
  "Cond.fix: Full": "Set conditioning mask value to (0.0)",
};

var defer = null;
onUiUpdate(function(){
  if(defer!==null){
    clearTimeout(defer);
  }
  defer = setTimeout(tooltips,100);
});

var tooltips = function(){
// from stable-diffusion-webui/javascript/hints.js

	gradioApp().querySelectorAll('span, button, select, p').forEach(function(span){
		tooltip = titles[span.textContent];

		if(!tooltip){
		    tooltip = titles[span.value];
		}

		if(!tooltip){
			for (const c of span.classList) {
				if (c in titles) {
					tooltip = titles[c];
					break;
				}
			}
		}

		if(tooltip){
			span.title = tooltip;
		}
	})

	gradioApp().querySelectorAll('select').forEach(function(select){
	    if (select.onchange != null) return;

	    select.onchange = function(){
            select.title = titles[select.value] || "";
	    }
	})


};

})();
