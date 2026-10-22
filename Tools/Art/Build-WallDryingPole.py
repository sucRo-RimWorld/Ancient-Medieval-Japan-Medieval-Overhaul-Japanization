#!/usr/bin/env python3
"""Direction-aware sprites, two sizes; candidate artwork pending author acceptance."""
from pathlib import Path
from PIL import Image, ImageDraw
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parents[2] / 'Textures/Things/Building/WallDryingPole'
EDGE=(42,32,25,255); WOOD_D=(62,41,29,255); WOOD=(159,113,65,255); WOOD_L=(207,154,95,255)
BAMBOO=(165,131,75,255); BAMBOO_L=(215,174,104,255); CORD=(178,141,93,255)
MEAT_D=(82,44,35,255); MEAT=(165,89,66,255); MEAT_L=(204,138,99,255)
FISH_D=(53,72,73,255); FISH=(117,147,141,255); FISH_L=(185,201,181,255)

def polygon(d,p,fill,edge=EDGE,width=7):
    d.polygon(p,fill=fill)
    d.line(p+[p[0]],fill=edge,width=width,joint='curve')

def meat(d,x,y,scale=1,slant=0):
    p=[(x-9*scale,y),(x+7*scale,y),(x+10*scale,y+20*scale),
       (x+5*scale+slant,y+35*scale),(x+12*scale+slant,y+51*scale),
       (x+6*scale+slant,y+78*scale),(x-11*scale+slant,y+74*scale),
       (x-4*scale+slant,y+48*scale),(x-11*scale,y+20*scale)]
    polygon(d,p,MEAT,MEAT_D,6)
    d.line([(x+scale,y+14*scale),(x+2*scale,y+40*scale),
            (x+4*scale+slant,y+59*scale)],fill=MEAT_L,width=5)

def fish(d,x,y,scale=1,slant=0):
    p=[(x-8*scale,y),(x+6*scale,y),(x+11*scale,y+16*scale),
       (x+8*scale+slant,y+45*scale),(x+6*scale+slant,y+57*scale),
       (x+16*scale+slant,y+73*scale),(x+scale+slant,y+65*scale),
       (x-11*scale+slant,y+75*scale),(x-5*scale+slant,y+53*scale),
       (x-12*scale,y+22*scale)]
    polygon(d,p,FISH,FISH_D,6)
    d.line([(x-5*scale,y+14*scale),(x+4*scale,y+26*scale),
            (x+scale,y+44*scale)],fill=FISH_L,width=4)
    d.ellipse((x-3*scale,y+7*scale,x+scale,y+11*scale),fill=EDGE)

def face_on(d,large,face,kind):
    cx=256; span=350 if large else 244
    left,right=cx-span//2,cx+span//2
    y=139 if face=='north' else 208
    post_y=y-39 if face=='north' else y-6
    for x in (left+23,right-23):
        d.rounded_rectangle((x-19,post_y-25,x+19,post_y+44),
                            radius=7,fill=WOOD_D,outline=EDGE,width=7)
        d.line([(x-7,post_y-16),(x+5,post_y-16)],fill=WOOD_L,width=4)
        if face=='north':
            polygon(d,[(x-12,post_y+29),(x+1,post_y+42),
                       (x+32,y-1),(x+20,y-17)],WOOD,EDGE,5)
        else:
            polygon(d,[(x-12,post_y-15),(x+4,post_y-30),
                       (x+28,y+7),(x+9,y+13)],WOOD,EDGE,5)
    d.rounded_rectangle((left,y-18,right,y+14),radius=12,fill=EDGE)
    d.rounded_rectangle((left+5,y-14,right-5,y+9),radius=9,fill=BAMBOO)
    d.line([(left+18,y-8),(right-18,y-8)],fill=BAMBOO_L,width=6)
    d.line([(left+20,y+9),(right-20,y+9)],fill=WOOD_D,width=3)
    for x in range(left+56,right-8,99):
        d.line([(x,y-12),(x,y+8)],fill=WOOD_D,width=6)
        d.line([(x+4,y-10),(x+4,y+6)],fill=WOOD_L,width=3)
    if kind is None: return
    n=7 if large else 3
    for i in range(n):
        x=left+30+i*(span-60)/(n-1)
        drop=y+27+(i%2)*4
        d.line([(x,y+9),(x+1,drop)],fill=WOOD_D,width=9)
        d.line([(x,y+9),(x+1,drop)],fill=CORD,width=5)
        d.ellipse((x-6,y,x+6,y+14),fill=WOOD_D,outline=EDGE,width=4)
        (fish if kind=='fish' else meat)(d,x+1,drop,scale=1.02 if large else 1.1)

def edge_on(d,large,face,kind):
    # Different screen-space projection: along the wall, not horizontally across it.
    sign=1 if face=='east' else -1
    anchor_x=256-sign*(52 if large else 42)
    y1=116 if large else 143
    y2=365 if large else 323
    x1=anchor_x+sign*23; x2=anchor_x+sign*(68 if large else 40)
    for y in [y1+13,y2-13]:
        polygon(d,[(anchor_x-sign*20,y-28),(anchor_x+sign*5,y-28),
                   (anchor_x+sign*5,y+27),(anchor_x-sign*20,y+27)],WOOD_D,EDGE,6)
        d.line([(anchor_x-sign*12,y-17),(anchor_x-sign*12,y+15)],
               fill=WOOD_L,width=5)
    polygon(d,[(anchor_x,y1+3),(anchor_x+sign*13,y1+25),
               (x1+sign*22,y1+48),(x1+sign*8,y1+24)],WOOD,EDGE,5)
    polygon(d,[(anchor_x,y2-1),(anchor_x+sign*11,y2-18),
               (x2+sign*20,y2-18),(x2+sign*9,y2+6)],WOOD,EDGE,5)
    d.line([(x1,y1),(x2,y2)],fill=EDGE,width=31)
    d.line([(x1,y1),(x2,y2)],fill=BAMBOO,width=22)
    d.line([(x1-sign*5,y1),(x2-sign*5,y2)],fill=BAMBOO_L,width=6)
    for q in (0.19,0.51,0.81):
        xx=x1+(x2-x1)*q; yy=y1+(y2-y1)*q
        d.line([(xx-sign*11,yy-6),(xx+sign*11,yy+6)],fill=WOOD_D,width=7)
    if kind is None: return
    n=5 if large else 3
    for i in range(n):
        q=(i+0.45)/(n+0.15)
        xx=x1+(x2-x1)*q; yy=y1+(y2-y1)*q
        hx=xx+sign*(43 if large else 49); hy=yy+9
        d.line([(xx,yy),(hx,hy),(hx,hy+12)],fill=WOOD_D,width=8)
        d.line([(xx,yy),(hx,hy),(hx,hy+12)],fill=CORD,width=4)
        (fish if kind=='fish' else meat)(d,hx,hy+11,
                                        scale=.79 if large else .82,slant=sign*4)

def render(large,face,kind):
    im=Image.new('RGBA',(512,512),(0,0,0,0)); d=ImageDraw.Draw(im)
    if face in ('north','south'): face_on(d,large,face,kind)
    else: edge_on(d,large,face,kind)
    return im.resize((256,256),Image.Resampling.LANCZOS)

for large in (False,True):
    path=ROOT.parent/'WallDryingPoleLarge' if large else ROOT
    path.mkdir(parents=True,exist_ok=True)
    stem='WallDryingPoleLarge' if large else 'WallDryingPole'
    for face in ('north','south','east','west'):
        for kind,suffix in ((None,''),('meat','FilledMeat'),('fish','FilledFish')):
            render(large,face,kind).save(path/f'{stem}{suffix}_{face}.png',optimize=False)
    render(large,'north',None).save(path/f'{stem}_MenuIcon.png',optimize=False)
print('AMJ_WALLPOLE_SPRITES_OK 26')
