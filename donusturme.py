import random
import time
import webcolors
import keyboard
from PIL import Image, ImageColor
import autoit

def renkler(resim: str, yogunluk_degeri: int):
    print(resim)
    im2 = Image.open(resim)
    hexListe4 = []

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
    eklenenler = []
    yogunluk = yogunluk_degeri
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
    return newRGBListe


def cizim1(resim: str, yogunluk_degeri: int):
    print(resim)
    im2 = Image.open(resim)
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
    yogunluk = yogunluk_degeri
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

    sonSatir = 0

    if mode:
        for i in range(32):
            print(i)
            if i < 20 - 1:  # sayi yerine hangi satırda kaldıysan o satır sayısını gir ordan başlıcak çizmeye     NOT: sadece satır satır çizmede kullanılır!
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


# cizim1("resized_giga.bmp")

sozlukRenk = {}

sozluk = {"inci2.png": "Girl With a Pearl Earring", "beluga.png": "Beluga", "rock.png": "The Rock",
          "Mona2.png": "Mona_Lisa",
          "elgato.png": "Elgato", "Hecker.png": "Hecker", "wednesday2.png": "Wednesday", "giga.png": "Giga Chad",
          "bale.png": "Sigma",
          "starry.png": "Starry Night", "blue1.png": "Snake Left", "blue2.png": "Snake Middle",
          "blue3.png": "Snake Right", "lambo1.png": "Lambo Left",
          "lambo2.png": "Lambo Middle", "lambo3.png": "Lambo Right", "bugatti1.png": "Bugatti Left",
          "bugatti2.png": "Bugatti Middle",
          "bugatti3.png": "Bugatti Right", "yoda1.png": "Yoda", "porsche1.png": "Porsche Left",
          "porsche2.png": "Porsche Middle", "porsche3.png": "Porsche Right",
          "chad2.png": "Giga Chad"}

renkSkalasiY1 = 740  # ilk renk skalası Y değeri = 740
renkSkalasiY2 = 785  # ikinci renk skalası Y değeri = 785

renklerSozluk = {"inci2.png": (885, 993), "beluga.png": (795, 997), "rock.png": (853, 902), "Mona2.png": (890, 946),
                 "elgato.png": (866, 960), "Hecker.png": (973, 1130), "wednesday2.png": (1160, 1111),
                 "giga.png": (751, 1108), "chad2.png": (751, 1108), "bale.png": (751, 1147),
                 "starry.png": (1102, 894), "blue1.png": (755, 1167), "blue2.png": (755, 1167),
                 "blue3.png": (755, 1167), "lambo1.png": (755, 1167),
                 "lambo2.png": (755, 1167), "lambo3.png": (755, 1167), "bugatti1.png": (751, 1077),
                 "bugatti2.png": (751, 1077),
                 "bugatti3.png": (751, 1077), "yoda1.png": (976, 1001)}


def cerveceRengiOlustur(resimAdi):
    print(resimAdi)
    try:
        skala_1x = renklerSozluk[resimAdi][0]
        skala_2x = renklerSozluk[resimAdi][1]
    except:
        skala_1x = 755
        skala_2x = 1167
    speed = 2
    time.sleep(0.1)
    autoit.mouse_click("left", skala_1x, renkSkalasiY1, speed=speed)
    time.sleep(0.1)
    autoit.mouse_click("left", skala_2x, renkSkalasiY2, speed=speed)
    time.sleep(0.2)


def cizim2(resimList: list, yogunluk_degeri: int):
    for resim in resimList:
        try:
            print(resim.split("/")[-1])
            yazilicak_isim = sozluk[resim.split("/")[-1]]
        except:
            yazilicak_isim = "Name"
        print(resim)
        im2 = Image.open(resim)
        im2 = im2.resize((32, 32))
        im2.save("_12_123.bmp")
        im2.close()
        im2 = Image.open("_12_123.bmp")
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
        yogunluk = yogunluk_degeri
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
        sonSatir = 0

        if mode:
            for i in range(32):
                print(i)
                if i < 20 - 1:  # sayi yerine hangi satırda kaldıysan o satır sayısını gir ordan başlıcak çizmeye     NOT: sadece satır satır çizmede kullanılır!
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
        if exit == 1:
            break
        time.sleep(0.1)
        autoit.mouse_click("left", 989, 893, speed=speed)  # next (resmi bitir)
        time.sleep(3)
        autoit.mouse_click("left", 964, 208, speed=speed)  # isim girme
        time.sleep(1)
        keyboard.write(yazilicak_isim)
        time.sleep(1)
        cerveceRengiOlustur(resim.split("/")[-1])
        autoit.mouse_click("left", 1137, 878, speed=3)  # finish
        time.sleep(3)
        autoit.mouse_click("left", 1137, 878, speed=speed)  # finish
        time.sleep(3)
        keyboard.press("space")
        time.sleep(0.1)
        keyboard.release("space")
        time.sleep(5)
        keyboard.press("d")
        time.sleep(0.5)
        keyboard.release("d")
        time.sleep(3)
        autoit.mouse_get_pos()


def AFK():
    exit = 0
    while exit == 0:
        keyboard.write("/")
        time.sleep(1)
        keyboard.write("")  # chate yazı
        time.sleep(1)
        keyboard.press_and_release("enter")
        renk = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        newRGBListe = []
        for x in range(1024):
            newRGBListe.append(renk)
        hexListeNew = []
        for x in newRGBListe:
            hexCode = webcolors.rgb_to_hex(x)
            hexListeNew.append(hexCode)
        hexListe = hexListeNew
        print(len(hexListe))
        print(hexListe)
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

        if mode == 0:
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
