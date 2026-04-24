import pandas as pd

data = {
    'Pemasukan': [500000, 750000, 600000],
    'Pengeluaran': [300000, 400000, 350000]
}

df = pd.DataFrame(data)

total_pemasukan = df['Pemasukan'].sum()
total_pengeluaran = df['Pengeluaran'].sum()
laba = total_pemasukan - total_pengeluaran

print("=== LAPORAN PENJUALAN TOKO ===")
print("Total Pemasukan :", total_pemasukan)
print("Total Pengeluaran :", total_pengeluaran)
print("Total Laba :", laba)
