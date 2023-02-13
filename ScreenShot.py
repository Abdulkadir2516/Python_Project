from pynput.keyboard import Key, Listener
import os
import pyautogui

# mousenin konum bilgilerini getirir
#pyautogui.displayMousePosition()

check = True

while check:
    konum = input("konum bilgisi girmek için 1e fare konumunuzu öğrenmek için 2 ye basın")
    if(konum == "1"):
        x = int(input("başlangıç x değeri "))
        y = int(input("başlangıç y değeri "))
        en = int(input("bitiş x değeri "))
        boy = int(input("bitiş y değeri "))
        print("Resim Çekmek İçin print_scrreen düğmesine basınız: ")

        check = False

    else:
        pyautogui.displayMousePosition()


def on_press(key):
    print("basılan tus => {}".format(key))
    if key == Key.print_screen:
        icindekiler = os.listdir('./')

        sayi = len(icindekiler)

        isim = "Screenshot_{}.jpg".format(sayi+1)

        if os.path.isfile(isim):
            print("var")
        else:
            global x
            global y
            global en
            global boy
            a = en- x
            b = boy-y
            # konum bilgisinin girileceği yer region=(x,y,en,boy)
            pyautogui.screenshot(isim,region=(x,y,a,b))
            
from pynput import keyboard, mouse

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()


input()

