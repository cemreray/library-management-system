from abc import ABC, abstractmethod

def metin_girdisi_al(mesaj, alan_adi):
    while True:
        deger = input(mesaj).strip()

        if deger == "":
            print(f"Hata: {alan_adi} boş bırakılamaz.")
        elif deger.isdigit():
            print(f"Hata: {alan_adi} sadece sayı olamaz.")
        elif not any(karakter.isalpha() for karakter in deger):
            print(f"Hata: {alan_adi} içinde en az bir harf olmalıdır.")
        else:
            return deger


def isim_girdisi_al(mesaj, alan_adi):
    while True:
        deger = input(mesaj).strip()

        if deger == "":
            print(f"Hata: {alan_adi} boş bırakılamaz.")
        elif not deger.replace(" ", "").isalpha():
            print(f"Hata: {alan_adi} sadece harflerden oluşmalıdır. Rakam veya özel karakter kullanılamaz.")
        else:
            return deger


def kayit_no_girdisi_al(mesaj):
    while True:
        deger = input(mesaj).strip()

        if deger == "":
            print("Hata: Kayıt numarası boş bırakılamaz.")
        elif deger.isalpha():
            print("Hata: Kayıt numarası sadece harflerden oluşamaz. Örnek: K001 veya D001")
        elif deger.isdigit():
            print("Hata: Kayıt numarası sadece sayılardan oluşamaz. Örnek: K001 veya D001")
        elif " " in deger:
            print("Hata: Kayıt numarası içinde boşluk olamaz.")
        else:
            return deger



class Menu:
    def menu_goster(self):
        print("\n--- Kütüphane Sistemi ---")
        print("1- Kitap Ekle")
        print("2- Kitap Sil")
        print("3- Kitap Güncelle")
        print("4- Kitapları Listele")
        print("5- Dergi Ekle")
        print("6- Dergi Sil")
        print("7- Dergi Güncelle")
        print("8- Dergileri Listele")
        print("9- Çıkış")



class Kaynak(ABC):
    def __init__(self, baslik, kayit_No):
        self._baslik = baslik
        self._kayit_No = kayit_No

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayit_No(self):
        return self._kayit_No

    @kayit_No.setter
    def kayit_No(self, value):
        self._kayit_No = value

    def __str__(self):
        return f"Başlık: {self.baslik}, Kayıt Numarası: {self.kayit_No}"



class Kitap(Kaynak):
    def __init__(self, baslik, kayit_No, yazar, tur):
        super().__init__(baslik, kayit_No)
        self._yazar = yazar
        self._tur = tur

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def tur(self):
        return self._tur

    @tur.setter
    def tur(self, value):
        self._tur = value

    def __str__(self):
        return f"{super().__str__()}, Yazar: {self.yazar}, Türü: {self.tur}"



class Dergi(Kaynak):
    def __init__(self, baslik, kayit_No, editor, yayin_evi):
        super().__init__(baslik, kayit_No)
        self._editor = editor
        self._yayin_evi = yayin_evi

    @property
    def editor(self):
        return self._editor

    @editor.setter
    def editor(self, value):
        self._editor = value

    @property
    def yayin_evi(self):
        return self._yayin_evi

    @yayin_evi.setter
    def yayin_evi(self, value):
        self._yayin_evi = value

    def __str__(self):
        return f"{super().__str__()}, Editör: {self.editor}, Yayın Evi: {self.yayin_evi}"



class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass



class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def kayitli_mi(self, kayit_No):
        for kitap in self.kitaplar:
            if kitap.kayit_No == kayit_No:
                return True
        return False

    def ekle(self):
        baslik = metin_girdisi_al("Kitabın başlığını giriniz: ", "Kitap başlığı")
        kayit_No = kayit_no_girdisi_al("Kitabın kayıt numarasını giriniz: ")

        if self.kayitli_mi(kayit_No):
            print("Hata: Bu kayıt numarasına ait bir kitap zaten var.")
            return

        yazar = isim_girdisi_al("Kitabın yazarını giriniz: ", "Yazar adı")
        tur = isim_girdisi_al("Kitabın türünü giriniz: ", "Kitap türü")

        kitap = Kitap(baslik, kayit_No, yazar, tur)
        self.kitaplar.append(kitap)

        print("Kitap başarıyla eklendi.")
        print("Toplam Kitap Sayısı:", self.kitap_sayisi())

    def sil(self):
        kayit_No = kayit_no_girdisi_al("Silinecek kitabın kayıt numarasını giriniz: ")

        for kitap in self.kitaplar:
            if kitap.kayit_No == kayit_No:
                self.kitaplar.remove(kitap)
                print("Kitap başarıyla silindi.")
                return

        print("Kitap bulunamadı.")

    def guncelle(self):
        kayit_No = kayit_no_girdisi_al("Güncellenecek kitabın kayıt numarasını giriniz: ")

        for kitap in self.kitaplar:
            if kitap.kayit_No == kayit_No:
                kitap.baslik = metin_girdisi_al("Yeni başlık: ", "Kitap başlığı")
                kitap.yazar = isim_girdisi_al("Yeni yazar: ", "Yazar adı")
                kitap.tur = isim_girdisi_al("Yeni tür: ", "Kitap türü")

                print("Kitap başarıyla güncellendi.")
                return

        print("Kitap bulunamadı.")

    def listele(self):
        if len(self.kitaplar) == 0:
            print("Kayıt bulunamadı.")
        else:
            print("\n--- Kitap Listesi ---")
            for kitap in self.kitaplar:
                print(kitap)

    def kitap_sayisi(self):
        return len(self.kitaplar)



class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def kayitli_mi(self, kayit_No):
        for dergi in self.dergiler:
            if dergi.kayit_No == kayit_No:
                return True
        return False

    def ekle(self):
        baslik = metin_girdisi_al("Derginin başlığını giriniz: ", "Dergi başlığı")
        kayit_No = kayit_no_girdisi_al("Derginin kayıt numarasını giriniz: ")

        if self.kayitli_mi(kayit_No):
            print("Hata: Bu kayıt numarasına ait bir dergi zaten var.")
            return

        editor = isim_girdisi_al("Derginin editörünü giriniz: ", "Editör adı")
        yayin_evi = metin_girdisi_al("Derginin yayınevini giriniz: ", "Yayınevi")

        dergi = Dergi(baslik, kayit_No, editor, yayin_evi)
        self.dergiler.append(dergi)

        print("Dergi başarıyla eklendi.")
        print("Toplam Dergi Sayısı:", self.dergi_sayisi())

    def sil(self):
        kayit_No = kayit_no_girdisi_al("Silinecek derginin kayıt numarasını giriniz: ")

        for dergi in self.dergiler:
            if dergi.kayit_No == kayit_No:
                self.dergiler.remove(dergi)
                print("Dergi başarıyla silindi.")
                return

        print("Dergi bulunamadı.")

    def guncelle(self):
        kayit_No = kayit_no_girdisi_al("Güncellenecek derginin kayıt numarasını giriniz: ")

        for dergi in self.dergiler:
            if dergi.kayit_No == kayit_No:
                dergi.baslik = metin_girdisi_al("Yeni başlık: ", "Dergi başlığı")
                dergi.editor = isim_girdisi_al("Yeni editör: ", "Editör adı")
                dergi.yayin_evi = metin_girdisi_al("Yeni yayınevi: ", "Yayınevi")

                print("Dergi başarıyla güncellendi.")
                return

        print("Dergi bulunamadı.")

    def listele(self):
        if len(self.dergiler) == 0:
            print("Kayıt bulunamadı.")
        else:
            print("\n--- Dergi Listesi ---")
            for dergi in self.dergiler:
                print(dergi)

    def dergi_sayisi(self):
        return len(self.dergiler)



menu = Menu()
kitap_islem = KitapIslem()
dergi_islem = DergiIslem()

while True:
    menu.menu_goster()
    secim = input("Yapmak istediğiniz işlemi seçin (1-9): ").strip()

    if secim == "":
        print("Hata: Seçim boş bırakılamaz.")
    elif not secim.isdigit():
        print("Hata: Seçim sadece sayı olmalıdır.")
    elif secim == "1":
        kitap_islem.ekle()
    elif secim == "2":
        kitap_islem.sil()
    elif secim == "3":
        kitap_islem.guncelle()
    elif secim == "4":
        kitap_islem.listele()
    elif secim == "5":
        dergi_islem.ekle()
    elif secim == "6":
        dergi_islem.sil()
    elif secim == "7":
        dergi_islem.guncelle()
    elif secim == "8":
        dergi_islem.listele()
    elif secim == "9":
        print("Programdan çıkılıyor. İyi günler!")
        break
    else:
        print("Hata: Lütfen 1-9 arasında seçim yapınız.")