import os
import random
import sys

from modules import scripts, script_callbacks, shared
import gradio as gr

class ConditioningHighresFixScript(scripts.Script):
    def title(self):
        return "Conditioning Highres.fix (for sd-v1-5-inpainting)"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        conditioning_highres_fix = gr.Radio(label='Conditioning Highres.fix strength (for sd-v1-5-inpainting)', choices=['Cond.fix: Disabled (none)', 'Cond.fix: Empty', 'Cond.fix: Lowest', 'Cond.fix: Low', 'Cond.fix: Medium', 'Cond.fix: High (recommended)', 'Cond.fix: Highest', 'Cond.fix: Full'], value='Cond.fix: Disabled (none)', type="index")
        return [conditioning_highres_fix]

    def process(self, p, conditioning_highres_fix):
        if conditioning_highres_fix>0 and p.denoising_strength is not None:
            d = p.denoising_strength
            w = -1.0
            m = ''
            if conditioning_highres_fix==1:
                w = 1.0
                m = 'Empty (=1)'
            elif conditioning_highres_fix==2:
                w = 1.0-d/4.0
                m = 'Lowest (=1-d/4)'
            elif conditioning_highres_fix==3:
                w = 1.0-d/2.0
                m = 'Low (=1-d/2)'
            elif conditioning_highres_fix==4:
                w = 0.5
                m = 'Medium (=1/2)'
            elif conditioning_highres_fix==5:
                w = 0.0+d/2.0
                m = 'High (=d/2)'
            elif conditioning_highres_fix==6:
                w = 0.0+d/4.0
                m = 'Highest (=d/4)'
            elif conditioning_highres_fix==7:
                w = 0.0
                m = 'Full (=0)'
            else:
                return
            print('Conditioning Highres.fix: '+m+' - set mask strength to '+str(w))
            setattr(p,'inpainting_mask_weight',w)

#EOF
