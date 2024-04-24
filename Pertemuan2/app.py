# def sum(n):
#     if(n<0):
#         raise ValueError("Angka tidak boleh negatif")
#     return n + 5

# try:
#     angka = float(input("Masukan nilai : "))
#     hasil = sum(angka)
#     print("Hasilnya adalah", hasil)
# except ValueError as e:
#     print("Pesan Error : ", e)2


try:
    a = [1,2,3]
    input = int(input('Masukan index : '))
    print(a[input])
except IndexError:
    print("Index di luar jangkauan")
except Exception as e :
    print("Terjadi kesalahan")