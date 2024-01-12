# diskon 1 baju = 10
# diskon 2 baju = 15
# diskon lebih dari 2 baju = 20

jumlah_baju = int(input("Masukan Jumlah baju: "))
harga_baju = 0
def jumlah(harga_baju, jumlah_baju):
    urutan_baju = 1
    while (jumlah_baju != 0):
        print("Harga Baju ke: ", urutan_baju)
        harga_baju += int(input())
            
        urutan_baju+=1
        jumlah_baju-=1
    return harga_baju

if (jumlah_baju == 1):
    harga = int(input("Masukan Harga: "))
    diskon = int(input("Masukan diskon: "))
    total = harga-(harga * (diskon/100))
    print(diskon,"%")
    print("Rp",'{:,.0f}'.format(total).replace(',', '.'))
    uang = int(input("Masukan Uang pembayaran: "))
    kembali = uang - total
    print("+===============================+")
    print("Jumlah Pembayaran    :","Rp",'{:,.0f}'.format(total).replace(',', '.'))
    print("Jumlah diskon        :", diskon,"%")
    print("Kembalian            :","Rp", '{:,.0f}'.format(kembali).replace(',', '.'))
    print("+===============================+")
elif (jumlah_baju == 2):
    harga1 = int(input("Masukan Harga baju 1: "))
    harga2 = int(input("Masukan Harga baju 2: "))
    diskon = int(input("Masukan diskon: "))
    total_harga = harga1+harga2
    total = total_harga-(total_harga * (diskon/100))
    print(diskon,"%")
    print("Rp",'{:,.0f}'.format(total).replace(',', '.'))
    uang = int(input("Masukan Uang pembayaran: "))
    kembali = uang - total
    print("+===============================+")
    print("Jumlah diskon    :",diskon,"%")
    print("Jumlah Pembayaran:","Rp",'{:,.0f}'.format(total).replace(',', '.'))
    print("Kembalian        :","Rp", '{:,.0f}'.format(kembali).replace(',', '.'))
    print("+===============================+")
elif (jumlah_baju > 2):
    harga_total = jumlah(harga_baju, jumlah_baju)
    diskon = int(input("Masukan diskon: "))
    total = harga_total-(harga_total * (diskon/100))
    print(diskon,"%")
    print("Rp",'{:,.0f}'.format(total).replace(',', '.'))
    uang = int(input("Masukan Uang pembayaran: "))
    kembali = uang - total
    print("+===============================+")
    print("Jumlah diskon    :",diskon,"%")
    print("Jumlah Pembayaran:","Rp",'{:,.0f}'.format(total).replace(',', '.'))
    print("Kembalian        :","Rp", '{:,.0f}'.format(kembali).replace(',', '.'))
    print("+===============================+")