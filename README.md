# stable-diffusion-webui-conditioning-highres-fix

This is Extension for AUTOMATIC1111/stable-diffusion-webui for rewriting "Inpainting conditioning mask strength" value relative to "Denoising strength" at runtime. This is useful for "Inpainting" models such as ` sd-v1-5-inpainting.ckpt`

## Installation:
Copy the link to this repository into "Extension index URL" in WebUI Extensions tab:
```
https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix
```
Also you may clone/download this repository and put it to `stable-diffusion-webui/extensions` directory.

## Usage:
You will see radiogroup titled "Conditioning Highres.fix strength (for sd-v1-5-inpainting)" on txt2img and img2img tabs.

When `Cond.fix: Disabled (none)` is selected – nothing will be done. But otherwise, your `Inpainting conditioning mask strength` will be:
- `Cond.fix: Empty` = always set to `1.0`, effectively turning off mask strength feature;
- `Cond.fix: Lowest` = set to `1-Denoising/4`
- `Cond.fix: Low` = set to `1-Denoising/2`
- `Cond.fix: Medium` = always set to `0.5`
- `Cond.fix: High (recommended)` = set to `Denoising/2`
- `Cond.fix: Highest` = set to `Denoising/4`
- `Cond.fix: Full` = always set to `0.0`, turning on maximal effect.

To use this in txt2img – don't forget to enable "Highres. fix" checkbox and make your dimensions larger than default 512*512. Also its better to turn off "Upscale latent space image when doing hires. fix" option in settings, because it often q

## Explanation:

Here is the grid that shows the relation between Denoising strength and Inpainting conditioning mask strength:
- [Original from txt2img](https://klimaleksus2.ucoz.ru/waifu/conditioning-highres-fix.png)
- [Grid in img2img](https://klimaleksus2.ucoz.ru/waifu/conditioning-highres-fix.jpg)

You can load this grid into [xy-plot-online-grid-viewer-v1.htm](https://klimaleksus.github.io/xy-plot-online-grid-viewer/xy-plot-online-grid-viewer-v1.htm) to explore it cell-wise.

As you can see, the lower Conditioning strength is, the better and sharper the image will become. On high Denoising strengths the image also becomes over-saturated and somewhat simplified.

In contrary, on high Conditioning strengths the duplication artifacts are clearly visible on high Denoising strengths.

On low Denoising strength the image will be still blurry unless the Conditioning strength is low. That's why I put "(recommended)" mark on High fix button – to make Conditioning strength as low as possible without over-saturating the image.

## Examples:

Here are strips of variable Denoising strength made on different Conditioning fix level:
- [Original (PNG)](https://klimaleksus2.ucoz.ru/waifu/0-Original.png)
- [Empty](https://klimaleksus2.ucoz.ru/waifu/1-Empty.jpg)
- [Lowest](https://klimaleksus2.ucoz.ru/waifu/2-Lowest.jpg)
- [Low](https://klimaleksus2.ucoz.ru/waifu/3-Low.jpg)
- [Medium](https://klimaleksus2.ucoz.ru/waifu/4-Medium.jpg)
- [High](https://klimaleksus2.ucoz.ru/waifu/5-High.jpg)
- [Highest](https://klimaleksus2.ucoz.ru/waifu/6-Highest.jpg)
- [Full](https://klimaleksus2.ucoz.ru/waifu/7-Full.jpg)

You can load all of them at once into online-grid-viewer, just copy and paste those links:
<details><summary>Links of abowe</summary>

```
https://klimaleksus2.ucoz.ru/waifu/1-Empty.jpg
https://klimaleksus2.ucoz.ru/waifu/2-Lowest.jpg
https://klimaleksus2.ucoz.ru/waifu/3-Low.jpg
https://klimaleksus2.ucoz.ru/waifu/4-Medium.jpg
https://klimaleksus2.ucoz.ru/waifu/5-High.jpg
https://klimaleksus2.ucoz.ru/waifu/6-Highest.jpg
https://klimaleksus2.ucoz.ru/waifu/7-Full.jpg
```

</details>
