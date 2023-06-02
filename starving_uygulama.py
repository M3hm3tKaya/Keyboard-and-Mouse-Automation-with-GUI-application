import time
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image, ImageColor
import webcolors
from starvingArtist_python import Ui_MainWindow
from donusturme import cizim1, renkler , cizim2 ,AFK , cerveceRengiOlustur
import webbrowser
import requests
from bs4 import BeautifulSoup
import random

def donusturme(resim: str):
    im = Image.open(resim)
    print(im)
    w, h = 32, 32
    resized_name = "resized_.bmp"
    resized = im.resize((w, h))
    resized.save(f"{resized_name}")
    im.close()
    liste = []
    im = Image.open(resized_name)
    for x in range(32):
        for c in range(256 // 32):
            for y in range(32):
                for z in range(256 // 32):
                    liste.append(im.getpixel((y, x)))

    img1 = Image.new("RGB", (256, 256))
    img1.putdata(liste)
    resized_name = "_256_" + resized_name
    img1.save(f"{resized_name}")

    return resized_name

class Starving(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.passes = []
        txEdit1 = self.ui.textEdit.toPlainText().split("\n")
        txEdit2 = self.ui.textEdit_2.toPlainText().split("\n")
        for x in txEdit1:
            self.passes.append(x.split("- ")[-1])
        for x in txEdit2:
            self.passes.append(x.split("- ")[-1])


        self.ui.pushButton.clicked.connect(self.clicked_button)   #onayla 1
        try:
            self.ui.pushButton_2.clicked.connect(self.cizim)  #çizime başla
            self.ui.buton_afk.clicked.connect(self.cizim_2)
        except:
            pass

        self.ui.sifirla_button.clicked.connect(self.sifirla)

        self.pixel_butonlari = []
        self.tum_pixel_renkleri = []
        randomRenk = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for renk in range(1024):
            self.tum_pixel_renkleri.append(randomRenk)

        self.cb = QApplication.clipboard()

        self.yogunluk = 10
        self.aralık = 15

        self.ui.yogunluk_onay.clicked.connect(self.yogunluk_degistir)

        self.ui.buton_pass.clicked.connect(self.sayfaya_git)
        self.ui.button_yenile.clicked.connect(self.yenile)

        self.ui.buton_ekle.clicked.connect(self.ekleme)
        self.ui.buton_sifirla.clicked.connect(self.sifirlaResimSayilari)
        self.ui.buton_sil.clicked.connect(self.sil)
        self.ui.buton_afkKal.clicked.connect(self.afkKal)
        self.ui.fileSelect.clicked.connect(self.dosyaSec)
        self.ui.fileSelect_2.clicked.connect(self.dosyaSec2)
        self.ui.resimBox_gercek.setVisible(0)
        for y in range(32):
            for x in range(32):
                button = QPushButton("", self)
                button.move(20 + (x * self.aralık), 380 + (y * self.aralık))
                button.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 0px;")
                button.setMinimumSize(self.aralık, self.aralık)
                button.setMaximumSize(self.aralık, self.aralık)
                self.pixel_butonlari.append(button)
        for button in self.pixel_butonlari:
            QApplication.processEvents()
            renk = button.palette().button().color().getRgb()
            # print(renk)
            button.clicked.connect(partial(self.renk_ver, button))
        self.resimlerDict = {}
        self.resimlerListesi = []
    def dosyaSec(self):
        dosya = QFileDialog.getOpenFileName(self,"Choose Art",r"C:")
        self.ui.lineEdit.setText(dosya[0])
    def dosyaSec2(self):
        dosya = QFileDialog.getOpenFileName(self,"Choose Art",r"C:")
        self.ui.resim_liste.setText(dosya[0])


    def sil(self):
        silinecek_resim_index = self.ui.resimBox.currentIndex()
        resimAdi = self.ui.resimBox.itemText(silinecek_resim_index)
        self.ui.resimBox.removeItem(silinecek_resim_index)
        self.resimlerDict[resimAdi] -= 1
        self.resimlerListesi.pop(silinecek_resim_index)
        sayac = 0
        self.ui.resimBox_2.clear()
        for item in self.resimlerDict.items():
            sayac += item[1]
            if item[1] > 0:
                self.ui.resimBox_2.addItem(f"{item[0]} : {item[1]}")
        self.ui.resimSayi.setText(f"{sayac}")

        if self.ui.resimBox.count() <= 0:
            self.ui.buton_sil.setEnabled(0)
    def ekleme(self):

        resim = self.ui.resim_liste.text()

        if resim != "":
            resim_ad = resim.split("/")[-1]
            self.ui.resimBox.addItem(f"{resim_ad}")
            self.resimlerListesi.append(resim)
            self.ui.buton_sil.setEnabled(1)
            self.ui.resimBox.setCurrentIndex(self.ui.resimBox.count()-1)
            if resim_ad in self.resimlerDict.keys():
                self.resimlerDict[resim_ad] += 1
            else:
                self.resimlerDict[resim_ad] = 1
            self.ui.resimBox_2.clear()
            sayac = 0
            for item in self.resimlerDict.items():
                sayac += item[1]
                self.ui.resimBox_2.addItem(f"{item[0]} : {item[1]}")
            self.ui.resimSayi.setText(f"{sayac}")
    def sifirlaResimSayilari(self):

        self.resimlerDict = {}
        self.ui.resimBox.clear()
        self.ui.resimBox_2.clear()
        self.resimlerListesi = []
        self.ui.resimSayi.setText("0")
        if self.ui.resimBox.count() <= 0:
            self.ui.buton_sil.setEnabled(0)

    def yenile(self):
        self.ui.button_yenile.setText("Bekleyin...")
        self.ui.button_yenile.setEnabled(False)
        sayac = 0
        textler = {"text1":"","text2":""}
        sira_numarasi = 0
        seciliText = "text1"
        for x in self.passes:
            sira_numarasi += 1
            if sira_numarasi == 36:
                seciliText = "text2"
                sira_numarasi = 1
            QApplication.processEvents()
            self.ui.button_yenile.setText(f"Bekleyin... {len(self.passes)-sayac}")
            sayac+=1
            pass_kod = x
            r = requests.get(f"https://www.roblox.com/game-pass/{pass_kod}")
            print(r)
            soup = BeautifulSoup(r.content, "html.parser")
            robux = soup.find("span", {"class", "text-robux-lg wait-for-i18n-format-render"}).text
            print(f"{pass_kod}  :  {robux}")
            # x.setText(f"{pass_kod}  :{robux}")
            QApplication.processEvents()
            textler[seciliText] += f"{sira_numarasi}- {pass_kod} :{robux}\n"
            if seciliText == "text1":
                self.ui.textEdit.setText(textler[seciliText])
            else:
                self.ui.textEdit_2.setText(textler[seciliText])
        self.ui.button_yenile.setText("YENİLE")
        self.ui.button_yenile.setEnabled(True)

    def sayfaya_git(self):
        kod = self.ui.pass_kod_gir.text()
        webbrowser.open(f"https://www.roblox.com/game-pass/configure?id={kod}#!/sales")
        print(kod)

    def yogunluk_degistir(self):
        self.yogunluk = int(self.ui.yogunluk_edit.text())
        self.ui.yogunluk.setText(f"Seçili Yoğunluk : {self.yogunluk}")

    def renkleri_olustur(self):
        QApplication.processEvents()

        for i in range(len(self.pixel_butonlari)):
            button = self.pixel_butonlari[i]
            renk = self.tum_pixel_renkleri[i]
            button.setStyleSheet(
                "QPushButton{" + f"background-color: rgb{renk};border-radius: 0px;" + "}" + "QPushButton::hover{background-color : "
                + f"rgb({abs(renk[0] - 20)},{abs(renk[1] - 20)},{abs(renk[2] - 20)})" + ";}")
        #farklı renk 0.6
        #aynı renk 0.1


    def sifirla(self):
        self.renkleri_olustur()
    def renk_ver(self, buton: QPushButton):

        self.renkleri_olustur()
        print(buton)
        renk1 = buton.palette().button().color().getRgb()
        rgbTuple = (renk1[0],renk1[1],renk1[2])
        print(renk1)
        print(renk1[:3])
        print(rgbTuple)
        self.ui.lineEdit_2.setText(f"{webcolors.rgb_to_hex(rgbTuple)}")
        for x in self.pixel_butonlari:
            if x.palette().button().color().getRgb() == renk1:
                continue
            else:
                renk = x.palette().button().color().getRgb()
                r, g, b = renk[0], renk[1], renk[2]
                artma = 75
                if r + artma > 255:
                    r = 255
                else:
                    r += artma
                if g + artma > 255:
                    g = 255
                else:
                    g += artma
                if b + artma > 255:
                    b = 255
                else:
                    b += artma
                renk = (r, g, b)
                #print(renk)
                x.setStyleSheet(
                    "QPushButton{" + f"background-color: rgb{renk};border-radius: 0px;" + "}" + "QPushButton::hover{background-color : "
                    + f"rgb({abs(r - 20)},{abs(g - 20)},{abs(b - 20)})" + ";}")

    def clicked_button(self):

        self.ui.pushButton.setEnabled(0)
        QApplication.processEvents()
        yogunluk_degeri = self.yogunluk
        try:
            resim = self.ui.lineEdit.text()
            print(resim)
            self.donusmus_resim = donusturme(resim)
            self.ui.gercekResim.setStyleSheet(
                f"image:url({resim});"
            )
            self.ui.donusmusResim.setStyleSheet(
                f"image:url({self.donusmus_resim});"
            )
            self.tum_pixel_renkleri = renkler(self.donusmus_resim[5:],yogunluk_degeri)
            print(self.tum_pixel_renkleri)
            sayim = {}
            for x in self.tum_pixel_renkleri:
                QApplication.processEvents()
                sayim[x] = 0
            for x in self.tum_pixel_renkleri:
                QApplication.processEvents()
                sayim[x] += 1
            print(sayim)
            toplam_cizim_suresi = 0
            for x in sayim:
                QApplication.processEvents()
                toplam_cizim_suresi += sayim[x]*0.13
                toplam_cizim_suresi += 0.65
            print(toplam_cizim_suresi / 60)



            self.renkleri_olustur()


            self.ui.pushButton_2.setEnabled(1)
            self.ui.sifirla_button.setEnabled(1)
        except:
            print("hata")
        self.ui.pushButton.setEnabled(1)

    def cizim(self):
        print("cizim")
        time.sleep(1)
        cizim1(self.donusmus_resim[5:],self.yogunluk)
    def cizim_2(self):
        print("cizim2")
        cizim2(self.resimlerListesi,self.yogunluk)
    def afkKal(self):
        time.sleep(2)
        AFK()


uygulama = QApplication([])
pencere = Starving()
pencere.show()
uygulama.exec()


