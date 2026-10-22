#!/usr/bin/env python3
"""Deterministic candidate wall-drying pole graphics, RimWorld 1.6 only."""
from PIL import Image, ImageDraw
from pathlib import Path
import sys
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[2] / 'Textures/Things/Building/WallDryingPole'
OUT.mkdir(parents=True, exist_ok=True)
WOOD_EDGE=(41,32,25,255); WOOD_DARK=(100,65,40,255)
WOOD=(155,106,56,255); HIGHLIGHT=(203,149,90,255)
ROPE=(175,143,100,255); MEAT_EDGE=(66,40,34,255); MEAT=(160,88,60,255); MEAT_HIGHLIGHT=(205,133,96,255)
FISH=(117,143,135,255); FISH_EDGE=(47,64,63,255)

def one(orientation, product):
    W=512
    a=Image.new('RGBA',(W,W),(0,0,0,0)); d=ImageDraw.Draw(a)
    dx={'north':0,'south':9,'east':-12,'west':-12}[orientation]
    for x in [118+dx,394+dx]:
        d.rounded_rectangle((x-20,130,x+20,184),radius=6,fill=WOOD_DARK,outline=WOOD_EDGE,width=7)
        d.rectangle((x-13,136,x+13,168),fill=WOOD)
        d.line([(x-10,142),(x+6,142)],fill=HIGHLIGHT,width=4)
    d.rounded_rectangle((91+dx,145,422+dx,175),radius=13,fill=WOOD_EDGE)
    d.rounded_rectangle((97+dx,150,416+dx,170),radius=9,fill=WOOD)
    d.line([(109+dx,156),(401+dx,156)],fill=HIGHLIGHT,width=6)
    d.line([(102+dx,168),(410+dx,168)],fill=WOOD_DARK,width=3)
    if product:
        for i,x in enumerate([148,204,260,316,372]):
            x+=dx
            end=300+(i%2)*19
            d.line([(x-7,161),(x-5,194),(x+1,end-22)],fill=WOOD_EDGE,width=10)
            d.line([(x-7,161),(x-5,194),(x+1,end-22)],fill=ROPE,width=5)
            d.ellipse((x-11,156,x+3,172),fill=WOOD_DARK,outline=WOOD_EDGE,width=4)
            y=198+(i%2)*8
            if product=='meat':
                poly=[(x-9,y-6),(x+11,y),(x+14,y+19),(x+8,y+47),(x+13,y+70),(x+2,y+91),(x-14,y+80),(x-8,y+58),(x-13,y+31)]
                d.polygon(poly,fill=MEAT,outline=MEAT_EDGE,width=7)
                d.line([(x+4,y+12),(x+4,y+31),(x-1,y+54)],fill=MEAT_HIGHLIGHT,width=6)
                d.line([(x-8,y+31),(x-6,y+61)],fill=WOOD_DARK,width=4)
            else:
                d.polygon([(x-19,y+24),(x-6,y+8),(x+15,y+12),(x+27,y+24),(x+15,y+40),(x-7,y+43)],fill=FISH,outline=FISH_EDGE,width=7)
                d.polygon([(x-17,y+24),(x-31,y+9),(x-31,y+40)],fill=FISH,outline=FISH_EDGE,width=6)
                d.ellipse((x+13,y+22,x+17,y+26),fill=WOOD_EDGE)
                d.line([(x-6,y+18),(x+9,y+18)],fill=HIGHLIGHT,width=4)
    if orientation=='west': a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return a.resize((256,256),Image.Resampling.LANCZOS)

for side in ['north','south','east','west']:
    for kind,suffix in [(None,''),('meat','FilledMeat'),('fish','FilledFish')]:
        one(side,kind).save(OUT/f'WallDryingPole{suffix}_{side}.png',optimize=False)
one('north',None).save(OUT/'WallDryingPole_MenuIcon.png',optimize=False)
