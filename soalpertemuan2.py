    
name = "Yoshep"
list = ["John", "Doe", "Angela", "Christina"]
print(list)
list.remove("Christina")
print(list)
list.append("Julia")
list.append(name)
print(list)
print(len(list))
list[0]: "Johnson"
print(list)

inventaris = ["Laptop", "Printer", "Scanner", "Monitor"]
print(inventaris)

# Buat list inventaris
inventaris = ["Laptop", "Printer", "Scanner", "Monitor"]
print("Inventaris awal:")
print(inventaris)

# Tambahkan item baru ke dalam list inventaris
item_baru = "Keyboard"
inventaris.append(item_baru)
print("Inventaris setelah ditambahkan item baru:")
print(inventaris)

# Buat list karyawan
karyawan = ["Andi", "Budi", "Citra", "Dewi"]
print("Karyawan awal:")
print(karyawan)

# Tambahkan karyawan baru ke dalam list karyawan
karyawan_baru = "Eka"
karyawan.append(karyawan_baru)
print("Karyawan setelah ditambahkan karyawan baru:")
print(karyawan)

#List Harga produk
harga_produk = ["50000", "150000", "250000", "750000"]
print(harga_produk)

harga_baru = "100000"
harga_produk.append(harga_baru)
print(harga_produk)

inventaris.remove("Scanner")
print(inventaris)

karyawan.remove("Budi")
print(karyawan)

print(len(inventaris))
print(len(karyawan))
