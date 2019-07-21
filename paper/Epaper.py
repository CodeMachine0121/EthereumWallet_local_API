from paper.essential import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from Wallet import *
import RPi.GPIO as GPIO
import bluetoothctl
import bluetooth


wt= wallet()

font = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
uppic = './paper/pics/up.bmp'
nextpic = './paper/pics/next.bmp'
wrongpic = './paper/pics/wrong.bmp'
addresspic = './paper/pics/address.bmp'
bluepic = './paper/pics/bluetooth.bmp'
def publickey():
    try:

        epd = epd2in7.EPD()
        epd.init()

        publickey = epd.makeQR(wt.PublicKey())
        
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
        address = epd.makeQR(wt.Address())
        #epd.Clear(0xFF)
       

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

        #獲得 助記碼的QR Code
        mnemonics = wt.Mnemonics()

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
       

        print ("read bmp file on window")
        blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        redimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
        drawblack = ImageDraw.Draw(blackimage1)

        font24 = ImageFont.truetype(font, 20)

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


def Searching_Bluetooth_keyboard_func():
    epd = epd2in7.EPD()
    epd.init()

    print("The bluetooth is drawing")
    blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
   

    drawblack = ImageDraw.Draw(blackimage1)
    font18 = ImageFont.truetype(font, 20)
    
    drawblack.text((47, 5), 'Search for bluetooth', font = font18, fill = 0)
    
    newimage = Image.open(bluepic)
    blackimage1.paste(newimage, (83,40))
    
    newimage = Image.open(uppic)
    blackimage1.paste(newimage, (0,150))
    newimage = Image.open(nextpic)
    blackimage1.paste(newimage, (240,150))

    epd.display(epd.getbuffer(blackimage1))

def Findmykeyboard_func():

    print("Search target bluetooth device with address ...")
    nearby_devices = bluetooth.discover_devices(lookup_names = True) #Search device nearby
    j = len(nearby_devices) #How many devicess nearby
    print "There are",j,"devices"

    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name)) #print device address and name
        device_name = name

    epd = epd2in7.EPD()
    epd.init()
    
    blackimage1 = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255) # 298*126
    drawblack = ImageDraw.Draw(blackimage1)
    font18 = ImageFont.truetype(font, 20)
    
    drawblack.text((30, 5), 'Bluetooth device nearby :', font = font18, fill = 0)
    
    epd.display(epd.getbuffer(blackimage1))

    k = 0
    j = len(nearby_devices)
    while(k<j):
        k_now = j - k
        print"this is ",k_now," device"
        k_now -= 1
        n = 30
        drawblack.multiline_text((40, n),nearby_devices[k_now][1], font = font18, fill = 0, spacing=4, align="center")
        n +=25

        epd.init()
        print("Clear...")

        epd.display(epd.getbuffer(blackimage1))
        k += 1
        while True:
            key1state = GPIO.input(key1)
            key2state = GPIO.input(key2)
            key3state = GPIO.input(key3)
            key4state = GPIO.input(key4)
            #下一頁
            if key3state == False:
                print('Next button Pressed')
                while True:
                    key1state = GPIO.input(key1)
                    key2state = GPIO.input(key2)
                    key3state = GPIO.input(key3)
                    key4state = GPIO.input(key4)
                    #確定
                    if key4state == False:
                        print('Enter button Pressed')
                        bluetoothctl.Bluetoothctl().connect(nearby_devices[1][0])
                        import event_value
                        os.system('python event_value.py')
                        break
            #上一頁
            elif key2state == False:
                print('Up button Pressed')
                while True:
                    key1state = GPIO.input(key1)
                    key2state = GPIO.input(key2)
                    key3state = GPIO.input(key3)
                    key4state = GPIO.input(key4)
                    if key4state == False:
                        print('Enter button Pressed')
                        bluetoothctl.Bluetoothctl().connect(nearby_devices[0][0])
                        import event_value
                        os.system(event_value.py)
                        break
            #確定
            elif key4state == False:
                print('Enter button Pressed')
                bluetoothctl.Bluetoothctl().connect(nearby_devices[0][0])
                import event_value
                os.system(event_value.py)
                break
