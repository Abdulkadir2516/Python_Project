# listelerle alıştırma

"""
Atm Projesi part 2

Kullanıcı Sorgulama

işlemler:
    bilgileri gösterme
    para çekme
    para yatırma
    havale gönderme
    şifre değişikliği
    bakiye bilgisini gösterme
    
"""

"""
listefile= ['greenrock',
 'Abdulkadir',
 'Yeşilkaya',
 '251677',
 '2300',
 'info@greenrock.gen.tr',
 'Yalova/Armutlu',
 '5459727734',
 'burak_123',
 'Burak',
 'Tütüncüoğlu',
 '123456',
 '2200',
 'burak@gmail.com',
 'Bursa/Yıldırım',
 '5459862615',
 'mustafa_147',
 'Mustafa Batu',
 'Koyar',
 'batu2009',
 '1500',
 'm.batukoyar@gmail.com',
 'fethiye',
 '5418231526',
 ]

file = open("./file2.txt", "x", )

dosya = open("./file2.txt" , "w", encoding=("utf-8"))


for i in range(len(listefile)):
        
    dosya.write(f"{listefile[i]},")

print("işlem Başarılı")

dosya = open("./file2.txt" , "r", encoding=("utf-8"))
dosya.read()

"""

# dosya işlemleri metin dosyasına kaydedilecek veriler buradan çekilecek

file = open("./file2.txt" , "r", encoding=("utf-8"))

stringfile = str(file.read())

listefile = stringfile.split(",")

while True:
    
    k_ıd = input("Kullanıcı Adınızı Giriniz:")
    
    sifre = input("Şifrenizi Giriniz:")
    
    check = False
    
    for i in range(0, len(listefile), 8):
        
        if k_ıd == listefile[i]:
            
            if sifre == listefile[i+3]:
                
                k_index = i
                
                check = True
    
    if check:
        print("Hoşgeldiniz")
    else:
        print("hatalı giriş")
    
    while check:
        
        islemler="""
        
        işlemler:
            1- bilgileri gösterme
            2- para çekme
            3- para yatırma
            4- havale gönderme
            5- şifre değişikliği
            6- bakiye bilgisini gösterme
            7- çıkış
        
        """  
        print(islemler)
        
        secim = int(input("İşleminizi Seçiniz: "))
        
        
        if secim == 1:
            
            for i in listefile[k_index:k_index+8]:
                print(i)
        
           
        elif secim == 2:
            
            tutar =  int(input("çekmek istediğiniz tutarı giriniz:"))
            
            kontrol = True
            
            if tutar%10 != 0:
                print("çekmek istediğiniz tutar 10 ve 10\'un katları şeklinde olmak zorunda")
                kontrol = False
                
            if tutar > int(listefile[k_index+4]):
                print("çekmek istediğiniz tutar bakiyenizden büyük olamaz")
                kontrol = False
        
            if tutar > 1500:
                print("günlük çekebileceğiz tutar 1500 tl yi geçemez")
                kontrol = False
            
            if kontrol:
                listefile[k_index+4] = int(listefile[k_index+4])-tutar
                
                dosya = open("./file2.txt" , "w", encoding=("utf-8"))

                
                for i in range(len(listefile)):
                        
                    dosya.write(f"{listefile[i]},")
                
                print("işlem Başarılı")
                
                dosya = open("./file2.txt" , "r", encoding=("utf-8"))
                dosya.read()
                
                
                
        elif secim == 3:
            
            tutary =  int(input("yatırmak istediğiniz tutarı giriniz:"))
            
            listefile[k_index+4] = int(listefile[k_index+4])+tutary
            
            dosya = open("./file2.txt" , "w", encoding=("utf-8"))

            for i in range(len(listefile)):
                    
                dosya.write(f"{listefile[i]},")
            
            print("işlem Başarılı")
            
            dosya = open("./file2.txt" , "r", encoding=("utf-8"))
            dosya.read()
        
        
        elif secim == 4:
            
            hesap = input("havale yapmak istediğin kullanıcın k_ıd sini giriniz: ")
            
            kontrol_hesap = False

            for i in range(0, len(listefile), 8):

                if hesap == listefile[i]:
                    
                    kontrol_hesap=True
                    
                    tutarh = int(input("göndermek istediğiniz tutarı giriniz: "))
                
                    if tutarh > int(listefile[k_index+4]):
                        print("göndermek istediğiniz tutar bakiyenizden büyük olamaz")

                    else:
                        listefile[k_index+4] = int(listefile[k_index+4])-tutarh
                        
                        h_index = listefile.index(hesap)
                        
                        listefile[h_index+4] = int(listefile[h_index+4])+tutarh
                        
                        dosya = open("./file2.txt" , "w", encoding=("utf-8"))

                        for j in range(len(listefile)):
                                
                            dosya.write(f"{listefile[j]},")
                                                
                        dosya = open("./file2.txt" , "r", encoding=("utf-8"))
                        dosya.read()
                        
                        print("işlem Başarılı")
        
            
            if not(kontrol_hesap):
                print("Böyle bir hesaba ulaşılamadı")
                    
    
        elif secim == 5:
            
            eski = input("eski şifrenizi giriniz: ")
            
            if eski == listefile[k_index+3]:
                
                yeni = input("yeni şifrenizi giriniz: ")
                
                yeni2 = input("yeni şifrenizi tekrar giriniz: ")
                
                if yeni == yeni2:
                    
                    listefile[k_index+3] = yeni
                    
                    dosya = open("./file2.txt" , "w", encoding=("utf-8"))

                    for j in range(len(listefile)):
                            
                        dosya.write(f"{listefile[j]},")
                                            
                    dosya = open("./file2.txt" , "r", encoding=("utf-8"))
                    dosya.read()
                
                else:
                    print("şifreler birbine eşit değiller")
                
            else:
                print("girilen şifre hatalı")
                
                
        
        elif secim == 6:
            
            print("Hesabınızdaki bakiyeniz => ",listefile[k_index+4])
            
    
        elif secim == 7:
            
            break
    
    
    
    
    
    
    

"""
while True:
    
    while True:
        
        k_ıd = input("Kullanıcı Adınızı Giriniz:")
        
        sifre = input("Şifrenizi Giriniz:")
        
        # k_check = False
        
        # for i in range(3):
            
        #     if k_ıd == kul_ad[i]:
        #         k_check = True
        
        if k_ıd.lower() in kul_ad:
            
            k_ind = kul_ad.index(k_ıd)
            
            if sifre == kul_sifre[k_ind]:
                
                print("Hoşgeldiniz: ", kul_bil[(k_ind*8)+1])
                
                break
            
            else:
                print("Şifre Hatalı kullanıcı adı doğru ")
            
        else:
            print("hatalı giriş yaptınız: ")
        
    while True:
        
        islemler=\"""
        
        işlemler:
            1- bilgileri gösterme
            2- para çekme
            3- para yatırma
            4- havale gönderme
            5- şifre değişikliği
            6- bakiye bilgisini gösterme
            7- çıkış
        
        \"""  
        print(islemler)
        
        secim = int(input("İşleminizi Seçiniz: "))
        
        
        if secim == 1:
            
            for i in kul_bil[k_ind:k_ind+8]:
                print(i)
            
        elif secim == 2:
            
            tutar =  int(input("çekmek istediğiniz tutarı giriniz:"))
            
            kontrol = True
            
            if tutar%10 != 0:
                print("çekmek istediğiniz tutar 10 ve 10\'un katları şeklinde olmak zorunda")
                kontrol = False
                
            if tutar > kul_bil[k_ind+4]:
                print("çekmek istediğiniz tutar bakiyenizden büyük olamaz")
                kontrol = False
        
            if tutar > 1500:
                print("günlük çekebileceğiz tutar 1500 tl yi geçemez")
                kontrol = False
            
            if kontrol:
                kul_bil[k_ind+4] = kul_bil[k_ind+4]-tutar
                print("işlem Başarılı")
            
        elif secim == 3:
            
            tutary =  int(input("yatırmak istediğiniz tutarı giriniz:"))
            
            kul_bil[k_ind+4] = kul_bil[k_ind+4]+tutary
            print("işlem Başarılı")
            
        elif secim == 4:
            
            hesap = input("havale yapmak istediğin kullanıcın k_ıd sini giriniz: ")
            
            if hesap in kul_ad:
                
                tutarh = int(input("göndermek istediğiniz tutarı giriniz: "))
                
                if tutarh > kul_bil[k_ind+4]:
                    print("göndermek istediğiniz tutar bakiyenizden büyük olamaz")
                
                else:
                    kul_bil[k_ind+4] = kul_bil[k_ind+4]-tutarh
                    
                    h_ind = kul_bil.index(hesap)
                    
                    kul_bil[h_ind+4] = kul_bil[h_ind+4]+tutarh
                    
                    print("işlem Başarılı")
    
        elif secim == 5:
            
            eski = input("eski şifrenizi giriniz: ")
            
            if eski == kul_sifre[k_ind]:
                
                yeni = input("yeni şifrenizi giriniz: ")
                
                yeni2 = input("yeni şifrenizi tekrar giriniz: ")
                
                if yeni == yeni2:
                    
                    kul_sifre[k_ind] = yeni
                    kul_bil[k_ind+3] = yeni2
                
                else:
                    print("şifreler birbine eşit değiller")
                
            else:
                print("girilen şifre hatalı")
            
        elif secim == 6:
            
            print("Hesabınızdaki bakiyeniz => ",kul_bil[k_ind+4])
            
            
        elif secim == 7:
            
            break
    
"""


