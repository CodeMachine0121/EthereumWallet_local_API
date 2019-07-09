#!/usr/bin/python
# -*- coding:utf-8 -*-
from essential import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


font = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
uppic = './pics/up.bmp'
nextpic = './pics/next.bmp'

try:
    epd = epd2in7.EPD()
    epd.init()
    print("Clear...")
    epd.Clear(0xFF)

    print ("read bmp file on window")
    blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
    #redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
    drawblack = ImageDraw.Draw(blackimage1)
    #drawred = ImageDraw.Draw(redimage1)
    font24 = ImageFont.truetype(font, 18)
    drawblack.text((20, 0), 'verify your password', font = font24, fill = 0)
    drawblack.line((30, 100, 225, 100), fill = 0)

    newimage = Image.open(uppic)
    blackimage1.paste(newimage, (0,150))
    newimage = Image.open(nextpic)
    blackimage1.paste(newimage, (240,150))
    epd.display(epd.getbuffer(blackimage1))

    epd.sleep()

except :
    print ('traceback.format_exc():\n%s' % traceback.format_exc())
    exit()

