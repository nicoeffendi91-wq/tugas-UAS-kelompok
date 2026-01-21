import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "barang.csv")

def menu_tambah_barang():
    print("=== TAMBAH BARANG ===")

    id_barang = input("Masukkan ID barang: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    if id_barang == "" or nama == "":
        print("ID dan nama tidak boleh kosong")
        return

    try:
        harga = int(input("Masukkan harga: "))
        if harga <= 0:
            print("Harga harus lebih dari 0")
            return
    except ValueError:
        print("Harga harus angka")
        return

    try:
        stok = int(input("Masukkan stok: "))
        if stok < 0:
            print("Stok tidak boleh negatif")
            return
    except ValueError:
        print("Stok harus angka")
        return

    data = []

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, newline="", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            try:
                header = next(reader)
            except StopIteration:
                header = ["id", "nama", "harga", "stok"]

            for row in reader:
                data.append(row)
    else:
        header = ["id", "nama", "harga", "stok"]

    with open(DATA_PATH, newline="", mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print("Barang berhasil ditambahkan.")

