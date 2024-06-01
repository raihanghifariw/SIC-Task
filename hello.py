# 1. menggabungkan string dan angka dengan operator koma.

print('Hello',10) # Hello 10
print('=========================================')

# 2. Menggunakan operator * dan +
print('Hello' * 3) # akan menduplicate string Hello sebanyak 3 kali
print(10 * 20) # akan mengalikan bilangan tersebut
print('=========================================')

print('Hello' + 'World') # akan menggabungkan kedua string tersebut
print(10 + 20) # akan menambahkan kedua bilangan tersebut
print('=========================================')

#Output
# HelloHelloHello
# 200
# Hello World
# 30

# 3. Mengetahui Tipe data menggunakan func type()

print(type('hello')) # output : <class 'str'>
print(type(30 + 10j)) # output : <class 'complex'>
print('=========================================')

# 4. Parsing String to other data types or change all data types
print(int('100') / 2) # output : 50
print('i like number ' + str(10)) # output : i like number 10
print('=========================================')
a = None
print(type(a))

print('Halo nama saya ' + str(20) * 3)
print('=========================================')

# 5. String Indexing

print('Hello'[0])
print('Hello'[3])
print('=========================================')

print('Hello'[-1])  # Negative Index
print('=========================================')
"""Jika ingin mendapatkan character dihitung dari akhir dari sebuah string, 
maka kita dapat menggunakan tanda - dan dimulai dari indeks 1 untuk mendapatkan character terakhir dari string."""

# 6.String Built-In Function
teks = 'Halo, nama saya, Raihan'
# Split function -> Digunakan untuk memisahkan string sesuai dengan separator yang kita inginkan dan mengembalikan hasilnya sebagai sebuah list.
x = teks.split(',  ')
print(x)
print('=========================================')

a = "Halo"
b = "halo"
# islower() function -> Digunakan untuk mengecek apakah semua element dalam string adalah huruf kecil, akan mengembalikan True jika iya, dan False jika tidak
print(b.islower()) 
print(a.islower())
print('=========================================')

# count() function -> Digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string
teks = "Halo semuanya, disini saya bersama dengan budi semuanya"
x = teks.count("semuanya")
print(x)
print('=========================================')

# 7. Built-in function

# Tipe data integer
x = int("12")
y = int(12.5)

print(x)
print(y)
print('=========================================')
# output
# 12
# 12

# Tipe data float:
# pow() -> Digunakan untuk mendapatkan nilai pangkat dari suatu bilangan. Contohnya:
x = pow(3, 3) # 3 pangkat 3
y = pow(4, -3) # 3 pangkat -3

print(x)
print(y)
print('=========================================')
#output
# 27
# 0.015625

# Tipe data string
# str() -> Digunakan untuk mengubah sebuah objek menjadi string. Contohnya:
x = str(12)
y = str(12.5)

print(type(x))
print(type(y))
print('=========================================')
#output
# <class 'str'>
# <class 'str'>
