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
        publickey = epd.makeQR(wt.PublicKey())
        epd.Clear(0xFF)
        
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        drawred = ImageDraw.Draw(redimage1)
    #    global font , uppic , nextpic
        font24 = ImageFont.truetype(font, 20)
        drawblack.text((180, 40), 'Wallet', font = font24, fill = 0)
        drawblack.text((180, 80), 'public', font = font24, fill = 0)
        drawblack.text((180, 120), 'key', font = font24, fill = 0)
        newimage =publickey
        blackimage1.paste(newimage, (0,0))

        
        epd.display(epd.getbuffer(blackimage1))
        #epd.display(epd.getbuffer(redimage1))
        epd.sleep()

    except :
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()

def address():
    try:

        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        address = epd.makeQR(wt.Address())
        epd.Clear(0xFF)
       

        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        drawred = ImageDraw.Draw(redimage1)
    #    global font , uppic , nextpic
        font24 = ImageFont.truetype(font, 20)
        drawblack.text((180, 40), 'Wallet', font = font24, fill = 0)
        drawblack.text((180, 80), 'Address', font = font24, fill = 0)

        newimage =address
        blackimage1.paste(newimage, (0,0))
        
        epd.display(epd.getbuffer(blackimage1))
        #epd.display(epd.getbuffer(redimage1))
        epd.sleep()

    except :
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()
def privatekey():
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        #獲得 助記碼的QR Code
        mnemonics = wt.Mnemonics()

        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        #redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        font24 = ImageFont.truetype(font, 20)
        drawblack.text((180, 40), 'Must', font = font24, fill = 0)
        drawblack.text((180, 80), 'note', font = font24, fill = 0)
        drawblack.text((180, 120), 'words', font = font24, fill = 0)
        
        newimage = epd.makeQR(mnemonics)
        blackimage1.paste(newimage, (0,0))

        
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
