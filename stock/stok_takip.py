"""
Stok Takip Programı part1

kasiyerler => k_ad, ad, soyad, sifre, tel, adres, mail
yönetici => k_ad, ad, soyad, sifre, tel, adres, mail


ürünler => barkodu, ürün adi, cinsi, tedarikçi, alış fiyatı, satış fiyatı, 
            alt limit ürün adeti

satis = barkodu, ürün adi, cinsi, tedarikçi, alış fiyatı, satış fiyatı, 
            alt limit ürün adeti
            

kasiyerin özellikleri:
    
    1- ürün satma
    2- ürün ekleme
    3- İade alma

ürün satma barkodu okuyup ürünü bulacak fiyatını ve biligilerini 
gösterecek toplam tutar ekrana gelecek onaylandığı zaman stoktan eksilecek

ürün ekleme ürün biliglerini dosyaya yazma


"""
import datetime
a = datetime.datetime.now() # şimdi
suan= datetime.datetime.strftime(a, '%d-%m-%Y' )
saat= datetime.datetime.strftime(a, '%X' )



kasiyerler = open("source/kasiyerler.txt", "r") # dosya okuma işlemi read 

#print(kasiyerler.read())

# b = str(kasiyerler.read())

# print(b.split(","))

data = str(kasiyerler.read())

# =============================================================================
# 
# for i in data.split("\n"):
#     
#     for j in i.split(","):
#         print(j,"\t\t", end=" ")
#     
#     print()
#  
#     
# input()
# =============================================================================

def urun_listeleme():
    
    urunler = open("source/ürünler.txt", "r")
    
    urun = str(urunler.read())
    
    düzenli = urun.split("\n")
    
    for i in düzenli:
        print(i)
    
# ÜRÜN EKLEME İŞLEMİ 
def urun_ekleme():
    
    urunler = open("source/ürünler.txt", "r")
    
    urun = str(urunler.read())
    
    x = urun.split(",")
    
    urunler = open("source/ürünler.txt", "a")
    
    liste = []
    
    for i in range(8):
        
        bil = str(x[i]) + " Değerini Giriniz "
        
        a = input(bil)
        
        liste.append(a)
    
    
    urunler.write("\n")
    
    for j in liste:
        
        urunler.write(str(j)+",")


    urunler = open("source/ürünler.txt", "r")
    urunler.read()




# ÜRÜN SATMA İŞLEMİ
# 
# ürün satma işlemi döngü içerisinde olup belirlenen bir tuşa basılınca döngüden çık
#
# Barkod numarası girilip ürün bulunacak yoksa ürün bulunamadı diyecek
# girilien barkod numaraları geçici listeye gönderilip daha sonra onaylandıktan sonra 
# ürün adeti sistemden çıkılacak ve satışlara eklenecek 
# 
# ürün satıldığı zaman ürün adeti alt limitten az olduğunda uyarı verecek
def satıs_yapma():
    
    s = list()
        
    urunler = open("source/ürünler.txt", "r")
       
    urun = str(urunler.read())
        
    y = urun.split(",")
        
    while True:
        
        a = datetime.datetime.now() # şimdi
        suan= datetime.datetime.strftime(a, '%d-%m-%Y' )
        saat= datetime.datetime.strftime(a, '%X' )
    
        ad = int(input("Ürün Adeti Giriniz: "))
    
        brk = input("Barkod Numarasını Giriniz: ")
        
        if brk == "@":
            break
    
    
        kontrol = False
        
        for i in range(8, len(y), 8):
            # print(y[i])
            
            if y[i] == "\n"+brk:
                kontrol = True
    
        
        if kontrol:
                    
            indeks = y.index("\n"+brk)
            
            print("Barkodu \t\t=> {} \nÜrün Adı \t\t=> {} \nAlış Fiyatı \t\t=> {} \nAdeti \t\t\t=> {} \nTutar \t\t\t=> {}".format(brk, y[indeks+1], y[indeks+4], ad, int(ad)*int(y[indeks+4])))
            print("Tarih \t\t\t=>", suan)
            print("Saat \t\t\t=>", saat)
            print("\n\n")
            # print(indeks)
            #(brk, y[indeks+1], y[indeks+4], ad, int(ad)*int(y[indeks+4])
            s.append(brk) # barkod
            s.append(y[indeks+1]) # ürün adı
            s.append(y[indeks+4]) # satış fiyatı
            s.append(ad) # adeti
            s.append(int(ad)*int(y[indeks+4])) # adet*satış fıyatı => Tutar
            s.append(suan) # tarih
            s.append(saat) # saat
            
            y[indeks+7] = str(int(y[indeks+7])-int(ad))
            
            
        
        else:
            print("barkod numarası kayıtlı değil")
        
    
    onay = input("Alışverisi onaylıyormusunuz (E/H)? ")
    
    if onay.lower() == "e":
            
        urunler = open("source/ürünler.txt", "w")
        # ürün adetini güncelleme
        for j in range(len(y)-1):
            
            urunler.write(str(y[j])+",")
    
    
        urunler = open("source/ürünler.txt", "r")
        urunler.read()
    
        
        satislar = open("source/anlik_satis.txt","w")
    
        a =0
        for x in s:
            a +=1
            
            satislar.write(str(x)+",")
            
            if a == 7:
                
                satislar.write("\n")
                a = 0
    
    
        satislar = open("source/anlik_satis.txt", "r")
        print(satislar.read())
    
    
    
        satislar2 = open("source/anlik_satis.txt", "r")
    
        bs = str(satislar2.read())
        
    
        an = bs.split(",")
    
        print(an)
        
        onay2 = input("Anlık satıştan ürün çıkarılacak mı (E/H)")
    
        if onay2.lower() == "e":
            kosul = True
            while kosul:
                print(an)
                
                iadeB = input("İade Edilecek Ürünün barkodunu giriniz: ")
                #iadead = input("İade Edilecek Ürünün adetini giriniz: ")
    
                indeks2 = an.index(iadeB)
    
                if an[indeks2] == iadeB:
                    iadead = input("İade Edilecek Ürünün adetini giriniz: ")
                    an[indeks2 + 3] = int(an[indeks2 + 3]) - int(iadead)
    
    
                    satislar3 = open("source/anlik_satis.txt", "w")
                    # ürün adetini güncelleme
                    for j in range(len(an)-1):
                        
                        satislar3.write(str(an[j])+",")
    
    
                    satislar3 = open("source/anlik_satis.txt", "r")
                    satislar3.read()
    
                    
                    
                    iade2 = input("İade Edilecek Başka Ürün Varmı (E/H) ")
    
                    if iade2.lower() != "e":
    
                        satis = open("source/satislar.txt", "a")
    
                        for j in range(len(an)-1):
                        
                            satis.write(str(an[j])+",")
    
                        kosul = False
                        satis.write("\n")
                        
                    satis = open("source/satislar.txt", "r")
                    satis.read()
                
        else:
            satis = open("source/satislar.txt", "a")
    
            for j in range(len(an)-1):
                satis.write(str(an[j])+",")
    
            satis.write("\n")
            
            satis = open("source/satislar.txt", "r")
            satis.read()
"""
onay2 birkaç defa alınacak döngü içerisinde

thislist = ["apple", "banana", "cherry"]
del thislist[0:2]
print(thislist)


iade ürün çıkarılacak çıkarıldıktan sonra tekra iade varmı
diye sorulup yoksa satışlara verileri yazacak
varsa başa dönecek

iade ürün hiç yoksa veriler satışlara eklenecek


"""

def kasiyer_ekle():
    
    kasiyer = open("source/kasiyerler.txt", "a")
    
    a = ["kullanici_adi","isim","soyisim","sifre","telefon","adres","mail"]
    
    kisi = []
    
    for i in a:
        
        söz = i + " değerini giriniz:"
        
        x = input(söz)
        
        kisi.append(x)
        
    
    kasiyer.write("\n")

    for j in kisi:
         
        kasiyer.write(str(j) + ",")
    
def kasiyer_cikart():
    
    kasiyer = open("source/kasiyerler.txt", "r")
    
    kas = str(kasiyer.read()).split(",")
    
    cıkartma = input("Çıkarılacak Kişinin kullanıcı adını giriniz: ")
    
    for i in range(0,len(kas)-1,7):
        
        if kas[i] == cıkartma:
            
            del kas[i:i+7]
       
    
    kasiyer2 = open("source/kasiyerler.txt", "w")
    
    say = 0
    for j in kas:
        say +=1 
        
        kasiyer2.write(str(j)+",")
        
        if say == 7:
            
            kasiyer2.write("\n")
            say=0

    kasiyer2 = open("source/kasiyerler.txt", "r")
    kasiyer2.read()


# KULLANICI SORGULAMA İŞLEMİ

check = False

veriler = data.split(",")

k_ad = input("kullanıcı adınızı giriniz:")

for i in range(7,len(veriler),7): # for i in veriler:
    
    if "\n"+k_ad == str(veriler[i]):
        check = True

if k_ad == "Krieger":
    
    check = False
    
    print("Giriş Başarılı Hoşgeldiniz", "Yönetici")
    
    while True:
    
        print("""
              1- Ürün Ekleme 
              2- Satış Yapma
              3- Ürün Listeleme
              4- Kasiyer Ekleme
              5- Kasiyer Çıkartma
              6- Çıkış
              """ )
        secim = input("Seçim Yapınız:")
        
        if secim == "1":
            urun_ekleme()
            
        elif secim == "2":
            satıs_yapma()
            
        elif secim == "3":
            urun_listeleme()
            
        elif secim == "6":
            break
        
        elif secim == "4":
            kasiyer_ekle()
        
        elif secim == "5":
            kasiyer_cikart()



if check:
    
    sifre = input("Şifre Giriniz:")
    
    indeks = veriler.index("\n"+k_ad)
    
    if sifre == veriler[indeks+3]:
        print("Giriş Başarılı Hoşgeldiniz", veriler[indeks+1])
        
        while True:
        
            print("""
                  1- Ürün Ekleme 
                  2- Satış Yapma
                  3- Ürün Listeleme
                  4- Çıkış
                  """ )
            secim = input("Seçim Yapınız:")
            
            if secim == "1":
                urun_ekleme()
                
            elif secim == "2":
                satıs_yapma()
                
            elif secim == "3":
                urun_listeleme()
                
            elif secim == "4":
                break
        
    else:
        print("Şifre Hatalı")
    
else:
    print("Kullanıcı Adı Hatalı")




input()

# =============================================================================
# ŞATIŞLARA ÜRÜN EKLEME
# 
# ürün barkodu, ürün adi,satış fiyatı,Tutar, ürün adeti, tarih ve saat
# satışa eklenecek
# 
# 
# 
# 
# 
# 
# 
# 
# =============================================================================
