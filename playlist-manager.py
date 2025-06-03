print()
print("======================")
print("== PLAYLIST MANAGER ==")
print("======================")
print()


def tambah_lagu(playlist):
    lagu = input("Lagu apa yang mau ditambahkan?: ")
    playlist.append(lagu)
    return f"{lagu} telah ditambahkan!"

def lihat_playlist(playlist):
    if not playlist:
        return "Playlist masih kosong!"
    return f"Playlist saat ini: {playlist}"

def hapus_lagu(playlist):
    if not playlist:
        return "Kamu belum menambahkan lagu!!"

    print("Playlist sekarang:", playlist)
    hapus = input("Mau hapus lagu apa?: ")

    if hapus in playlist:
        playlist.remove(hapus)
        return f"{hapus} telah dihapus"
    else:
        return f"Lagu '{hapus}' tidak ditemukan!"


def main():
    playlist = []

    while True:
        print()
        print("Ada yang bisa dibantu ?")
        print("1. Tambahkan Playlist")
        print("2. Lihat Playlist")
        print("3. Hapus beberapa lagu")
        print("4. Keluar")
        print()
        pilihan = input("Pilih 1, 2, 3, 4: ")

        if pilihan == "1":
            print()
            hasil = tambah_lagu(playlist)
            print(hasil)

        elif pilihan == "2":
            print()
            hasil = lihat_playlist(playlist)
            print(hasil)

        elif pilihan == "3":
            print()
            hasil = hapus_lagu(playlist)
            print(hasil)

        elif pilihan == "4":
            print("Bye!")
            break
        else:
            print("Pilihan tidak valid!")


main()
