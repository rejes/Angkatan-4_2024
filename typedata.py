# Mendapatkan tipe data dari objek apapun dengan menggunakan fungsi type()

x=10
y=5
panjang=1000
print("data = ", y,", adalah tipe : ", type(y))

data_float = 1.5
print("data = ", data_float, ", adalah bertipe : ", type(data_float))

data_string = "Ningrum"
print("data = ", data_string, ", adalah bertipe : ", type(data_string))

data_bool = True
print("data = ", data_bool, ", adalah bertipe : ", type(data_bool))

data_complex = complex(5,6)
print("data = ", data_complex, ", adalah bertipe : ", type(data_complex))

from ctypes import c_double
data_c_double = c_double(10.5)
print("data = ", data_c_double, ", adalah bertipe : ", type(data_c_double))