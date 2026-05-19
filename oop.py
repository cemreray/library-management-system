from abc import ABC, abstractmethod

class Menu:
    def menu_goster(self):
        print('---Kütüphane Sistemi---')
        print('1- Kitap Ekle')
        print('2- Kitap Sil')
        print('3- Kitap Güncelle')
        print('4- Kitapları Lİstele')
        print('5- Dergi Ekle')
        print('6- Dergi Sil')
        print('7- Dergi Güncelle')
        print('8- Dergileri Listele')
        print('9- Çıkış')


class Kaynak(ABC):
    def __init__(self, baslik, kayit_No):
        self._baslik = baslik
        self._kayit_No = kayit_No

    @property
    def baslik(self):
        return self._baslik
        
    @baslik.setter
    def baslik(self,value):
        self._baslik = value

    @property 
    def kayit_No(self):
        return self._kayit_No
        
    @kayit_No.setter
    def kayit_No(self,value):
        self._kayit_No = value

    def __str__(self):
        return f"Başlık: {self.baslik}, Kayıt Numarası {self.kayit_No}"
        
class Kitap(Kaynak):
    def __init__(self, baslik, kayit_No,yazar,tur):
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
    def __init__(self, baslik,kayit_No,editor, yayin_evi):
        super().__init__(baslik, kayit_No)
        self._editor = editor
        self._yayin_evi = yayin_evi

    @property
    def editor(self):
        return self._editor
        
    @editor.setter
    def editor(self,value):
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
        baslik = input("Kitabın başlığını giriniz: ")
        kayit_No = input("Kitabın kayıt numarasını giriniz: ")

        if self.kayitli_mi(kayit_No):
            print("Bu kayıt numarasına ait bir kitap var.")
            return
        
        yazar = input("Kitabın yazarını giriniz: ")
        tur   = input("Kitabın türünü giriniz: ")
        
        kitap = Kitap(baslik, kayit_No, yazar, tur)
        self.kitaplar.append(kitap)

        print("Kitap başarıyla eklendi.")
        print("Toplam Kitap Sayısı: ", self.kitap_sayisi())

    def sil(self):
        kayit_No = input("Silinecek kitabın kayıt numarasını giriniz: ")

        for kitap in self.kitaplar:
            if kitap.kayit_No == kayit_No:
                self.kitaplar.remove(kitap)
                print("Kitap başarıyla silindi.")
                return
        print("Kitap bulunamadı.")

    def guncelle(self):
        kayit_No = input("Güncellenecek kitabın kayıt numarasını giriniz: ")

        for kitap in self.kitaplar:
            if kitap.kayit_No == kayit_No:
                kitap.baslik = input("Yeni başlık: ")
                kitap.yazar = input("Yeni yazar:. ")
                kitap.tur = input("Kitabın türü: ")
                print("Kitap başarıyla güncellendi.")
                return
        print("Kitap bulunamadı...")
        
    def listele(self):
        if len(self.kitaplar) == 0:
            print("Kayıt bulunamadı...")
        else:
            print("\n---Kitap Listesi---")
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
        baslik = input("Derginin başlığını giriniz: ")
        kayit_No = input("Derginin kayıt numarasını giriniz: ")

        if self.kayitli_mi(kayit_No):
            print("Bu kayıt numarasına ait bir dergi var.")
            return
        
        editor = input("Derginin editörünü giriniz: ")
        yayin_evi = input("Derginin yayınevini giriniz: ")
        
        dergi = Dergi(baslik, kayit_No, editor, yayin_evi)
        self.dergiler.append(dergi)

        print("Dergi başarıyla eklendi.")
        print("Toplam Dergi Sayısı: ", self.dergi_sayisi())

    def sil(self):
        kayit_No = input("Silinecek derginin kayıt numarasını giriniz: ")

        for dergi in self.dergiler:
            if dergi.kayit_No == kayit_No:
                self.dergiler.remove(dergi)
                print("Dergi başarıyla silindi.")
                return
        print("Dergi bulunamadı.")

    def guncelle(self):
        kayit_No = input("Güncellenecek derginin kayıt numarasını giriniz: ")

        for dergi in self.dergiler:
            if dergi.kayit_No == kayit_No:
                dergi.baslik = input("Yeni başlık: ")
                dergi.editor = input("Yeni editör:. ")
                dergi.yayin_evi = input("Yeni yayınevi: ")
                print("Dergi başarıyla güncellendi.")
                return
        print("Dergi bulunamadı...")
        
    def listele(self):
        if len(self.dergiler) == 0:
            print("Kayıt bulunamadı...")
        else:
            print("\n---Dergi Listesi---")
            for dergi in self.dergiler:
                print(dergi)

    def dergi_sayisi(self):
        return len(self.dergiler)
    
menu = Menu()
kitap_islem = KitapIslem()
dergi_islem = DergiIslem()

while True:
        menu.menu_goster()
        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

        if secim == '1':
            kitap_islem.ekle()
        elif secim == '2':
            kitap_islem.sil()
        elif secim == '3':
            kitap_islem.guncelle()
        elif secim == '4':
            kitap_islem.listele()
        elif secim == '5':
            dergi_islem.ekle()
        elif secim == '6':
            dergi_islem.sil()
        elif secim == '7':
            dergi_islem.guncelle()
        elif secim == '8':
            dergi_islem.listele()
        elif secim == '9':
           print("Programdan çıkılıyor...")
           break
        else:
            print("Hatalı seçim. Lütfen 1-9 arasında seçim yapınız.")

