# Target: input tanggal & bulan lahir → output zodiak

# Zodiak        Range Tanggal
# Aries         21 Maret - 19 April
# Taurus	    20 April - 20 Mei
# Gemini      	21 Mei - 20 Juni
# Cancer      	21 Juni - 22 Juli
# Leo	        23 Juli - 22 Agustus
# Virgo	        23 Agustus - 22 Sept
# Libra       	23 Sept - 22 Okt
# Scorpio       23 Okt - 21 Nov
# Sagittarius  	22 Nov - 21 Des
# Capricorn	    22 Des - 19 Jan
# Aquarius      20 Jan - 18 Feb
# Pisces	    19 Feb - 20 Maret

print()
print("===========")
print("==WELCOME==")
print("===========")
print()

try:
    tanggal = int(input("Tanggal lahir (1-31): "))
    bulan = int(input("Bulan lahir (1-12): "))
except ValueError:  # output user input harus huruf bukan angka
    print("Pakai angka bang, jangan huruf")
    exit()

if not (1 <= bulan <= 12) or not (1 <= tanggal <= 31):
    print("Bulan harus 1-12, tanggal harus 1-31!")
    exit()
else:
    if bulan == 3 and tanggal >= 21 or bulan == 4 and tanggal <= 19:
        print("Zodiak kamu Aries")
    elif bulan == 4 and tanggal >= 20 or bulan == 5 and tanggal <= 20:
        print("Zodiak kamu Taurus")
    elif bulan == 5 and tanggal >= 21 or bulan == 6 and tanggal <= 20:
        print("Zodiak kamu Gemini")
    elif bulan == 6 and tanggal >= 21 or bulan == 7 and tanggal <= 22:
        print("Zodiak kamu Cancer")
    elif bulan == 7 and tanggal >= 23 or bulan == 8 and tanggal <= 22:
        print("Zodiak kamu Leo")
    elif bulan == 8 and tanggal >= 23 or bulan == 9 and tanggal <= 22:
        print("Zodiak kamu Virgo")
    elif bulan == 9 and tanggal >= 23 or bulan == 10 and tanggal <= 22:
        print("Zodiak kamu Libra")
    elif bulan == 10 and tanggal >= 23 or bulan == 11 and tanggal <= 21:
        print("Zodiak kamu Scorpio")
    elif bulan == 11 and tanggal >= 22 or bulan == 12 and tanggal <= 21:
        print("Zodiak kamu Sagittarius")
    elif bulan == 12 and tanggal >= 22 or bulan == 1 and tanggal <= 19:
        print("Zodiak kamu Capricorn")
    elif bulan == 1 and tanggal >= 20 or bulan == 2 and tanggal <= 18:
        print("Zodiak kamu Aquarius")
    elif bulan == 2 and tanggal >= 19 or bulan == 3 and tanggal <= 20:
        print("Zodiak kamu Pisces")
    else:
        print("Masukkan tanggal dan bulan dengan benar")
