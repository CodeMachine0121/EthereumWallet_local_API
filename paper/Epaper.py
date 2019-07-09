from paper.essential import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from Wallet import *

wt= wallet()

font = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
uppic = './paper/pics/up.bmp'
nextpic = './paper/pics/next.bmp'
wrongpic = './paper/pics/wrong.bmp'
addresspic = './paper/pics/address.bmp'
def publickey():
    try:

        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        epd.Clear(0xFF)
        address = epd.makeQR(wt.PublicKey())

        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        drawred = ImageDraw.Draw(redimage1)
    #    global font , uppic , nextpic
        font24 = ImageFont.truetype(font, 18)
        drawblack.text((32, 0), 'My pocket qrcode', font = font24, fill = 0)
        newimage =address
        blackimage1.paste(newimage, (65,25))
        newimage = Image.open(uppic)
        blackimage1.paste(newimage, (0,150))
        newimage = Image.open(nextpic)
        blackimage1.paste(newimage, (240,150))

        epd.display(epd.getbuffer(blackimage1))
        #epd.display(epd.getbuffer(redimage1))
        epd.sleep()

    except :
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()
def privatekey(strs):
    strs = strs.split(" ")
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        #獲得 助記碼的QR Code
        mnemonics = wt.Mnemonics().split(' ')

        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        #redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        font24 = ImageFont.truetype(font, 15)
        drawblack.text((21, 0), 'Must note this words', font = font24, fill = 0)

        #把 24個助記碼分半
        m1=''
        m2=''
        for i in range(0,12):
            m1+=mnemonics[i]
            m1+=','
        for i in range(12,24):
            m2+=mnemonics[i]
            m2+=','
        newimage = epd.makeQR(m1)
        blackimage1.paste(newimage, (0,25))

        newimage = epd.makeQR(m2)
        blackimage1.paste(newimage, (120,25))


        newimage = Image.open(uppic)
        blackimage1.paste(newimage, (0,150))

        newimage = Image.open(nextpic)
        blackimage1.paste(newimage, (240,150))

        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()
    except :
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()

def wrong():
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        epd.Clear(0xFF)

        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)

        font24 = ImageFont.truetype(font, 24)

        newimage = Image.open(wrongpic)
        blackimage1.paste(newimage, (0,0))

        newimage = Image.open(uppic)
        blackimage1.paste(newimage, (0,150))
        newimage = Image.open(nextpic)
        blackimage1.paste(newimage, (240,150))
        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()

    except:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()
