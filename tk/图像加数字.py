#!/usr/bin/ruby -w
# -*- coding : utf-8 -*-

from PIL import Image,ImageFont, ImageDraw

# im=Image.open('./背景图.gif')
im=Image.open('./美女.jpg')

draw=ImageDraw.Draw(im)

print(im.size)

fontsize=min(im.size)//4
print(fontsize)

font=ImageFont.truetype('./Truetype.ttf',fontsize)
draw.text((im.size[0]-fontsize,0),'丁',font=font,fill=(0,255,0))
im.save('./aaa.jpg','jpeg')
# im.save('./aaa.gif','gif')

