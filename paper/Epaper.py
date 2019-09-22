from paper.essential import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from Wallet import *


#font = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
font = '/usr/share/fonts/truetype/msttcorefonts/Comic_Sans_MS_Bold.ttf'
uppic = '/home/pi/EthereumWallet_local_API/paper/pics/up.bmp'
nextpic = '/home/pi/EthereumWallet_local_API/paper/pics/next.bmp'
wrongpic = '/home/pi/EthereumWallet_local_API/paper/pics/wrong.bmp'
addresspic = '/home/pi/EthereumWallet_local_API/paper/pics/address.bmp'

def publickey(publickey):
    try:

        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        publickey = epd.makeQR(publickey)
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

def address(address):
    try:

        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        address = epd.makeQR(address)

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
def privatekey(mnemonics,password):
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        #獲得 助記碼的QR Code

        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        #redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)
        font24 = ImageFont.truetype(font, 15)
        drawblack.text((170, 40), "<-Mnemonics:", font = font24, fill = 0)
        drawblack.text((180, 80), 'password:', font = font24, fill = 0)
        drawblack.text((180, 120), password, font = font24, fill = 0)
        
        newimage = epd.makeQR(mnemonics)
        blackimage1.paste(newimage, (0,0))

        
        newimage = Image.open(nextpic)
        blackimage1.paste(newimage, (240,150))

        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()
    except :
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        exit()
def boot():
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        font24 = ImageFont.truetype(font, 15)
        drawblack = ImageDraw.Draw(blackimage1)
        
        drawblack.text((30,70),'press key1 to show address',font = font24)        

        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()

    except:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        exit() 
def setup():
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        font24 = ImageFont.truetype(font, 15)
        drawblack = ImageDraw.Draw(blackimage1)
        
        drawblack.text((30, 70), 'There has no any accounts', font = font24, fill = 0)

        font24 = ImageFont.truetype(font, 10)
        drawblack.text((50,100),'press key1 to new an address',font = font24)        

        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()

    except:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
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

def setBalance(bal):
    try:
        epd = epd2in7.EPD()
        epd.init()
        print("Clear...")
        epd.Clear(0xFF)
        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        font24 = ImageFont.truetype(font, 25)
        drawblack = ImageDraw.Draw(blackimage1)
        print('send balance: ',bal)
        drawblack.text((30, 60),'send balance: '+bal, font = font24, fill = 0)
        epd.display(epd.getbuffer(blackimage1))
        epd.sleep()
    except:
        print('traceback.format_exc():\n%s'%(traceback.format_exc()))
        




