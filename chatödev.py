import tkinter as tk
from tkinter import messagebox

def hesapla(islem):
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())

        if islem == 'toplama':
            sonuc = sayi1 + sayi2
        elif islem == 'cikarma':
            sonuc = sayi1 - sayi2
        elif islem == 'carpma':
            sonuc = sayi1 * sayi2
        elif islem == 'bolme':
            if sayi2 == 0:
                messagebox.showerror("Hata", "Bir sayı sıfıra bölünemez!")
                return
            sonuc = sayi1 / sayi2
        else:
            sonuc = "Hatalı işlem"

        sonuc_label.config(text=f"Sonuç: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

# Tkinter ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x300")

# İlk sayı için giriş kutusu ve etiket
label1 = tk.Label(pencere, text="Sayı 1:")
label1.pack()
entry1 = tk.Entry(pencere)
entry1.pack()

# İkinci sayı için giriş kutusu ve etiket
label2 = tk.Label(pencere, text="Sayı 2:")
label2.pack()
entry2 = tk.Entry(pencere)
entry2.pack()

# İşlem butonları
btn_toplama = tk.Button(pencere, text="Toplama", command=lambda: hesapla('toplama'))
btn_toplama.pack()

btn_cikarma = tk.Button(pencere, text="Çıkarma", command=lambda: hesapla('cikarma'))
btn_cikarma.pack()

btn_carpma = tk.Button(pencere, text="Çarpma", command=lambda: hesapla('carpma'))
btn_carpma.pack()

btn_bolme = tk.Button(pencere, text="Bölme", command=lambda: hesapla('bolme'))
btn_bolme.pack()

# Sonuç etiketi
sonuc_label = tk.Label(pencere, text="Sonuç:")
sonuc_label.pack()

# Tkinter ana döngüsünü başlat
pencere.mainloop()
