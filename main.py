import random
import time
import webcolors
import keyboard
from PIL import Image, ImageColor
import autoit

hexListe = []
im2 = Image.open("labirent1.bmp")
resimListe = ["resized_giga.bmp", "resized_incikupeli.bmp", "resizded_mona.bmp", "resizded_rock.bmp",
              "resized_animekız3.bmp", "resized_animekız2.bmp"]
resim = random.choice(resimListe)
print(resim)

hexListe4 = []

# for x in range(32):#1e1f1a
#     for y in range(32):
#         hexListe.append(webcolors.rgb_to_hex(im2.getpixel((y,x))))
#

pixel = 32
oran = int(32 / pixel)

for x in range(pixel):
    for c in range(oran):
        for y in range(pixel):
            for z in range(oran):
                hexListe4.append(webcolors.rgb_to_hex(im2.getpixel((y, x))))

hexListe = hexListe4
hexListeNew = []
rgbListe = []
newRGBListe = []
for x in hexListe:
    color = ImageColor.getcolor(x, "RGB")
    rgbListe.append(color)
print(rgbListe)

eklenenler = []
yogunluk = 5
for x in range(1024):
    newRGBListe.append("0")
for x in rgbListe:
    sayac = -1
    for y in rgbListe:
        sayac += 1
        if sayac in eklenenler:
            continue
        if abs(x[0] - y[0]) < yogunluk and abs(x[1] - y[1]) < yogunluk and abs(x[2] - y[2]) < yogunluk:
            y = x
            newRGBListe[sayac] = y
            eklenenler.append(sayac)

        else:
            newRGBListe[sayac] = y

for x in newRGBListe:
    hexCode = webcolors.rgb_to_hex(x)
    hexListeNew.append(hexCode)
hexListe = hexListeNew
print(len(hexListe))
print(hexListe)

time.sleep(3)

secili_renk = ""
liste_sayac = 0
pixel_sayac = 0
y = 176
speed = 2  # aeafa8
# time.sleep(1)
# (879, 734) yazı yeri
# (914, 860) renk butonu#0f0e17


mode = 0  # mode = 1 satır satır çizer / mode = 0 önce aynı renk olanları boyar
exit = 0

file = open("SonSatir.txt", "r")
sonSatir = int(file.read())
file.close()
if mode:
    for i in range(32):
        print(i)
        if i < sonSatir - 1:  # sayi yerine hangi satırda kaldıysan o satır sayısını gir ordan başlıcak çizmeye     NOT: sadece satır satır çizmede kullanılır!
            liste_sayac += 32
            y += 19
            continue
        if exit == 1:
            file = open("SonSatir.txt", "w")
            file.write(str(i))
            file.close()
            break

        for x in range(664, 664 + (19 * 32), 19):

            if i != 0 and i < 0:
                liste_sayac += 1
                continue  # 262b2a

            if secili_renk != hexListe[liste_sayac]:
                secili_renk = hexListe[liste_sayac]
                autoit.mouse_click("left", 1085, 827, speed=speed)

                autoit.mouse_click("left", 1082, 738, speed=speed)

                time.sleep(0.1)
                if keyboard.is_pressed("end"):
                    exit = 1
                    break
                keyboard.write(f"{secili_renk}")
                time.sleep(0.1)
                autoit.mouse_click("left", 1085, 827, speed=speed)

            autoit.mouse_click("left", x, y, speed=speed)

            liste_sayac += 1

        y += 19


else:
    for a in hexListe:
        if exit == 1:
            break

        y = 176
        if a != 0:
            secili_renk = a
            # hexListe[liste_sayac] = 0
            autoit.mouse_click("left", 1085, 827, speed=speed)

            autoit.mouse_click("left", 1082, 738, speed=speed)

            time.sleep(0.1)
            keyboard.write(f"{secili_renk}")
            time.sleep(0.1)

            autoit.mouse_click("left", 1085, 827, speed=speed)


        else:
            continue

        liste_sayac = 0
        pixel_sayac += 1
        for i in range(32):

            for x in range(664, 664 + (19 * 32), 19):

                # if i != 4 and i < 4:
                #     liste_sayac += 1
                #     continue

                if keyboard.is_pressed("end"):
                    exit = 1
                    break

                if secili_renk == hexListe[liste_sayac] and hexListe[liste_sayac] != 0:
                    hexListe[liste_sayac] = 0
                    autoit.mouse_click("left", x, y, speed=speed)
                    print(1)

                else:
                    liste_sayac += 1
                    continue

                liste_sayac += 1

            y += 19
