print()
print("==============")
print("====SIMPLE====")
print("==CALCULATOR==")
print("==============")
print()


def kalkulator():
    try:
        a = int(input("Masukkan angka : "))
        operasi = input("Pilih (+, -, *, /): ")
        b = int(input("Masukkan angka : "))

        if operasi == "+":
            return a + b
        elif operasi == "-":
            return a - b
        elif operasi == "*":
            return a * b
        elif operasi == "/":
            return a / b
        else:
            return "Error: operasi tidak valid"

    except ValueError:  # output ketika pengguna memasukkan huruf
        return "Beri input dengan benar"
    except ZeroDivisionError:  # output ketika pengguna membagi dengan angka 0
        return "Jangan membagi dengan 0"


hasil = kalkulator()
print(f"Hasil : {hasil}")
