#!/usr/bin/env python
# coding: utf-8

# In[9]:


#import semua kelas dan fungsi dari modul tkinter
from tkinter import *

#membuat instance atau jendela utama dengan ukuran 400x240 piksel
root = tk.Tk()
root.title("My Gui")
root.geometry("400x240")

#membuat Label dengan teks "Masukan Nilai Pertama : "
lbl = Label(root, text="Masukan Nilai Pertama : ", anchor="e", width=20)
#menempatakn label pada grid baris ke-0 dan kolom ke-0
lbl.grid(column=0, row=0)

#membuat widget Entry untuk memasukkan nilai pertama dan ditempatkan pada grid baris ke-0 dan kolom ke-1 
nilai1 = Entry(root,width=20)
nilai1.grid(column=1,row=0)

#membuat Label dengan teks "Masukan Nilai Kedua : "
lbl2 = Label(root, text="Masukan Nilai Kedua : ",anchor="e",width=20)
#menempatakn label pada grid baris ke-1 dan kolom ke-0
lbl2.grid(column=0, row=1)

#membuat widget Entry untuk memasukkan nilai kedua dan ditempatkan pada grid baris ke-1 dan kolom ke-1 
nilai2 = Entry(root,width=20)
nilai2.grid(column=1,row=1)

#membuat Label dengan teks "Hasil : "
lbl3 = Label(root, text="Hasil : ",anchor="e",width=20)
#menempatakn label pada grid baris ke-2 dan kolom ke-0
lbl3.grid(column=0, row=2)

#membuat widget Label untuk menampilkan hasil perhitungan dan ditempatkan pada grid baris ke-2 dan kolom ke-1
hasil = Label(root, text="0", anchor="w",width=10)
hasil.grid(column=1,row=2)

#fungsi penjumlahan
def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))

#fungsi pengurangan
def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))
    
#fungsi perkalian
def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))

#fungsi pembagian
def bagi():
    hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))

#fungsi pangkat
def pangkat():
    hasil.configure(text=(float(nilai1.get())**float(nilai2.get())))

#fungsi modulus
def modulus():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))
    
#fungsi akar
def akar():
    hasil.configure(text=(float(nilai1.get())**(1/float(nilai2.get()))))

#membuat tombol tambah dengan fungsi tambah didalamnya dan diletakkan pada grid baris ke-3 dan kolom ke-0
btn = Button(root, text="Tambah", command=tambah)
btn.grid(column=0, row=3)

#membuat tombol kurang dengan fungsi kurang didalamnya dan diletakkan pada grid baris ke-3 dan kolom ke-1
btn = Button(root, text="Kurang", command=kurang)
btn.grid(column=1, row=3)

#membuat tombol kali dengan fungsi kali didalamnya dan diletakkan pada grid baris ke-4 dan kolom ke-0
btn = Button(root, text="Kali", command=kali)
btn.grid(column=0, row=4)

#membuat tombol bagi dengan fungsi bagi didalamnya dan diletakkan pada grid baris ke-4 dan kolom ke-1
btn = Button(root, text="Bagi", command=bagi)
btn.grid(column=1, row=4)

#membuat tombol pangkat dengan fungsi pangkat didalamnya dan diletakkan pada grid baris ke-5 dan kolom ke-0
btn = Button(root, text="Pangkat", command=pangkat)
btn.grid(column=0, row=5)

#membuat tombol modulus dengan fungsi modulus didalamnya dan diletakkan pada grid baris ke-5 dan kolom ke-1
btn = Button(root, text="Modulus", command=modulus)
btn.grid(column=1, row=5)

#membuat tombol akar dengan fungsi akar didalamnya dan diletakkan pada grid baris ke-6 dan kolom ke-0
btn = Button(root, text="Akar", command=akar)
btn.grid(column=0, row=6)

#menjalankan program hingga dihentikan oleh pengguna
root.mainloop()


# In[ ]:





# In[ ]:




